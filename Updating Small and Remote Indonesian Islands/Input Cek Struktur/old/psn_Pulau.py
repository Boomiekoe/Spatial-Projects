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
with open('Penguasaan_Pulau.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0 
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[1]
                prov = line[6]
                gdb = prov +str('.gdb')
                output = str('psnPulau_')+ line[13]
                jens = line[3]
                psn = 'Penguasaan'
                # Field 
                thn = line[5]
                kab = str('"')+line[7]+str('"')
                kec = str('"')+line[8]+str('"')
                pro = str('"')+line[6]+str('"')
                types = str('"')+line[4]+str('"')
                #print
                print shp
                print output
                #Change workspace
                arcpy.env.workspace = str(os.path.join(tools_folder,gdb,psn))
                arcpy.env.overwriteOutput = True
                print arcpy.env.workspace
                # Process: Project (moving)
                print 'Moving Feature ' + output + ' to Database'
            
                #project 
                arcpy.Project_management(shp, output, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "", "", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
                #Process : Adding Field
                print 'Create Format Fields for Feature ' + output
                print jens
                if jens == "1":
                    print "type one"
                    # objID
                    arcpy.AddField_management(output, "objID", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # objType
                    arcpy.AddField_management(output, "objType", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "objType", types, "VB", "")
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
                               
                    # psnObjName
                    arcpy.AddField_management(output, "psnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "psnObjName", "[Pemilikan]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnObjName", "[pemilikan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            continue
                    # psnID	
                    arcpy.AddField_management(output, "psnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "psnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [psnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [psnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    #arcpy.CalculateField_management(output, "psnObjName", "pemilikan", "VB", "'Klasifikasi pemilikan @ gMAN2014\\n\\nkode = [psnID] \\n'ISI KODE =   DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif kode = 1 then \\npemilikan =\"Terdaftar\"\\nelseif kode = 2 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 3 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 980 then \\npemilikan =\"Jalan\"\\nelseif kode = 990 then \\npemilikan =\"Sungai\"\\nelseif kode = 152 then \\npemilikan =\"Danau/Telaga/Situ\"\\n\\nelse\\npemilikan =\"    \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    #arcpy.CalculateField_management(output, "area", "[AREA]", "VB", "")
                    # psnRemarks
                    arcpy.AddField_management(output, "psnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "psnRemarks", "[RDTK]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnRemarks", "[KETERANGAN]", "VB", "")
                        except arcpy.ExecuteError, error:
                            continue
                    #Process : Delete Field
                    
#2
                elif jens == "2":
                    print "type two"
                    # objID
                    arcpy.AddField_management(output, "objID", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # objType
                    arcpy.AddField_management(output, "objType", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "objType", types, "VB", "")
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
                    #arcpy.CalculateField_management(output, "wacName", kec, "VB", "")
                    # wadName	
                    arcpy.AddField_management(output, "wadName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "wadName", kec, "VB", "")
                   # psnID
                    arcpy.AddField_management(output, "psnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # psnObjName	
                    arcpy.AddField_management(output, "psnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "psnObjName", "[PENGUASAAN]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnObjName", "[Penguasaan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "psnObjName", "[penguasaan]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "psnObjName", "[JNS_PENG]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "psnObjName", "[JNS_PGS]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                            arcpy.CalculateField_management(output, "psnObjName", "[Jenis_Peng]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            try:
                                                arcpy.CalculateField_management(output, "psnObjName", "[J_PGSN2]", "VB", "")
                                            except arcpy.ExecuteError, error:
                                                try:
                                                    arcpy.CalculateField_management(output, "psnObjName", "[TANAH]", "VB", "")
                                                except arcpy.ExecuteError, error:
                                                    try:
                                                        arcpy.CalculateField_management(output, "psnObjName", "[JENIS_PENG]", "VB", "")
                                                    except arcpy.ExecuteError, error:
                                                        try:
                                                            arcpy.CalculateField_management(output, "psnObjName", "[Jenis]", "VB", "")
                                                        except arcpy.ExecuteError, error:
                                                            print "no psnOBjName"
                    try:
                        arcpy.CalculateField_management(output, "psnID", "[Kode]", "VB", "")
                    except arcpy.ExecuteError, error:
                        print "1"
                        try:
                            arcpy.CalculateField_management(output, "psnID", "[kode]", "VB", "")
                        except arcpy.ExecuteError, error:
                            print "2"
                            try:
                                arcpy.CalculateField_management(output, "psnID", "[J_PGSN]", "VB", "")
                            except arcpy.ExecuteError, error:
                                print "3"
                                try:
                                    arcpy.CalculateField_management(output, "psnID", "[Jns_Kuasa]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    print "3"
                                    try:
                                        arcpy.CalculateField_management(output, "psnID", "[kuasa_2011]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        print "4"
                                        try:
                                            arcpy.CalculateField_management(output, "psnID", "[kode_2011]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            print "5"
                                            try:
                                                arcpy.CalculateField_management(output, "psnID", "[OCODE]", "VB", "")
                                            except arcpy.ExecuteError, error:
                                                print "6"
                                                try:
                                                    print ""#arcpy.CalculateField_management(output, "psnID", "[Jns_Kuasa]", "VB", "")
                                                except arcpy.ExecuteError, error:
                                                    print "7"
                                                    try:
                                                        print ""#arcpy.CalculateField_management(output, "psnID", "[STATUS_TNH]", "VB", "")
                                                    except arcpy.ExecuteError, error:
                                                        print "8"
                                                        try:
                                                           print "" #arcpy.CalculateField_management(output, "psnID", "[ST_TNH]", "VB", "")
                                                        except arcpy.ExecuteError, error:
                                                            print "9"
                                                            try:
                                                                print ""#arcpy.CalculateField_management(output, "psnID", "[TANAH]", "VB", "")
                                                            except arcpy.ExecuteError, error:
                                                                print "10"
                                                                try:
                                                                    arcpy.CalculateField_management(output, "psnID", "Kode", "VB", "'Klasifikasi Kode Penguasaan @ gMAN 2014\\n\\npenguasaan = [psnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif penguasaan = \"Perorangan\" then \\nKode = 31\\nelseif penguasaan = \"Kelompok Masyarakat\" then \\nKode = 32\\nelseif penguasaan = \"Badan Hukum\" then \\nKode = 33\\nelseif penguasaan = \"Instansi Pemerintah\" then \\nKode = 34\\nelseif penguasaan = \"Lainnya\" then \\nKode = 35\\nelseif penguasaan = \"Tanah Negara\" then \\nKode = 35\\nelseif penguasaan = \"Waduk\" then \\nKode = 151\\nelseif penguasaan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif penguasaan = \"Jalan\" then \\nKode = 980\\nelseif penguasaan = \"Jalan Tol\" then \\nKode = 981\\nelseif penguasaan = \"Sungai\" then \\nKode = 990\\nelseif penguasaan = \"Sungai Besar\" then \\nKode = 991\\nelseif penguasaan = \"Laut Dalam\" then \\nKode = 79\\nelseif penguasaan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                                                                except arcpy.ExecuteError, error:
                                                                    print "11 No psnID"
                    try:
                        arcpy.CalculateField_management(output, "psnObjName", "[PENGUASAAN]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnObjName", "[Penguasaan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "psnObjName", "[penguasaan]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "psnObjName", "[STATUS]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "psnObjName", "[Status]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                           arcpy.CalculateField_management(output, "psnObjName", "penguasaan", "VB", "'Klasifikasi Penguasaan @ gMAN 2014\\n\\nkode = [psnID]\\n'ISI KODE DENGAN NAMA KOLOM KODE PENGUASAAN\\n\\nif kode = 31 then\\npenguasaan = \"Perorangan\"\\n\\nelseif kode = 32 then\\npenguasaan = \"Kelompok Masyarakat\"\\n\\nelseif kode = 33 then\\npenguasaan = \"Badan Hukum\"\\n\\nelseif kode = 34 then\\npenguasaan = \"Instansi Pemerintah\"\\n\\nelseif kode = 35 then\\npenguasaan  = \"Lainnya\"\\n\\nelseif kode = 980 then \\npenguasaan =\"Jalan\"\\n\\nelseif kode = 990 then \\npenguasaan =\"Sungai\"\\n\\nelseif kode = 152 then \\npenguasaan =\"Danau/Telaga/Situ\"\\n\\n\\nelse\\npenguasaan =\"  \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                                           print "objname clear"
                                        except arcpy.ExecuteError, error:
                                            print ""
                        
                    #arcpy.CalculateField_management(output, "psnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [psnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [psnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        print ""
                    
                    # psnRemarks
                    arcpy.AddField_management(output, "psnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "psnRemarks", "[KETERANGAN]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnRemarks", "[Keterangan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "psnRemarks", "[keterangan]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "psnRemarks", "[KET]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "psnRemarks", "[Ket]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                            arcpy.CalculateField_management(output, "psnRemarks", "[ket]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            continue
                    #Process : Delete Field
                    #print 'Deleting Originals Fields for Feature ' + output
                    #try:
                     #   arcpy.DeleteField_management(output, "Nama_Layer")
                    #except arcpy.ExecuteError, error:
                     #   continue
                    #try:
                      #  arcpy.DeleteField_management(output, "No_Idfier")
                    #except arcpy.ExecuteError, error:
                       # continue
                    #arcpy.DeleteField_management(output, "Pemilikan")
                    #try:
                     #   arcpy.DeleteField_management(output, "Tipe")
                    #except arcpy.ExecuteError, error:
                     #   continue
                    #try:
                     #   arcpy.DeleteField_management(output, "Kecamatan")
                    #except arcpy.ExecuteError, error:
                     #   continue
                    #try:
                     #   arcpy.DeleteField_management(output, "J_Milik")
                    #except arcpy.ExecuteError, error:
                     #   continue
                    #arcpy.DeleteField_management(output, "Kode")
                    #arcpy.DeleteField_management(output, "PERIMETER")
                    #arcpy.DeleteField_management(output, "HECTARES")
                    
                elif jens == "5":
                    print "type five"
                    # objID
                    arcpy.AddField_management(output, "objID", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
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
                    # psnID
                    arcpy.AddField_management(output, "psnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "psnID", "[JENIS]", "VB", "")
                    # psnObjName	
                    arcpy.AddField_management(output, "psnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "psnObjName", "pemilikan", "VB", "'Klasifikasi pemilikan @ gMAN2014\\n\\nkode = [psnID] \\n'ISI KODE =   DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif kode = 1 then \\npemilikan =\"Terdaftar\"\\nelseif kode = 2 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 3 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 980 then \\npemilikan =\"Jalan\"\\nelseif kode = 990 then \\npemilikan =\"Sungai\"\\nelseif kode = 152 then \\npemilikan =\"Danau/Telaga/Situ\"\\n\\nelse\\npemilikan =\"    \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "area", "[LUAS]", "VB", "")
                    # psnRemarks
                    arcpy.AddField_management(output, "psnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "psnRemarks", "[KETERANGAN]", "VB", "")
                    #Process : Delete Field
                    
                else:
                    print "no type found"
                    continue
                print "repeat"    
                
            except arcpy.ExecuteError, error:
                print "Something went wrong handling " + ". Here's a traceback:"
                print output
                continue
                

            
            
        else:
            
            pass
            
        lompati = lompati +1
