# Author: Avery Sandborn
# Name: sandborn_project.py
# Date Written: 11/20/12
# Date Modified: 12/10/12
# Variables Used:
    # NoPath: exception for error handling associated with the file paths
    # InvalidResponse: exception for error handling associated with the user response
    # LayerResponse: exception for the error handling associated with the user response
    # r_directory: file path to data sources
    # s_directory: file path to output data
    # continueVar: variable used to determine if the user wants to make another map
    # query: query to select area of interest
    # outshp: output variable for easy access
    # countyshp: shapefile of the counties
    # Layer1: user input to indicate if they want to use the banks layer
    # Layer2: user input to indicate if they want to use the coffee layer
    # Layer3: user input to indicate if they want to use the convenience layer
    # Layer4: user input to indicate if they want to use the grocery layer
    # Layer5: user input to indicate if they want to use the markets layer
    # banks: shortcut to bankes layer
    # coffee: shortcut to coffee layer
    # convenience: shortcut to convenience layer
    # grocery: shortcut to grocery shapefile
    # markets: shortcut to market shapefile
    # Amenitites: list of desired amenities
    # total: output string of number of points in shapefile
    # totalValue: output number of points in shapefile
    # mapdocument: mxd source in data source
    # mapdocument2: mxd copied to output directory
    # dataframe: dataframe of mapdocument2
    # roads2: roads layer
    # a: amenity index in Amenities List
    # amenity: amenity layer
    # legend: legend element of mxd
    # author: author text element of mxd
    # title: title text element of mxd
    # deletelayers: list of layers to delete so that you can make another map
    # layer: layers to delete
    # continueVar2: user input to indicate if they want to remake their map
# Outline of main tasks performed:
    # Greet the User
    # Import modules, pass exceptions, set directory variables
    # Check to see if directories exist
    # clip county shapefile to area of interest (Baltimore City)
    # Have user specify which layers they want to include on their map
    # Clip each amenity layer and give count of points
    # Create a MXD document to create map
    # Edit legend, title, author elements
    # Export map to pdf
    # Delete all files
    # ask the user if they want to remake their map
    # exit application
# Final Product
    # Map of city with specified amenities

######################################

# Greet the user, explain what this tool does
print "Greetings User!"
print ""
print "This Daily Errands Mapping Application will help you to plan your day in the most efficient way possible!  This tool will output a map that shows you exactly where all your frequently visited destinations are located."
print ""

######################################

# Import the arcpy module
import arcpy
import os

# Pass the NoPath Exception
class NoPath(Exception):
    pass

# Pass the InvalidResponse Exception
class InvalidResponse(Exception):
    pass

# Pass the InvalidResponse Exception
class LayerResponse(Exception):
    pass

# Create directory file path variables
r_directory = "C:/Users/asandborn/Downloads/Sandborn_2012_Python_Sample/Sandborn_2012_Python_Sample/Data/"
s_directory = "C:/Users/asandborn/Downloads/Sandborn_2012_Python_Sample/Sandborn_2012_Python_Sample/Final_Outputs/"

######################################

# Error handling: check to see if the input file path directory is set right

try:
    # if the r_directory does not exist
    if os.path.exists(r_directory) == False:
        # raise the NoPath error
        raise NoPath
    # if the r_directory does exist
    else:
        print "Data folder (r_directory) does exist, continuing tool execution."
        
except NoPath:
    # while the r_directory does not exist
    while (os.path.exists(r_directory) == False):
        # ask the user to retype the correct file
        print "Data folder (r_directory) does NOT exist."
        print ""
        r_directory = input('Please enter an existing file path that contains the data.  Please use forward slashes instead of backward slashes, and be sure to include the last backslash.  Use quotations.  Follow the naming convention ("G:/geog476/final_project/Data/"): ')
        print ""
        
except:
    print arcpy.GetMessages(2)

print ""

# Error handling: check to see if the output file path directory is set right

try:
    # if the s_directory does not exist
    if os.path.exists(s_directory) == False:
        # raise the NoPath error
        raise NoPath
    # if the s_directory does exist
    else:
        print "Output folder (s_directory) does exist, continuing tool execution."   

