import arcpy

arcpy.env.overWriteOutput = True

arcpy.env.workspace = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb'

arcpy.AddField_management ('CallsforService','Crime_Explanation','TEXT','', '', '','Crime_Explanation', '', '', '')

featureClass = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb\CallsforService'

fieldList = ['CFSType','Crime_Explanation']


with arcpy.da.UpdateCursor(featureClass, fieldList) as cursor:
  for row in cursor:
      if (row [0] == 'Burglary Call'):
            row [1] = 'This is a burglary'			   
      cursor.updateRow(row)