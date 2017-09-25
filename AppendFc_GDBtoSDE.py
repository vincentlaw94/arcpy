import arcpy, os

inputGDB = r"W:\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\MergedParks\William A. Switzer PP\CW_William_A_Switzer_PP\CW_William_A_Switzer_PP\CW_William_A_Switzer_PP.gdb"
SDE = r"\\goa\desktop\T_Z\vincent.law\Desktop\New folder\ParksCityworksEdit.GDB@genesis-sde.sde\ParksCityworksEdit.GDB.Central" 
arcpy.env.workspace = SDE

SDEFCs = arcpy.ListFeatureClasses()
for fc in SDEFCs:
    sourceFC = str(fc)[31:]
    if arcpy.Exists(os.path.join(inputGDB, sourceFC)):
        fcPath = SDE + "\\" + fc
        arcpy.Append_management(os.path.join(inputGDB,sourceFC), fcPath, "NO_TEST")
