#Populate fields in featureclass 
import arcpy
arcpy.env.workspace = r"C:\Users\vincent.law\Documents\CW\CW_Rochon_Sands_PP5.gdb"
featureClass = arcpy.ListFeatureClasses()
for fc in featureClass:
    arcpy.CalculateField_management(fc, "Unique_ID", "!OBJECTID!", "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "PASITES_ID", '"1046"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "Park_Type", '"PP"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "Region_Name", '"Central"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "District_Name", '"Wainwright"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "Park_Name", '"Rochon Sands PP"', "PYTHON_9.3", "")
    



