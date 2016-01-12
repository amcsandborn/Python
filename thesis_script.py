###########################################
# Author: Avery Sandborn
# Date: December 3, 2014
# File: project.py
###########################################

#%%
###########################################
# Section 1
# USER INPUTS
###########################################

# BEFORE YOU RUN THE CODE, MAKE SURE YOU DO THE FOLLOWING:

# Change variable "workspace" to your project folder
workspace = "R:\\Engstrom_Research\\GHANA\\Avery\\AGU_2014_v03\\Python_Project\\"

# create folders in workspace named "Original_Data", "Spatial_Features", "Zonal_Stats", "Census_Data", and "Arrays"
workspace_original = workspace + "Original_Data\\"
workspace_spatial_features = workspace + "Spatial_Features\\"
workspace_zonal_stats = workspace + "Zonal_Stats\\"
workspace_census = workspace + "Census_Data\\"
workspace_arrays = workspace + "Arrays\\"

# place NB shapefile in "Original_Data" folder and set to variable
nb_shp = "NB_selected_v03.shp"

# Set join field that is the same in both census data and zonal stats data
join_field = "FMV_NUMBER"

# place spatial features into "Spatial_Features" folder

# place census data in .xls file in "Original_Data" folder (must be .xls, not .xlsx)
# set the worksheet name of the census data to a variable
excel_worksheet = "neigbhorhood_veg_imp"

# set the deliete field list to include "OID_x" and "OID_y", as well as any fileds from zonal_stats tables and census table that you want deleted (i.e. not in the correlation matrix)
delete_field_list = ["OID_x", "COUNT", "AREA", "MIN", "MAX", "RANGE", "OID_y", "OBJECTID", "Neighborho", "coverage", "SUM_AREA", "area_km", "Shape_Leng", "Shape_Area", "imp_2002", "imp_2010", "imp_change", "veg_2002", "veg_2010", "veg_change"]

#%%
###########################################
# Section 2
# BASIC PYTHON
###########################################

# Inform user script is beginning
print "" ; print "Beginning Script" ; print ""

# Import Modules
import arcpy
import os
import numpy
import pandas
import csv
import xlrd
import pylab

# Turn on Spatial Analysis Extension
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")

from arcpy.da import *

# set overwrite output function to true
arcpy.env.overwriteOutput = True

#%%
###########################################
# Section 3
# Define Functions
###########################################

# https://geonet.esri.com/thread/110894

# define a function that converts table to csv file 
def TableToCSV(fc,CSVFile):  
    
    # set fields equal to the attribute columns in the table
    fields = [f.name for f in arcpy.ListFields(fc) if f.type <> 'Geometry']
    
    # open the csv file name for writing
    with open(CSVFile, 'w') as f:  
        
        # write the fields into the csv file
        f.write(','.join(fields)+'\n') #csv headers  
        
        # use a search cursor to join each row in the table to the csv file
        with arcpy.da.SearchCursor(fc, fields) as cursor:  
            for row in cursor:  
                # comma delimited file
                f.write(','.join([str(r) for r in row])+'\n')  

#%%
###########################################
# Section 4
# CREATE SPATIAL FEATURE IMAGES
###########################################

# Get original image
# call the mappy modules
# run feas.py on them
# get all the spatial features

#%%
###########################################
# Section 5
# GET THE ZONAL STATISTICS OF EACH SPATIAL FEATURE
###########################################

print "Running the \"Zonal Statistics as Table\" tool..."

# Make Neighborhood shapefile a layer
arcpy.MakeFeatureLayer_management(workspace_original + nb_shp, "NB_LYR")

# Make a list of spatial features
spatial_feature_list = os.listdir(workspace_spatial_features)

# make list of base names of spatial features
base_name_list = []

# make a list of zonal stats tables (DBFs only)
zonal_stats_list = []

