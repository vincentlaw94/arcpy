import arcpy

arcpy.env.workspace = r"M:\Parks\HQ\OPERATIONS\CPI\Asset_Management\GNSS Projects\Parks Inventory\MergedParks\_MasterCopy_Restored\SDE Connection\ParksCityWorks.GDB@GENESIS-SDE-DEV.sde"

REFERENCED = r"\\env.gov.ab.ca\Parks\CityWorks\Referenced"

dataSet = arcpy.ListDatasets ('','Feature')
featureClass = []
for ds in dataSet:
    for fc in arcpy.ListFeatureClasses('','',ds):
        featureClass.append(fc)

featureClass1 = [fc for fc in featureClass if "Building" not in fc]
featureClass2 = [fc for fc in featureClass1 if "Culvert_Line" not in fc]
featureClass3 = [fc for fc in featureClass2 if "Speed_Bump" not in fc]
featureClass4 = [fc for fc in featureClass3 if "Bridge" not in fc]
featureClass5 = [fc for fc in featureClass4 if "Boundary" not in fc]
featureClass6 = [fc for fc in featureClass5 if "Trails" not in fc]


edit = arcpy.da.Editor(arcpy.env.workspace)
edit.startEditing(False, True)
edit.startOperation()

for fc in featureClass:
    if "Building" in fc:
        with arcpy.da.UpdateCursor(fc, ['Picture1','Park_Name']) as cursor:
            for row in cursor:
                try:
                    a = str(row[0][row[0].find("IMG"):])
                    parkName = str(row[1].replace(" ","_"))
                    row[0] = REFERENCED + "\\" + parkName + "\\" + a
                    cursor.updateRow(row)
                except:
                    row[0] = " "
    elif "Culvert_Line" in fc:
        with arcpy.da.UpdateCursor(fc, ['Picture1','Park_Name']) as cursor:
            for row in cursor:
                try:
                    a = str(row[0][row[0].find("IMG"):])
                    parkName = str(row[1].replace(" ","_"))
                    row[0] = REFERENCED + "\\" + parkName + "\\" + a
                    cursor.updateRow(row)
                except:
                    row[0] = " "
    elif "Speed_Bump" in fc:
        with arcpy.da.UpdateCursor(fc, ['Picture1','Park_Name']) as cursor:
            for row in cursor:
                try:
                    a = str(row[0][row[0].find("IMG"):])
                    parkName = str(row[1].replace(" ","_"))
                    row[0] = REFERENCED + "\\" + parkName + "\\" + a
                    cursor.updateRow(row)
                except:
                    row[0] = " "
    elif "Bridge" in fc:
        with arcpy.da.UpdateCursor(fc, ['Picture1','Park_Name']) as cursor:
            for row in cursor:
                try:
                    a = str(row[0][row[0].find("IMG"):])
                    parkName = str(row[1].replace(" ","_"))
                    row[0] = REFERENCED + "\\" + parkName + "\\" + a
                    cursor.updateRow(row)
                except:
                    row[0] = " "


for fc in featureClass6:
    with arcpy.da.UpdateCursor(fc, ['Picture','Park_Name']) as cursor:
            for row in cursor:
                try:
                    a = str(row[0][row[0].find("IMG"):])
                    parkName = str(row[1].replace(" ","_"))
                    row[0] = REFERENCED + "\\" + parkName + "\\" + a
                    cursor.updateRow(row)
                except:
                    row[0] = " "
edit.stopOperation()
edit.stopEditing(True)
