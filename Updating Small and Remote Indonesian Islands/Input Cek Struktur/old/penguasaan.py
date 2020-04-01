print "Memulai Tool"
import arcpy
import csv
import sys
import os

# 1. Mendapatkan folder relatif berdasarkan lokasi script.
script_folder = sys.path[0]
tools_folder = os.path.dirname(script_folder)
#print script_folder 622678wd
#print tools_folder
#print arcpy.env.workspace

#exit()
with open('Penguasaan_Jateng.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[1]
                prov = line[6]
                gdb = prov +str('.gdb')
                output = str('psn_')+ line[13]
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
                    #try:
                     #   arcpy.CalculateField_management(output, "psnObjName", "[penguasaan]", "VB", "")
                    #except arcpy.ExecuteError, error:
                     #   continue
                    # psnID	
                    arcpy.AddField_management(output, "psnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "psnID", "[KODE]", "VB", "")
                    #arcpy.CalculateField_management(output, "psnObjName", "penguasaan", "VB", "'Klasifikasi Penguasaan @ gMAN 2014\\n\\nkode = [psnID]\\n'ISI KODE DENGAN NAMA KOLOM KODE PENGUASAAN\\n\\nif kode = 31 then\\npenguasaan = \"Perorangan\"\\n\\nelseif kode = 32 then\\npenguasaan = \"Kelompok Masyarakat\"\\n\\nelseif kode = 33 then\\npenguasaan = \"Badan Hukum\"\\n\\nelseif kode = 34 then\\npenguasaan = \"Instansi Pemerintah\"\\n\\nelseif kode = 35 then\\npenguasaan  = \"Lainnya\"\\n\\nelseif kode = 980 then \\npenguasaan =\"Jalan\"\\n\\nelseif kode = 990 then \\npenguasaan =\"Sungai\"\\n\\nelseif kode = 152 then \\npenguasaan =\"Danau/Telaga/Situ\"\\n\\n\\nelse\\npenguasaan =\"  \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n") 
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        continue
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
                    arcpy.CalculateField_management(output, "wacName", kec, "VB", "")
                    # psnID
                    arcpy.AddField_management(output, "psnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # psnObjName	
                    arcpy.AddField_management(output, "psnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "psnObjName", "[Penguasaan]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnObjName", "[penguasaan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "psnObjName", "[PENGUASAAN]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "psnObjName", "[JenisKuasa]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "psnObjName", "[QNAME]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                            arcpy.CalculateField_management(output, "psnObjName", "[Jns_Kuasa]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            continue
                    try:
                        arcpy.CalculateField_management(output, "psnID", "[KDPENG]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "psnID", "[KDPeng]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "psnID", "[Kode]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "psnID", "[KD_PENGUAS]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "psnID", "[Kodekuasa]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                            arcpy.CalculateField_management(output, "psnID", "[kodekuasa]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            try:
                                                arcpy.CalculateField_management(output, "psnID", "[Kode_Kuasa]", "VB", "")
                                            except arcpy.ExecuteError, error:
                                                try:
                                                    arcpy.CalculateField_management(output, "psnID", "[Kode_kuasa]", "VB", "")
                                                except arcpy.ExecuteError, error:
                                                    try:
                                                        arcpy.CalculateField_management(output, "psnID", "[PngusanCod]", "VB", "")
                                                    except arcpy.ExecuteError, error:
                                                        try:
                                                            arcpy.CalculateField_management(output, "psnID", "[Pngasan_Co]", "VB", "")
                                                        except arcpy.ExecuteError, error:
                                                            try:
                                                                arcpy.CalculateField_management(output, "psnID", "[Pngasan_Co]", "VB", "")
                                                            except arcpy.ExecuteError, error:
                                                                try:
                                                                    arcpy.CalculateField_management(output, "psnID", "[kod_kuasa]", "VB", "")
                                                                except arcpy.ExecuteError, error:
                                                                    try:
                                                                        arcpy.CalculateField_management(output, "psnID", "Kode", "VB", "'Klasifikasi Kode Penguasaan @ gMAN 2014\\n\\npenguasaan = [psnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE penguasaan\\n\\nif penguasaan = \"Perorangan\" then \\nKode = 31\\nelseif penguasaan = \"Kelompok Masyarakat\" then \\nKode = 32\\nelseif penguasaan = \"Badan Hukum\" then \\nKode = 33\\nelseif penguasaan = \"Instansi Pemerintah\" then \\nKode = 34\\nelseif penguasaan = \"Lainnya\" then \\nKode = 35\\nelseif penguasaan = \"Tanah Negara\" then \\nKode = 35\\nelseif penguasaan = \"Waduk\" then \\nKode = 151\\nelseif penguasaan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif penguasaan = \"Jalan\" then \\nKode = 980\\nelseif penguasaan = \"Jalan Tol\" then \\nKode = 981\\nelseif penguasaan = \"Sungai\" then \\nKode = 990\\nelseif penguasaan = \"Sungai Besar\" then \\nKode = 991\\nelseif penguasaan = \"Laut Dalam\" then \\nKode = 79\\nelseif penguasaan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                                                                    except arcpy.ExecuteError, error:
                                                                        continue
                    # psnRemarks
                    print "creating remarks"
                    arcpy.AddField_management(output, "psnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    #try:
                     #   arcpy.CalculateField_management(output, "psnRemarks", "[Keterangan]", "VB", "")
                    #except arcpy.ExecuteError, error:
                     #   try:
                      #      arcpy.CalculateField_management(output, "psnRemarks", "[keterangan]", "VB", "")
                       # except arcpy.ExecuteError, error:
                        #    continue
                    # area  
                    try:
                        print "try create area"
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                        #try:
                         #   print "try fill area"
                          #  arcpy.CalculateField_management(output, "area", "[luas_ha]", "VB", "")
                        #except arcpy.ExecuteError, error:
                         #   try:
                          #      print "try fill area"
                           #     arcpy.CalculateField_management(output, "area", "[Luas_Ha]", "VB", "")
                            #except arcpy.ExecuteError, error:
                             #   print "give up area"
                              #  continue
                    except arcpy.ExecuteError, error:
                        print "there Is already area field"
                        continue    
                    
                    #Process : Delete Field
                    print 'Deleting Originals Fields for Feature ' + output
                    try:
                        arcpy.DeleteField_management(output, "Penguasaan")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "KDPENG")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "KDPeng")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "KD_PENGUAS")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Kode")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Pengus")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Hectares")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Keterangan")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "keterangan")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "QNAME_1")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "COUNT")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Luas_Ha")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Luas_ha")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "luas_ha")
                    except arcpy.ExecuteError, error:
                        continue
                    
                    
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
