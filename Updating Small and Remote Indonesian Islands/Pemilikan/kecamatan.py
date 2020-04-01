print "Memulai Tool"
import arcpy
import csv
import sys
import os

# 1. Mendapatkan folder relatif berdasarkan lokasi script.
script_folder = sys.path[0]
tools_folder = os.path.dirname(script_folder)
#print script_folder
#print tools_folder
#print arcpy.env.workspace

#exit()
with open('Pemilikan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[1]
                prov = line[6]
                gdb = prov +str('.gdb')
                output = str('pmn_')+ line[13]
                pmn = 'Pemilikan'
                # Field 
                thn = line[5]
                kab = str('"')+line[7]+str('"')
                kec = str('"')+line[8]+str('"')
                pro = str('"')+line[6]+str('"')
                #print
                print shp
                print output
                #Change workspace
                arcpy.env.workspace = str(os.path.join(tools_folder,gdb,pmn))
                arcpy.env.overwriteOutput = True
                print arcpy.env.workspace
                # Process: Project (moving)
                print 'Moving Feature ' + output + ' to Database'
            
                #project 
                arcpy.Project_management(shp, output, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "", "", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")

                # Process: Add Field
                print 'Creating Fields for Feature ' + output 
                # objID
                arcpy.AddField_management(output, "objID", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                arcpy.CalculateField_management(output, "objID", "[OBJECTID]", "VB", "")
                # objType
                arcpy.AddField_management(output, "objType", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

                # objYear
                arcpy.AddField_management(output, "objYear", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                arcpy.CalculateField_management(output, "objYear", thn, "VB", "")
            
                # wapName	
                arcpy.AddField_management(output, "wapName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                arcpy.CalculateField_management(output, "wapName", pro, "VB", "")
            
                # wakName	
                arcpy.AddField_management(output, "wakName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                arcpy.CalculateField_management(output, "wakName", kab, "VB", "")
            
                # wacName	
                arcpy.AddField_management(output, "wacName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                arcpy.CalculateField_management(output, "wacName", kec, "VB", "")
            
                # pmnID
                arcpy.AddField_management(output, "pmnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

                # pmnObjName	
                arcpy.AddField_management(output, "pmnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

                # area  
                arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        
                # pmnRemarks
                arcpy.AddField_management(output, "pmnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

                #Process : Filling Field
                print 'Filling pmnID Fields for Feature ' + output
                # Process: Calculate Field
                # pmnID
                try:
                    arcpy.CalculateField_management(output, "pmnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [PEMILIKAN] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [PEMILIKAN] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                except arcpy.ExecuteError, error:
                    try:
                        arcpy.CalculateField_management(output, "pmnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [Pemilikan] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [Pemilikan] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "pmnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [Pemilikan] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [pemilikan] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                        except arcpy.ExecuteError, error:
                            print "Failed writing pmnObjName " + ". Here's a traceback:"
                            print output
                            continue
                print 'Filling pmnObjName Fields for Feature ' + output
                # Process: Calculate Field
                # pmnObjName
                arcpy.CalculateField_management(output, "pmnObjName", "pemilikan", "VB", "'Klasifikasi pemilikan @ gMAN2014\\n\\nkode = [pmnID] \\n'ISI KODE =   DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif kode = 1 then \\npemilikan =\"Terdaftar\"\\nelseif kode = 2 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 3 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 980 then \\npemilikan =\"Jalan\"\\nelseif kode = 990 then \\npemilikan =\"Sungai\"\\nelseif kode = 152 then \\npemilikan =\"Danau/Telaga/Situ\"\\n\\nelse\\npemilikan =\"    \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                #Process : Delete Field
                print 'Deleting Originals Fields for Feature ' + output
                # pmnID
                try:
                    arcpy.DeleteField_management(output, "PEMILIKAN")
                except arcpy.ExecuteError, error:
                    try:
                        arcpy.DeleteField_management(output, "Pemilikan")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.DeleteField_management(output, "pemilikan")
                        except arcpy.ExecuteError, error:
                            print "Failed Deleting Fields " + ". Here's a traceback:"
                            print output
                            continue
                print "repeat"    
                
            except arcpy.ExecuteError, error:
                print "Something went wrong handling " + ". Here's a traceback:"
                print output
                continue
                

            
            
        else:
            
            pass
            
        lompati = lompati +1
