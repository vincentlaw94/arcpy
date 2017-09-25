#Populate fields in featureclass 
import arcpy
arcpy.env.workspace = r"C:\Users\vincent.law\Documents\CW\CW_Rochon_Sands_PP5.gdb"

featureClass = arcpy.ListFeatureClasses()

a2 = """def rep_field(in_fld, rep_value):
	targets = ['W:\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\Rochon Sands PP\ROCHONSANDSPP05102014GB~files','W:\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\Rochon Sands PP\ROCHONSANDSPP06102014~files','W:\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\Rochon Sands PP\ROCHONSANDSPP06102014GB2~files','W:\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\Rochon Sands PP\ROCHONSANDSPP07102014GB~files','W:\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\Rochon Sands PP\ROCHONSANDSPP07102014GB2~files']
	for targ in targets:
		in_fld = in_fld.replace(targ, rep_value)
		return in_fld"""
	
a1 = """rep_field (!Picture!,r'\\\env.gov.ab.ca\Parks\CityWorks\Referenced\Rochon_Sands_PP')"""

a11 = """rep_field (!Picture1!,r'\\\env.gov.ab.ca\Parks\CityWorks\Referenced\Rochon_Sands_PP')"""

for fc in featureClass:
    if "Bridge" in fc:
        arcpy.CalculateField_management(fc, "Picture1", a11, "PYTHON_9.3", a2)
    elif "Speed_Bump" in fc:
        arcpy.CalculateField_management(fc, "Picture1", a11, "PYTHON_9.3", a2)
    elif "Building" in fc:
        arcpy.CalculateField_management(fc, "Picture1", a11, "PYTHON_9.3", a2)
    elif "Culvert_Line" in fc:
        arcpy.CalculateField_management(fc, "Picture1", a11, "PYTHON_9.3", a2)
    else:
        arcpy.CalculateField_management(fc, "Picture", a1, "PYTHON_9.3", a2)
            
            
for fc in featureClass:
    arcpy.CalculateField_management(fc, "Unique_ID", "!OBJECTID!", "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "PASITES_ID", '"1046"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "Park_Type", '"PP"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "Region_Name", '"Central"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "District_Name", '"Wainwright"', "PYTHON_9.3", "")
    arcpy.CalculateField_management(fc, "Park_Name", '"Rochon Sands PP"', "PYTHON_9.3", "")
    



