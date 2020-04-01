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
with open('Penggunaan_Jateng.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[1]
                prov = line[6]
                gdb = prov +str('.gdb')
                output = str('ptn_')+ line[13]
                jens = line[3]
                ptn = 'Penggunaan'
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
                arcpy.env.workspace = str(os.path.join(tools_folder,gdb,ptn))
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
                    # ptnObjName
                    arcpy.AddField_management(output, "ptnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    #try:
                     #   arcpy.CalculateField_management(output, "ptnObjName", "[penguasaan]", "VB", "")
                    #except arcpy.ExecuteError, error:
                     #   continue
                    # ptnID	
                    arcpy.AddField_management(output, "ptnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "ptnID", "[KODE]", "VB", "")
                    #arcpy.CalculateField_management(output, "ptnObjName", "penguasaan", "VB", "'Klasifikasi Penguasaan @ gMAN 2014\\n\\nkode = [ptnID]\\n'ISI KODE DENGAN NAMA KOLOM KODE PENGUASAAN\\n\\nif kode = 31 then\\npenguasaan = \"Perorangan\"\\n\\nelseif kode = 32 then\\npenguasaan = \"Kelompok Masyarakat\"\\n\\nelseif kode = 33 then\\npenguasaan = \"Badan Hukum\"\\n\\nelseif kode = 34 then\\npenguasaan = \"Instansi Pemerintah\"\\n\\nelseif kode = 35 then\\npenguasaan  = \"Lainnya\"\\n\\nelseif kode = 980 then \\npenguasaan =\"Jalan\"\\n\\nelseif kode = 990 then \\npenguasaan =\"Sungai\"\\n\\nelseif kode = 152 then \\npenguasaan =\"Danau/Telaga/Situ\"\\n\\n\\nelse\\npenguasaan =\"  \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n") 
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        continue
                    #arcpy.CalculateField_management(output, "area", "[AREA]", "VB", "")
                    # ptnRemarks
                    arcpy.AddField_management(output, "ptnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnRemarks", "[RDTK]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnRemarks", "[KETERANGAN]", "VB", "")
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
                    # ptnID
                    arcpy.AddField_management(output, "ptnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # ptnObjName	
                    arcpy.AddField_management(output, "ptnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnObjName", "[QNAME]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnObjName", "[Penggunaan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "ptnObjName", "[LANDUSE]", "VB", "")
                            except arcpy.ExecuteError, error:
                                continue
                    try:
                        arcpy.CalculateField_management(output, "ptnID", "[Kode]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnID", "[Kode_G]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "ptnID", "[KODE]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Penggunaan @ gMAN 2014\\n\\npenggunaan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PENGGUNAAN\\n\\nif penggunaan = \"Perkampungan Jarang\" then \\nKode = 101\\nelseif penggunaan = \"Perkampungan Padat\" then \\nKode = 102\\nelseif penggunaan = \"Perumahan Jarang\" then \\nKode = 103\\nelseif penggunaan = \"Perumahan Padat\" then \\nKode = 104\\nelseif penggunaan = \"Emplasemen Sementara\" then \\nKode = 105\\nelseif penggunaan = \"Emplasemen Tetap\" then \\nKode = 106\\nelseif penggunaan = \"Komplek Olah Raga\" then \\nKode = 107\\nelseif penggunaan = \"Lapangan Golf\" then \\nKode = 108\\nelseif penggunaan = \"Taman\" then \\nKode = 109\\nelseif penggunaan = \"Pemakaman Umum\" then \\nKode = 110\\nelseif penggunaan = \"Pemakaman Khusus\" then \\nKode = 112\\nelseif penggunaan = \"Industri Aneka Pangan\" then \\nKode = 113\\nelseif penggunaan = \"Industri Aneka Sandang\" then \\nKode = 114\\nelseif penggunaan = \"Industri Aneka Kimia\" then \\nKode = 115\\nelseif penggunaan = \"Industri Aneka Bahan Bangunan dan Umum\" then \\nKode = 116\\nelseif penggunaan = \"Taman Makam Pahlawan\" then \\nKode = 111\\nelseif penggunaan = \"Industri Logam Dasar\" then \\nKode = 117\\nelseif penggunaan = \"Industri Kimia Dasar\" then \\nKode = 118\\nelseif penggunaan = \"Industri Kecil\" then \\nKode = 119\\nelseif penggunaan = \"Pertambangan Terbuka\" then \\nKode = 120\\nelseif penggunaan = \"Pertambangan Tertutup\" then \\nKode = 121\\nelseif penggunaan = \"Sawah Irigasi 2x Padi/Tahun\" then \\nKode = 122\\nelseif penggunaan = \"Sawah Irigasi 2x Padi/Tahun + Palawija\" then \\nKode = 123\\nelseif penggunaan = \"Sawah Irigasi Lebih Dari 2x Padi/Tahun\" then \\nKode = 124\\nelseif penggunaan = \"Sawah Irigasi 1x Padi/Tahun\" then \\nKode = 125\\nelseif penggunaan = \"Sawah Irigasi 1x Padi/Tahun + Palawija\" then \\nKode = 126\\nelseif penggunaan = \"Sawah Tadah Hujan\" then \\nKode = 127\\nelseif penggunaan = \"Sawah Pasang Surut 2x Padi/Tahun\" then \\nKode = 128\\nelseif penggunaan = \"Sawah Pasang Surut 2x Padi/Tahun + Palawija\" then \\nKode = 129\\nelseif penggunaan = \"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\" then \\nKode = 130\\nelseif penggunaan = \"Sawah Pasang Surut 1x Padi/Tahun\" then \\nKode = 131\\nelseif penggunaan = \"Sawah Pasang Surut 1x Padi/Tahun + Palawija\" then \\nKode = 132\\nelseif penggunaan = \"Tegalan/Ladang\" then \\nKode = 133\\nelseif penggunaan = \"Tanaman Sayuran\" then \\nKode = 134\\nelseif penggunaan = \"Tanaman Bunga\" then \\nKode = 135\\nelseif penggunaan = \"Kebun Campuran\" then \\nKode = 136\\nelseif penggunaan = \"Kebun Sejenis\" then \\nKode = 137\\nelseif penggunaan = \"Perkebunan Besar\" then \\nKode = 138\\nelseif penggunaan = \"Perkebunan Rakyat\" then \\nKode = 139\\nelseif penggunaan = \"Padang Rumput\" then \\nKode = 140\\nelseif penggunaan = \"Sabana\" then \\nKode = 141\\nelseif penggunaan = \"Alang-Alang\" then \\nKode = 142\\nelseif penggunaan = \"Semak Belukar\" then \\nKode = 143\\nelseif penggunaan = \"Hutan Lebat\" then \\nKode = 144\\nelseif penggunaan = \"Hutan Belukar\" then \\nKode = 145\\nelseif penggunaan = \"Hutan Sejenis Alami\" then \\nKode = 146\\nelseif penggunaan = \"Hutan Sejenis Buatan\" then \\nKode = 147\\nelseif penggunaan = \"Kolam Air Tawar/Empang\" then \\nKode = 148\\nelseif penggunaan = \"Tambak\" then \\nKode = 149\\nelseif penggunaan = \"Penggaraman\" then \\nKode = 150\\nelseif penggunaan = \"Waduk\" then \\nKode = 151\\nelseif penggunaan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif penggunaan = \"Rawa\" then \\nKode = 153\\nelseif penggunaan = \"Tanah Rusak\" then \\nKode = 154\\nelseif penggunaan = \"Tanah Tandus\" then \\nKode = 155\\nelseif penggunaan = \"Tanah Terbuka Sementara\" then \\nKode = 156\\nelseif penggunaan = \"Tanah Terbuka\" then \\nKode = 157\\nelseif penggunaan = \"Terminal\" then \\nKode = 158\\nelseif penggunaan = \"Padang Pasir\" then \\nKode = 159\\nelseif penggunaan = \"Dermaga Apung\" then \\nKode = 160\\nelseif penggunaan = \"Rumah di atas air\" then \\nKode = 161\\nelseif penggunaan = \"Mangrove\" then \\nKode = 162\\nelseif penggunaan = \"Gumuk Pasir\" then \\nKode = 163\\nelseif penggunaan = \"Gosong\" then \\nKode = 164\\nelseif penggunaan = \"Terumbu Karang\" then \\nKode = 165\\nelseif penggunaan = \"Pelabuhan Laut\" then \\nKode = 166\\nelseif penggunaan = \"Lainnya\" then \\nKode = 167\\nelseif penggunaan = \"Penginapan\" then \\nKode = 168\\nelseif penggunaan = \"Rumah Makan\" then \\nKode = 169\\nelseif penggunaan = \"SPBU\" then \\nKode = 170\\nelseif penggunaan = \"Perkantoran\" then \\nKode = 171\\nelseif penggunaan = \"Fasilitas Pendidikan\" then \\nKode = 172\\nelseif penggunaan = \"Fasilitas Kesehatan\" then \\nKode = 173\\nelseif penggunaan = \"Fasilitas Peribadatan\" then \\nKode = 174\\nelseif penggunaan = \"Keramba\" then \\nKode = 175\\nelseif penggunaan = \"Pertokoan\" then \\nKode = 176\\nelseif penggunaan = \"Pasar\" then \\nKode = 177\\nelseif penggunaan = \"Dam\" then \\nKode = 178\\nelseif penggunaan = \"Hutan Kota\" then \\nKode = 179\\nelseif penggunaan = \"Tanah Timbul\" then \\nKode = 180\\nelseif penggunaan = \"Obyek Wisata\" then \\nKode = 181\\nelseif penggunaan = \"Gedung Pertemuan\" then \\nKode = 182\\nelseif penggunaan = \"Pembangkit Tenaga Listrik\" then \\nKode = 183\\nelseif penggunaan = \"Rumah Susun\" then \\nKode = 184\\nelseif penggunaan = \"Apartemen\" then \\nKode = 185\\nelseif penggunaan = \"Bandara\" then \\nKode = 186\\nelseif penggunaan = \"Pergudangan\" then \\nKode = 187\\nelseif penggunaan = \"Komplek Militer\" then \\nKode = 188\\nelseif penggunaan = \"Pasir Pantai\" then \\nKode = 189\\nelseif penggunaan = \"Karang/Bebatuan\" then \\nKode = 190\\nelseif penggunaan = \"Lapangan Olahraga\" then \\nKode = 191\\nelseif penggunaan = \"Kawasan Industri\" then \\nKode = 192\\nelseif penggunaan = \"Stasiun KA\" then \\nKode = 193\\nelseif penggunaan = \"Jalur Hijau\" then \\nKode = 194\\nelseif penggunaan = \"Instalasi\" then \\nKode = 195\\nelseif penggunaan = \"Komplek Perbankan\" then \\nKode = 196\\nelseif penggunaan = \"Rumah Toko\" then \\nKode = 197\\nelseif penggunaan = \"Hutan Rawa\" then \\nKode = 198\\nelseif penggunaan = \"Rumah Kantor\" then \\nKode = 199\\nelseif penggunaan = \"Situs Bersejarah\" then \\nKode = 200\\nelseif penggunaan = \"Perairan Bekas Tambang\" then \\nKode = 201\\nelseif penggunaan = \"Tanah Reklamasi\" then \\nKode = 202\\nelseif penggunaan = \"Perternakan\" then \\nKode = 203\\nelseif penggunaan = \"Perikanan\" then \\nKode = 204\\nelseif penggunaan = \"Kawasan Konservasi \" then \\nKode = 205\\nelseif penggunaan = \"Gedung Olahraga\" then \\nKode = 206\\nelseif penggunaan = \"Perbengkelan\" then \\nKode = 207\\nelseif penggunaan = \"Rumah Makan\" then \\nKode = 208\\nelseif penggunaan = \"Fasilitas Sanitasi\" then \\nKode = 209\\nelseif penggunaan = \"Tempat Pelelangan Ikan\" then \\nKode = 210\\nelseif penggunaan = \"Penginapan\" then \\nKode = 211\\nelseif penggunaan = \"Tempat Hiburan\" then \\nKode = 212\\nelseif penggunaan = \"Jalan\" then \\nKode = 980\\nelseif penggunaan = \"Jalan Tol\" then \\nKode = 981\\nelseif penggunaan = \"Sungai\" then \\nKode = 990\\nelseif penggunaan = \"Sungai Besar\" then \\nKode = 991\\nelseif penggunaan = \"Laut Dalam\" then \\nKode = 79\\nelseif penggunaan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode =0\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                                except arcpy.ExecuteError, error:
                                    continue
                    # ptnRemarks
                    print "creating remarks"
                    arcpy.AddField_management(output, "ptnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        #            try:
         #               arcpy.CalculateField_management(output, "ptnRemarks", "[Keterangan]", "VB", "")
          #          except arcpy.ExecuteError, error:
           #             try:
            #                arcpy.CalculateField_management(output, "ptnRemarks", "[keterangan]", "VB", "")
             #           except arcpy.ExecuteError, error:
              #              continue
                    # area  
                    try:
                        print "try create area"
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
               #         try:
                #            print "try fill area"
                 #           arcpy.CalculateField_management(output, "area", "[luas_ha]", "VB", "")
                  #      except arcpy.ExecuteError, error:
                   #         try:
                    #            print "try fill area"
                     #           arcpy.CalculateField_management(output, "area", "[Luas_Ha]", "VB", "")
                      #      except arcpy.ExecuteError, error:
                       #         print "give up area"
                        #        continue
                    except arcpy.ExecuteError, error:
                        print "there Is already area field"
                        continue    
                    
                    #Process : Delete Field
                    print 'Deleting Originals Fields for Feature ' + output
                    try:
                        arcpy.DeleteField_management(output, "E")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "F")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "G")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Penggunaan")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "QNAME")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "LANDUSE")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Kode")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Kode_G")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Tipe")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "No_Idfier")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "No_Id")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Kec")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Kecamatan")
                    except arcpy.ExecuteError, error:
                        continue
                    try:
                        arcpy.DeleteField_management(output, "Nama_Layer")
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
