import arcpy

arcpy.env.overWriteOutput = True

arcpy.env.workspace = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb'


featureClass = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb\CallsforService'

fieldList = ['CFSType','Crime_Explanation','OBJECTID']
crimeCount = 0

result = arcpy.GetCount_management(featureClass)
print(result)
