import arcpy

arcpy.env.workspace = r'C:\Users\vincent.law\Documents\CW_Castle_PP.gdb'
outputfolder = 'C:\\Users\\vincent.law\\Documents\\Castle\\'
fc = arcpy.ListFeatureClasses()


for fc1 in fc:
    fcname = str(fc1)
    arcpy.TableToExcel_conversion(fc1, outputfolder + fcname + ".xls")