# for every spatial feature in the list:
for spatial_feature in spatial_feature_list:
    
    # set in raster as variable
    in_value_raster = workspace_spatial_features + spatial_feature
    
    # set output table variable
    base_name = os.path.splitext(spatial_feature)[0]
    base_name_list.append(base_name)
    out_table = workspace_zonal_stats + base_name + "_zonalstats.dbf"
    
    # run zonal stats as table tool
    # ZonalStatisticsAsTable(in_zone_data, zone_field, in_value_raster, out_table, {ignore_nodata}, {statistics_type})
    arcpy.sa.ZonalStatisticsAsTable("NB_LYR", join_field, in_value_raster, out_table, "NODATA", "ALL")
    
    zonal_stats_list.append(base_name + "_zonalstats.dbf")

#%%
###########################################
# Section 6
# CONVERT ZONAL STAT TABLE FROM DBF TO CSV
###########################################

print "Converting Zonal Stat table from DBF to CSV..."

# make a list of zonal stats tables (DBFs only)
zonal_stats_list_new = []

# for each zonal stat, merge it with census data:
for zonal_stats in zonal_stats_list:

    # set the in table and out_table variables 
    base_name = os.path.splitext(zonal_stats)[0]
    in_dbf = workspace_zonal_stats + base_name + ".dbf"
    out_csv = workspace_zonal_stats + base_name + ".csv"

    # use the TableToCSV function to convert the dbf to a csv
    TableToCSV(in_dbf, out_csv)
    
    # read the csv in, separate by commas
    csv_df = pandas.read_csv(out_csv, sep = ",", header = 0)
    
    # get the shape of the csv (number of rows and columns)
    csv_df.shape
    csv_df.head
    
    # append the csv to the list for later use
    zonal_stats_list_new.append(base_name + ".csv")
    
#%%
###########################################
# Section 7
# CONVERT CENSUS DATA TABLE FROM EXCEL TO CSV
###########################################

print "Converting Census Data table from DBF to CSV..."

# make a list of census data (XLS only)
census_data_list = []
for name in os.listdir(workspace_original):
    if name.endswith(".xls"):
        census_data_list.append(name)

census_data_list_new = []

# for each census data xls, copy to new file, and delete un-needed fields
for census_data in census_data_list:
    
    # set the input table to the specific worksheet
    base_name = os.path.splitext(census_data)[0]
    workbook = xlrd.open_workbook(workspace_original + census_data)
    worksheet = workbook.sheet_by_name(excel_worksheet)
    input_table = workspace_original + census_data + "\\" + excel_worksheet + "$"   
    
    # convert the xls worksheet to a dbf
    arcpy.TableToTable_conversion(input_table, workspace_census, base_name + ".dbf")
    
    in_dbf = workspace_census + base_name + ".dbf"
    out_csv_census = workspace_census + base_name + ".csv"
    
    # use the TableToCSV function to convert the dbf to a csv
    TableToCSV(in_dbf, out_csv_census)
    
    # read the csv in, separate by commas
    census_csv = pandas.read_csv(out_csv_census, sep = ",", header = 0)
    
    # get the shape of the csv (number of rows and columns)
    census_csv.shape
    census_csv.head    
    
    # append new sorted dbfs to a new list for later use
    census_data_list_new.append(base_name + ".csv")
    
#%%
###########################################
# Section 8
# JOIN THE TWO CSVS TOGETHER
###########################################

print "Joining the zonal stats csv and the census data csv..."

csv_merge_list_new = []

# for each zonal stat csv, join the census csv to it
for zonal_stats in base_name_list:
    
    # read in the two csvs
    csv_zonal = pandas.read_csv(workspace_zonal_stats + zonal_stats + "_zonalstats.csv", sep = ",", header = 0)
    csv_census = pandas.read_csv(out_csv_census, sep = ",", header = 0)

    # merge the two csvs
    csv_merge = pandas.merge(csv_zonal, census_csv, how='left', on=join_field,  left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True)

    # get the name for the merged csv file
    base_name = os.path.splitext(zonal_stats)[0]
    out_csv = workspace_zonal_stats + base_name + "_merge.csv"    
    
    # write it to csv
    csv_merge.to_csv(out_csv)
    
    # add to list for later use
    csv_merge_list_new.append(base_name + "_merge.csv")
    
#%%
###########################################
# Section 9
# EDIT THE CSV TABLE
###########################################

