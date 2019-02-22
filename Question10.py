import arcpy
import os
arcpy.env.overWriteOutput = True

arcpy.env.workspace = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb'

workspace = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb'
outworkspace = r'C:\Users\cahig\Desktop\Exercise 3\Exercise 3.gdb\Exercise 3.gdb\join'
targetFeatures = os.path.join(workspace, "Tracts")
joinFeatures = os.path.join(workspace, "General_Offense")




arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, outworkspace)