except NoPath:
    # while the r_directory does not exist
    while (os.path.exists(s_directory) == False):
        # ask the user to retype the correct file
        print "Output folder (s_directory) does NOT exist."
        print ""
        s_directory = input('Please enter an existing file path where you can output the data.  Please use forward slashes instead of backward slashes, and be sure to include the last backslash.  Use quotations.  Follow the naming convention ("G:/geog476/final_project/Final_Outputs/"): ')
        print ""

except:
    print arcpy.GetMessages(2)
    
print ""

######################################

# WHILE LOOP to let the user define how long they will continue working with the application

continueVar = "Yes"
while continueVar == "Yes":

######################################

    # Clip the state shapefile to the specific county

    # Define SQL query in Python
    query = '"NAME" LIKE \'Baltimore City\''

    # Create an output variable for easy access
    outshp = str(s_directory) + "BaltCity.shp"

    # Select only specific county from all counties, and make a new shapefile
    countyshp = arcpy.Select_analysis(str(r_directory) + "co_md_project.shp", str(s_directory) + "BaltCity.shp", query)

    # Allow the user to select which supporting layers they would like to add to the map
    Layer1 = input("Would you like to visit a bank? Please enter 'Yes' or 'No'(include the single quotes): ")
    print ""
    Layer2 = input("Would you like to visit a coffee shop? Please enter 'Yes' or 'No'(include the single quotes): ")
    print ""
    Layer3 = input("Would you like to visit a convenience store? Please enter 'Yes' or 'No'(include the single quotes): ")
    print ""
    Layer4 = input("Would you like to visit a grocery store? Please enter 'Yes' or 'No'(include the single quotes): ")
    print ""
    Layer5 = input("Would you like to visit a farmer's market? Please enter 'Yes' or 'No'(include the single quotes): ")

    # Error handling: check to see if user input is correct
    try:
        # if the user input is not 'Yes'
        if Layer1 == 'Yes':
            Layer1 = 'Yes'
        elif Layer1 == 'yes':
            Layer1 = 'Yes'
        elif Layer1 == 'Y':
            Layer1 = 'Yes'
        elif Layer1 == 'y':
            Layer1 = 'Yes'
        elif Layer1 == 'YES':
            Layer1 = 'Yes'
        else:
            raise LayerResponse     
    except LayerResponse:
        Layer1 = 'No'
    except:
        print arcpy.GetMessages(2)

    try:
        # if the user input is not 'Yes'
        if Layer2 == 'Yes':
            Layer2 = 'Yes'
        elif Layer2 == 'yes':
            Layer2 = 'Yes'
        elif Layer2 == 'Y':
            Layer2 = 'Yes'
        elif Layer2 == 'y':
            Layer2 = 'Yes'
        elif Layer2 == 'YES':
            Layer2 = 'Yes'
        else:
            raise LayerResponse     
    except LayerResponse:
        Layer2 = 'No'
    except:
        print arcpy.GetMessages(2)

    try:
        # if the user input is not 'Yes'
        if Layer3 == 'Yes':
            Layer3 = 'Yes'
        elif Layer3 == 'yes':
            Layer3 = 'Yes'
        elif Layer3 == 'Y':
            Layer3 = 'Yes'
        elif Layer3 == 'y':
            Layer3 = 'Yes'
        elif Layer3 == 'YES':
            Layer3 = 'Yes'
        else:
            raise LayerResponse     
    except LayerResponse:
        Layer3 = 'No'
    except:
        print arcpy.GetMessages(2)

    try:
        # if the user input is not 'Yes'
        if Layer4 == 'Yes':
            Layer4 = 'Yes'
        elif Layer4 == 'yes':
            Layer4 = 'Yes'
        elif Layer4 == 'Y':
            Layer4 = 'Yes'
        elif Layer4 == 'y':
            Layer4 = 'Yes'
        elif Layer4 == 'YES':
            Layer4 = 'Yes'
        else:
            raise LayerResponse     
    except LayerResponse:
        Layer4 = 'No'
    except:
        print arcpy.GetMessages(2)

    try:
        # if the user input is not 'Yes'
        if Layer5 == 'Yes':
            Layer5 = 'Yes'
        elif Layer5 == 'yes':
            Layer5 = 'Yes'
        elif Layer5 == 'Y':
            Layer5 = 'Yes'
        elif Layer5 == 'y':
            Layer5 = 'Yes'
        elif Layer5 == 'YES':
            Layer5 = 'Yes'
        else:
            raise LayerResponse     
    except LayerResponse:
        Layer5 = 'No'
    except:
        print arcpy.GetMessages(2)

    print ""
    print "Thank you.  Please sit back and relax while your map is being created."
    print ""

    # create shortcut variables to shapefiles
    banks = "Banks_2007"
    coffee = "CoffeeShops_2007"
    convenience = "Convience_Stores_2007"
    grocery = "Grocery_20073"
    markets = "Markets_2007"

    # Create an empty list for only those amenities that the user selected
    Amenities = []

    # for each layer, append it to the empty Amenities list if the user said 'Yes'.
    if Layer1 == 'Yes':

        # Clip each desired point shapefile to the spcified county
        arcpy.Clip_analysis(r_directory + banks + ".shp", countyshp, s_directory + banks + "_clip.shp")

        # Find the total number of points within county
        total = arcpy.GetCount_management(s_directory + banks + "_clip.shp")
        totalValue = total.getOutput(0)
        print "There are " + totalValue + " bank locations in Baltimore City."

        # append only the desired amenitites to the list
        Amenities.append(s_directory + banks + "_clip.shp")

        print ""

    # for each layer, append it to the empty Amenities list if the user said 'Yes'.
    if Layer2 == 'Yes':

        # Clip each desired point shapefile to the spcified county
        arcpy.Clip_analysis(r_directory + coffee + ".shp", countyshp, s_directory + coffee + "_clip.shp")

        # Find the total number of points within county
        total = arcpy.GetCount_management(s_directory + coffee + "_clip.shp")
        totalValue = total.getOutput(0)
        print "There are " + totalValue + " coffee shop locations in Baltimore City."

        # append only the desired amenitites to the list
        Amenities.append(s_directory + coffee + "_clip.shp")

        print ""

    # for each layer, append it to the empty Amenities list if the user said 'Yes'.
    if Layer3 == 'Yes':

        # Clip each desired point shapefile to the spcified county
        arcpy.Clip_analysis(r_directory + convenience + ".shp", countyshp, s_directory + convenience + "_clip.shp")

        # Find the total number of points within county
        total = arcpy.GetCount_management(s_directory + convenience + "_clip.shp")
        totalValue = total.getOutput(0)
        print "There are " + totalValue + " convenience store locations in Baltimore City."

        # append only the desired amenitites to the list
        Amenities.append(s_directory + convenience + "_clip.shp")

        print ""

    # for each layer, append it to the empty Amenities list if the user said 'Yes'.
    if Layer4 == 'Yes':

        # Clip each desired point shapefile to the spcified county
        arcpy.Clip_analysis(r_directory + grocery + ".shp", countyshp, s_directory + grocery + "_clip.shp")

        # Find the total number of points within county
        total = arcpy.GetCount_management(s_directory + grocery + "_clip.shp")
        totalValue = total.getOutput(0)
        print "There are " + totalValue + " grocery store locations in Baltimore City."

        # append only the desired amenitites to the list
        Amenities.append(s_directory + grocery + "_clip.shp")

        print ""

    # for each layer, append it to the empty Amenities list if the user said 'Yes'.
    if Layer5 == 'Yes':

        # Clip each desired point shapefile to the spcified county
        arcpy.Clip_analysis(r_directory + markets + ".shp", countyshp, s_directory + markets + "_clip.shp")

        # Find the total number of points within county
        total = arcpy.GetCount_management(s_directory + markets + "_clip.shp")
        totalValue = total.getOutput(0)
        print "There are " + totalValue + " farmer's market locations in Baltimore City."

        # append only the desired amenitites to the list
        Amenities.append(s_directory + markets + "_clip.shp")

        print ""

    ######################################

    # Get a premade mxd, save a copy of it
    mapdocument = arcpy.mapping.MapDocument(r_directory + "errands.mxd")
    mapdocument.saveACopy(s_directory + "errands.mxd")
    del mapdocument

    # Define the new mapdocument, define the new data frame
    mapdocument2 = arcpy.mapping.MapDocument(s_directory + "errands.mxd")
    dataframe = arcpy.mapping.ListDataFrames(mapdocument2)[0]

    # Create a layer from a feature shapefile which contains the data
    arcpy.MakeFeatureLayer_management(r_directory + "MD_interstates.shp", "Interstates")
    arcpy.SaveToLayerFile_management("Interstates", s_directory + "roads.lyr")

    # Add roads layer for reference
    roads2 = arcpy.mapping.Layer(s_directory + "roads.lyr")
    arcpy.mapping.AddLayer(dataframe, roads2)
    arcpy.ApplySymbologyFromLayer_management(roads2, s_directory + "roads.lyr")

    ######################################

    # For each amenity they want to visit, add it to the layout

    # Use new list loop that has only desired amenitites in it
    for a in Amenities:
        # Find layer, and add layer to data frame
        amenity = arcpy.mapping.Layer(a)
        arcpy.mapping.AddLayer(dataframe, amenity)
        del amenity

        # Refresh acrive view and TOC to make sure that every layer is there
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

    ######################################

    # Get legend object, returns an array
    legend = arcpy.mapping.ListLayoutElements(mapdocument2, "LEGEND_ELEMENT")[0]

    # Set the legend to update automatically and reflec the layers in the view:
    legend.autoAdd = True

    # Refresh acrive view and TOC to make sure that every layer is there
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    # Add author's name to map, second text element in document, hence item 1
    author = arcpy.mapping.ListLayoutElements(mapdocument2, "TEXT_ELEMENT")[0]
    author.text = "Author's Name: Avery Sandborn"

    # Refresh acrive view and TOC to make sure that every layer is there
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    # Add title to map
    title = arcpy.mapping.ListLayoutElements(mapdocument2, "TEXT_ELEMENT")[1]

    # Modify the text of your title
    title.text = "Daily Errand Destinations in Baltimore City"

    # Refresh acrive view and TOC to make sure that every layer is there
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    # Export the map to PDF in the page layout view (not data view)
    arcpy.mapping.ExportToPDF(mapdocument2, s_directory + "errands.pdf", "PAGE_LAYOUT")

    ######################################

    # Delete layers because you already made the PDF, so you can make an additional map if desired
    deletelayers = arcpy.mapping.ListLayers(mapdocument2, "", dataframe)

    # Remove all layers from view
    for layer in deletelayers:
        arcpy.mapping.RemoveLayer(dataframe, layer)

    for a in Amenities:
        arcpy.Delete_management(a)

    arcpy.Delete_management(s_directory + "roads.lyr")
    arcpy.Delete_management(countyshp)

    # delete files so that you can make additional maps if desired
    del mapdocument2
    del dataframe
    
    # : Once the user has declined to continue, delete the lab08.mxd document
    arcpy.Delete_management(s_directory + "errands.mxd")

    ######################################

    # Inform user that their desired map is done and can be found within the specified directory
    print "Your map is completed and can be found in PDF version in the following directory: " + s_directory + "errands.pdf"
    print ""
    print "Please save your map to your own hardrive now.  When this application is closed, your map will be deleted.  Additionally, make sure that you do not have the map open.  Please close the map now."
    print ""



    # Ask user if they want to continue in the application
    continueVar2 = input("Would you like re-make your map and start again? Please enter 'Yes' or 'No' (include the quotations): ")
    print ""

    # Once the user has declined to continue, delete the pdf document
    arcpy.Delete_management(s_directory + "errands.pdf")

    # Error handling: check to see if user input is correct

    try:
        # if the user input is not 'Yes' raise the exception
        if continueVar2 == 'Yes':
            continueVar = 'Yes'
        elif continueVar2 == 'yes':
            continueVar = 'Yes'
        elif continueVar2 == 'Y':
            continueVar = 'Yes'
        elif continueVar2 == 'y':
            continueVar = 'Yes'
        elif continueVar2 == 'YES':
            continueVar = 'Yes'
        else:
            raise InvalidResponse     

    except InvalidResponse:
        # exit the application if the user provides an invalid response
        print "Either you do not want to continue, or you have entered an invalid response, exiting the application now."
        continueVar = 'No'
        print ""

    except:
        print arcpy.GetMessages(2)
    
    # END WHILE LOOP

######################################

# 3f: Thank the user for using your application
print "Thank you for using the Daily Errands Mapping Application!  I hope you enjoyed your time with us today.  Come again soon!"
print ""

