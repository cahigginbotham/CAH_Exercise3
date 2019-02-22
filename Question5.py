import arcpy 

arcpy.env.overWriteOutput = True
arcpy.CreateFileGDB_management(r'C:\Users\cahig\Desktop\Exercise 3', 'q5_exercise.gdb')
#I had to run this several times to make it work and the overwrite would not work for the GDB
featureList = ['CapitalCities','Landmarks','HistoricPlaces','StateNames','Nationalities','Rivers']

current_workspace = (r'C:\Users\cahig\Desktop\Exercise 3\q5_exercise.gdb')

geometry_type_polygon = "POLYGON"
geometry_type_line = "POLYLINE"
geometry_type_point = "POINT"

spatial_reference = arcpy.SpatialReference(102100)



def createPolygonFeatureClass(in_fc_name,overwriteSetting):
    arcpy.env.overWriteOutput = overwriteSetting
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type_polygon,'', "DISABLED", "DISABLED", spatial_reference)
def createLineFeatureClass(in_fc_name,overwriteSetting):
    arcpy.env.overWriteOutput = overwriteSetting
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type_line,'', "DISABLED", "DISABLED", spatial_reference)
def createPointFeatureClass(in_fc_name,overwriteSetting):
    arcpy.env.overWriteOutput = overwriteSetting
    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type_point,'', "DISABLED", "DISABLED", spatial_reference)

for feature in featureList:
    if (feature == 'Rivers'):
      print(feature)
      createLineFeatureClass(feature,True)
    elif (feature == 'Landmarks'or'HistoricPlaces'):
       print(feature)
       createPointFeatureClass(feature,True)
    else:
       print(feature)
       createPolygonFeatureClass(feature,True)
    
        

  