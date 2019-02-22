import arcpy
arcpy.env.workspace = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb'

featureClass = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb\CallsforService'

fieldList = ['CFSType','Crime_Explanation']


arcpy.SelectLayerByAttribute_management (featureClass, 'NEW_SELECTION',"CFSType = 'Burglary Call'") 

arcpy.CopyFeatures_management (featureClass,'Burglary_Selection')
         
      
