import arcpy
from arcpy import da
import os
#Change workspace variable to folder containing all the gdbs you want to extract
workspace = r"C:\Users\vincent.law\Documents\CW2017GDB\goodcentral\test - Copy"
pictureLocation = r"\\env.gov.ab.ca\Parks\CityWorks\Referenced" + "\\"
featureClass = []
arcpy.env.overwriteOutput = True
walk = arcpy.da.Walk(workspace, datatype=['FeatureClass'], type="Any")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        table.append(os.path.join(dirpath, filename))

#Remove irrelevant featureclasses
        featureClass = [fc for fc in table if "Boundary" not in fc]
        featureClass1 = [fc for fc in featureClass if "Trails" not in fc]
        featureClass2 = [fc for fc in featureClass1 if "Anno" not in fc]

#Add "Picture" field to featureclasses with "Picture1" field
for fc in featureClass2:
    if "Building" in fc:
        arcpy.AddField_management (fc,"Picture", "TEXT", "", "", "", "", "NULLABLE")
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[1] = row[0]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
    elif "Culvert_Line" in fc:
        arcpy.AddField_management (fc,"Picture", "TEXT", "", "", "", "", "NULLABLE")
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[1] = row[0]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
    elif "Speed_Bump" in fc:
        arcpy.AddField_management (fc,"Picture", "TEXT", "", "", "", "", "NULLABLE")
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[1] = row[0]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
    elif "Bridge" in fc:
        arcpy.AddField_management (fc,"Picture", "TEXT", "", "", "", "", "NULLABLE")
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[1] = row[0]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)

    tableAttach = fc + "__ATTACH"
    fcName = "'" + str(fc[fc.find(".gdb\\"):].replace(".gdb\\","")) + "'"
    arcpy.AddField_management (tableAttach, "ATTACHMENTID1", "TEXT", "", "", "", "", "NULLABLE")
    arcpy.AddField_management(tableAttach, "FCname", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED")
    arcpy.CalculateField_management(tableAttach, "FCname", fcName, "PYTHON_9.3", "")

    r = fc[:fc.find(".gdb\\")] + ".gdb"
    edit = arcpy.da.Editor(r)
    edit.startEditing(False, True)
    edit.startOperation()
    with arcpy.da.UpdateCursor(tableAttach, ['ATTACHMENTID','ATTACHMENTID1']) as cursor:
        for row in cursor:
            row[1] = row[0]
            cursor.updateRow(row)
            del row
    edit.stopOperation()
    edit.stopEditing(True)
    arcpy.JoinField_management(fc, "GlobalID", tableAttach, "REL_GLOBALID")




#parkName uses the filename of the GDB. It removes 'Verified' in the front and '.gdb' at the end. This mean you will have to double check if the name of folder match up with the name in REFERENCE picture folder
    parkName = fc.replace(workspace,"").replace("Verified_","").replace(".gdb\Loading_Ramp","").replace(".gdb\Recreation_Point","").replace(".gdb\Sign_Advisory_and_Wildlife","").replace(".gdb\Sign_AreaEntry_and_SmallGuide","").replace(".gdb\Sign_CampsiteMarker_and_RAP","").replace(".gdb\Sign_ParkID_and_Boundary","").replace(".gdb\Sign_Parking_and_Traffic","").replace(".gdb\Sign_Symbol_Trail_WalkUpMultPnl","").replace(".gdb\Site_Features","").replace(".gdb\Stairs","").replace(".gdb\Waste_Disposal","").replace(".gdb\Water_Facility","").replace(".gdb\Water_Point","").replace(".gdb\Culvert_Line","").replace(".gdb\Erosion_Slope_Control","").replace(".gdb\Fence_and_Railing","").replace(".gdb\Road","").replace(".gdb\Speed_Bump","").replace(".gdb\Trails","").replace(".gdb\Bench_and_Table","").replace(".gdb\Bridge","").replace(".gdb\Communication","").replace(".gdb\Dump_Station","").replace(".gdb\Firepit_and_BBQ","").replace(".gdb\Fuel_Supply","").replace(".gdb\Wastewater_Point","").replace(".gdb\Campsite","").replace(".gdb\Parking_Area","").replace(".gdb\Recreation_Area","").replace(".gdb\Building","").replace(".gdb\Boundary","").replace(".gdb\Platform","").replace(".gdb\Wastewater_Area","").replace(".gdb\Electrical_Point","").replace(".gdb\Gates","").replace("\\","")


#Extract picture attachments from tableAttach
    r = fc[:fc.find(".gdb\\")] + ".gdb"
    edit = arcpy.da.Editor(r)
    edit.startEditing(False, True)
    edit.startOperation()
    with da.SearchCursor(tableAttach, ['DATA', 'ATT_NAME', 'ATTACHMENTID']) as cursor:
        for item in cursor:
            if "Bench_and_Table" in fc:
                attachment = item[0]
                filenum = "Bench_and_Table" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Bridge" in fc:
                attachment = item[0]
                filenum = "Bridge" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Communication" in fc:
                attachment = item[0]
                filenum = "Communication" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Dump_Station" in fc:
                attachment = item[0]
                filenum = "Dump_Station" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Electrical_Point" in fc:
                attachment = item[0]
                filenum = "Electrical_Point" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Firepit_and_BBQ" in fc:
                attachment = item[0]
                filenum = "Firepit_and_BBQ" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Fuel_Supply" in fc:
                attachment = item[0]
                filenum = "Fuel_Supply" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Gates" in fc:
                attachment = item[0]
                filenum = "Gates" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Loading_Ramp" in fc:
                attachment = item[0]
                filenum = "Loading_Ramp" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Recreation_Point" in fc:
                attachment = item[0]
                filenum = "Recreation_Point" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Sign_Advisory_and_Wildlife" in fc:
                attachment = item[0]
                filenum = "Sign_Advisory_and_Wildlife" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + park + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Sign_AreaEntry_and_SmallGuide" in fc:
                attachment = item[0]
                filenum = "Sign_AreaEntry_and_SmallGuide" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Sign_CampsiteMarker_and_RAP" in fc:
                attachment = item[0]
                filenum = "Sign_CampsiteMarker_and_RAP" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Sign_ParkID_and_Boundary" in fc:
                attachment = item[0]
                filenum = "Sign_ParkID_and_Boundary" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Sign_Parking_and_Traffic" in fc:
                attachment = item[0]
                filenum = "Sign_Parking_and_Traffic" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Sign_Symbol_Trail_WalkUpMultPnl" in fc:
                attachment = item[0]
                filenum = "Sign_Symbol_Trail_WalkUpMultPnl" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Site_Features" in fc:
                attachment = item[0]
                filenum = "Site_Features" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Stairs" in fc:
                attachment = item[0]
                filenum = "Stairs" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Waste_Disposal" in fc:
                attachment = item[0]
                filenum = "Waste_Disposal" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Wastewater_Point" in fc:
                attachment = item[0]
                filenum = "Wastewater_Point" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Water_Facility" in fc:
                attachment = item[0]
                filenum = "Water_Facility" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Water_Point" in fc:
                attachment = item[0]
                filenum = "Water_Point" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row

            elif "Culvert_Line" in fc:
                attachment = item[0]
                filenum = "Culvert_Line" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Erosion_Slope_Control" in fc:
                attachment = item[0]
                filenum = "Erosion_Slope_Control" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Fence_and_Railing" in fc:
                attachment = item[0]
                filenum = "Fence_and_Railing" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Road" in fc:
                attachment = item[0]
                filenum = "Road" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Speed_Bump" in fc:
                attachment = item[0]
                filenum = "Speed_Bump" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Campsite" in fc:
                attachment = item[0]
                filenum = "Campsite" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Building" in fc:
                attachment = item[0]
                filenum = "Building" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Parking_Area" in fc:
                attachment = item[0]
                filenum = "Parking_Area" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Platform" in fc:
                attachment = item[0]
                filenum = "Platform" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row

            elif "Recreation_Area" in fc:
                attachment = item[0]
                filenum = "Recreation_Area" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row


            elif "Wastewater_Area" in fc:
                attachment = item[0]
                filenum = "Wastewater_Area" + "_" + "ATT" + str(item[2]) + "_"
                filename = filenum + str(item[1])
                open(pictureLocation + parkName + os.sep + filename, 'wb').write(attachment.tobytes())
                del item
                del filenum
                del filename
                del attachment

                with arcpy.da.UpdateCursor(fc, ['ATT_NAME', 'ATTACHMENTID1','FCname','Picture'],"REL_GLOBALID IS NOT NULL") as cursor:
                    for row in cursor:
                        row[3] = pictureLocation + parkName + "\\" +  row[2] + "_ATT" + row[1] + "_" + row[0]
                        cursor.updateRow(row)
                        del row
        edit.stopOperation()
        edit.stopEditing(True)

for fc in featureClass2:
    arcpy.DeleteField_management(fc, "FCname")
    arcpy.DeleteField_management(fc, "REL_GLOBALID")
    arcpy.DeleteField_management(fc, "ATT_NAME")
    arcpy.DeleteField_management(fc, "CONTENT_TYPE")
    arcpy.DeleteField_management(fc, "DATA_SIZE")
    arcpy.DeleteField_management(fc, "ATTACHMENTID1")

for fc in featureClass2:
    if "Building" in fc:
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[0] = row[1]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
        arcpy.DeleteField_management(fc, "Picture")
    elif "Culvert_Line" in fc:
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[0] = row[1]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
        arcpy.DeleteField_management(fc, "Picture")
    elif "Speed_Bump" in fc:
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[0] = row[1]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
        arcpy.DeleteField_management(fc, "Picture")
    elif "Bridge" in fc:
        r = fc[:fc.find(".gdb\\")] + ".gdb"
        edit = arcpy.da.Editor(r)
        edit.startEditing(False, True)
        edit.startOperation()
        with arcpy.da.UpdateCursor(fc, ['Picture1','Picture']) as cursor:
            for row in cursor:
                row[0] = row[1]
                cursor.updateRow(row)
                del row
        edit.stopOperation()
        edit.stopEditing(True)
        arcpy.DeleteField_management(fc, "Picture")
