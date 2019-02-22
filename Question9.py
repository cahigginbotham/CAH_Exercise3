import arcpy 

arcpy.env.overWriteOutput = True
arcpy.env.workspace = r'C:\Users\cahig\Desktop\Exercise 3\q5_exercise.gdb'

featureList = ['CapitalCities','Landmarks','HistoricPlaces','StateNames','Nationalities','Rivers']

workspace = r'C:\Users\cahig\Desktop\Exercise 3\q5_exercise.gdb'
domName = "Landmarks"
gdb = r'C:\Users\cahig\Desktop\Exercise 3\q5_exercise.gdb'
inFeatures = r'C:\Users\cahig\Desktop\Exercise 3\q5_exercise.gdb\Landmarks'
inField = "Type"



arcpy.AddField_management ('Landmarks','Type','TEXT','', '', '','Type', '', '', '')

arcpy.CreateDomain_management (workspace, 'Landmarks', '', 'TEXT', 'CODED', '', '')

domDict = {"BL":"Building", "BF": "Battlefield", "CM": "Cemetary", 
           "AR": "Archeology", "AR": "Art"}

for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
    
arcpy.AssignDomainToField_management(inFeatures, inField, domName)