print "Dropping unneeded columns from the CSV file..."

csv_merge_drop_list = []

# for each merged file, drop the columns you don't need
for csv_merge in base_name_list:

    # read in the csv merge file
    csv_merge_read = pandas.read_csv(workspace_zonal_stats + csv_merge + "_merge.csv", sep = ",", header = 0)

    # drop the columns
    csv_merge_drop = csv_merge_read.drop(delete_field_list, 1)

    # get the name for the merged csv file
    base_name = os.path.splitext(csv_merge)[0]
    out_csv = workspace_zonal_stats + base_name + "_drop.csv"    

    # write it to csv
    csv_merge_drop.to_csv(out_csv)

    # drop the two weird columns from the merged file
    # http://stackoverflow.com/questions/15887372/remove-multiple-columns

    # rows to delete
    delete = ["", "Unnamed: 0"]

    csv1 = out_csv
    csv2 = workspace_zonal_stats + base_name + "_finished.csv"

    # for each csv file, drop the files
    with open(csv1) as infile, open(csv2, "wb") as outfile:

        r = csv.DictReader(infile)       
        firstrow = next(r)
        fields = r.fieldnames
        w = csv.DictWriter(outfile, [field for field in fields if not field in delete], extrasaction="ignore")
        w.writeheader()
        w.writerow(firstrow)
        for row in r:
            w.writerow(row)
    
    # add to list for later use
    csv_merge_drop_list.append(base_name + "_finished.csv")    

#%%
###########################################
# Section 10
# CREATE CORRELATION MATRIX
###########################################

print "Creating correlation matrix..."

""" Useful Links on Creating Correlation Matrix:
http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting
http://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy
http://pythonprogramming.net/pandas-statistics-correlation-tables-how-to/
http://web.stanford.edu/~mwaskom/software/seaborn/examples/many_pairwise_correlations.html
http://stackoverflow.com/questions/12319969/how-to-use-numpy-genfromtxt-when-first-column-is-string-and-the-remaining-column
http://penandpants.com/2012/03/09/reading-text-tables-with-python/
http://glowingpython.blogspot.com/2012/10/visualizing-correlation-matrices.html
http://stackoverflow.com/questions/15988413/python-pylab-pcolor-options-for-publication-quality-plots
"""

correlation_list = []
matrix_with_header_list = []

# Get the header you want to use for the matrix header, open the csv for reading
base_name = os.path.splitext(csv_merge)[0]
with open(workspace_zonal_stats + base_name + "_finished.csv" , "r") as f:
    # read the top row (header row)
    reader = csv.reader(f)
    row1 = next(reader)
    
with open(workspace_zonal_stats + base_name + "_finished.csv" , "r") as f:
    # read the top row (header row)
    reader = csv.reader(f)
    row2 = next(reader)
    
row2.insert(0, "")

# for each csv, convert it into an array
for csv_file in base_name_list:

    base_name = os.path.splitext(csv_file)[0]
    
    # read in the csv, get the values
    csv_df = pandas.read_csv(workspace_zonal_stats + csv_file + "_finished.csv", sep = ",", header = 0)
    csv_values = csv_df.values

    # make the correlation coefficient matrix of the csv values
    corr_coef_matrix = numpy.corrcoef(csv_values, rowvar = False)
    
    # save the matrix as a csv
    matrix_csv = workspace_arrays + base_name + "_matrix.csv"
    numpy.savetxt(matrix_csv, corr_coef_matrix, delimiter = ",")

    # append it to the list for later use
    correlation_list.append(base_name + "_matrix.csv")

    # add the row headers, columns header to the matrix array 
    df1 = pandas.DataFrame(corr_coef_matrix, index = row1, columns = row1)

    # convert the array with header to csv
    df1.to_csv(workspace_arrays + base_name + "_headers.csv")
    
    # append to list for later use
    matrix_with_header_list.append(base_name + "_headers.csv")
    
#%%
###########################################
# Section 11
# END THE SCRIPT
###########################################

# Inform user script is ending
print "" ; print "Script Completed" ; print ""
