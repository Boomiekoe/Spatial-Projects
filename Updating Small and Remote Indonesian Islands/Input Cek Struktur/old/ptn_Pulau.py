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
with open('Penggunaan_Pulau.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0 
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[1]
                prov = line[6]
                gdb = prov +str('.gdb')
                output = str('ptnPulau_')+ line[13]
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
                    try:
                        arcpy.CalculateField_management(output, "ptnObjName", "[Pemilikan]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnObjName", "[pemilikan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            continue
                    # ptnID	
                    arcpy.AddField_management(output, "ptnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [ptnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    #arcpy.CalculateField_management(output, "ptnObjName", "pemilikan", "VB", "'Klasifikasi pemilikan @ gMAN2014\\n\\nkode = [ptnID] \\n'ISI KODE =   DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif kode = 1 then \\npemilikan =\"Terdaftar\"\\nelseif kode = 2 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 3 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 980 then \\npemilikan =\"Jalan\"\\nelseif kode = 990 then \\npemilikan =\"Sungai\"\\nelseif kode = 152 then \\npemilikan =\"Danau/Telaga/Situ\"\\n\\nelse\\npemilikan =\"    \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
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
                    #arcpy.CalculateField_management(output, "wacName", kec, "VB", "")
                    # wadName	
                    arcpy.AddField_management(output, "wadName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "wadName", kec, "VB", "")
                   # ptnID
                    arcpy.AddField_management(output, "ptnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # ptnObjName	
                    arcpy.AddField_management(output, "ptnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnObjName", "[PENGGUNAAN]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnObjName", "[Penggunaan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "ptnObjName", "[penggunaan]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "ptnObjName", "[JnisPnggun]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "ptnObjName", "[Ket_PGT]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                            arcpy.CalculateField_management(output, "ptnObjName", "[Jenis_Peng]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            try:
                                                arcpy.CalculateField_management(output, "ptnObjName", "[J_PGSN2]", "VB", "")
                                            except arcpy.ExecuteError, error:
                                                try:
                                                    arcpy.CalculateField_management(output, "ptnObjName", "[TANAH]", "VB", "")
                                                except arcpy.ExecuteError, error:
                                                    try:
                                                        arcpy.CalculateField_management(output, "ptnObjName", "[JENIS_PENG]", "VB", "")
                                                    except arcpy.ExecuteError, error:
                                                        try:
                                                            arcpy.CalculateField_management(output, "ptnObjName", "[Jenis]", "VB", "")
                                                        except arcpy.ExecuteError, error:
                                                            try:
                                                                arcpy.CalculateField_management(output, "ptnObjName", "[J_PGUNAAN]", "VB", "")
                                                            except arcpy.ExecuteError, error:
                                                                print "no ptnOBjName"
                    try:
                        arcpy.CalculateField_management(output, "ptnID", "[Kode]", "VB", "")
                    except arcpy.ExecuteError, error:
                        print "1"
                        try:
                            arcpy.CalculateField_management(output, "ptnID", "[kode]", "VB", "")
                        except arcpy.ExecuteError, error:
                            print "2"
                            try:
                                arcpy.CalculateField_management(output, "ptnID", "[Jenis_Pe_1]", "VB", "")
                            except arcpy.ExecuteError, error:
                                print "3"
                                try:
                                    arcpy.CalculateField_management(output, "ptnID", "[PGN]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    print "3"
                                    try:
                                        arcpy.CalculateField_management(output, "ptnID", "[KODE_JENIS]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        print "4"
                                        try:
                                            arcpy.CalculateField_management(output, "ptnID", "[KODE_PENGG]", "VB", "")
                                        except arcpy.ExecuteError, error:
                                            print "5"
                                            try:
                                                arcpy.CalculateField_management(output, "ptnID", "[Jns_PGT]", "VB", "")
                                            except arcpy.ExecuteError, error:
                                                print "6"
                                                try:
                                                    print ""#arcpy.CalculateField_management(output, "ptnID", "[Jns_Kuasa]", "VB", "")
                                                except arcpy.ExecuteError, error:
                                                    print "7"
                                                    try:
                                                        print ""#arcpy.CalculateField_management(output, "ptnID", "[STATUS_TNH]", "VB", "")
                                                    except arcpy.ExecuteError, error:
                                                        print "8"
                                                        try:
                                                           print "" #arcpy.CalculateField_management(output, "ptnID", "[ST_TNH]", "VB", "")
                                                        except arcpy.ExecuteError, error:
                                                            print "9"
                                                            try:
                                                                print ""#arcpy.CalculateField_management(output, "ptnID", "[TANAH]", "VB", "")
                                                            except arcpy.ExecuteError, error:
                                                                print "10"
                                                                try:
                                                                    arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Penggunaan @ gMAN 2014\\n\\npenggunaan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PENGGUNAAN\\n\\nif penggunaan = \"Perkampungan Jarang\" then \\nKode = 101\\nelseif penggunaan = \"Perkampungan Padat\" then \\nKode = 102\\nelseif penggunaan = \"Perumahan Jarang\" then \\nKode = 103\\nelseif penggunaan = \"Perumahan Padat\" then \\nKode = 104\\nelseif penggunaan = \"Emplasemen Sementara\" then \\nKode = 105\\nelseif penggunaan = \"Emplasemen Tetap\" then \\nKode = 106\\nelseif penggunaan = \"Komplek Olah Raga\" then \\nKode = 107\\nelseif penggunaan = \"Lapangan Golf\" then \\nKode = 108\\nelseif penggunaan = \"Taman\" then \\nKode = 109\\nelseif penggunaan = \"Pemakaman Umum\" then \\nKode = 110\\nelseif penggunaan = \"Pemakaman Khusus\" then \\nKode = 112\\nelseif penggunaan = \"Industri Aneka Pangan\" then \\nKode = 113\\nelseif penggunaan = \"Industri Aneka Sandang\" then \\nKode = 114\\nelseif penggunaan = \"Industri Aneka Kimia\" then \\nKode = 115\\nelseif penggunaan = \"Industri Aneka Bahan Bangunan dan Umum\" then \\nKode = 116\\nelseif penggunaan = \"Taman Makam Pahlawan\" then \\nKode = 111\\nelseif penggunaan = \"Industri Logam Dasar\" then \\nKode = 117\\nelseif penggunaan = \"Industri Kimia Dasar\" then \\nKode = 118\\nelseif penggunaan = \"Industri Kecil\" then \\nKode = 119\\nelseif penggunaan = \"Pertambangan Terbuka\" then \\nKode = 120\\nelseif penggunaan = \"Pertambangan Tertutup\" then \\nKode = 121\\nelseif penggunaan = \"Sawah Irigasi 2x Padi/Tahun\" then \\nKode = 122\\nelseif penggunaan = \"Sawah Irigasi 2x Padi/Tahun + Palawija\" then \\nKode = 123\\nelseif penggunaan = \"Sawah Irigasi Lebih Dari 2x Padi/Tahun\" then \\nKode = 124\\nelseif penggunaan = \"Sawah Irigasi 1x Padi/Tahun\" then \\nKode = 125\\nelseif penggunaan = \"Sawah Irigasi 1x Padi/Tahun + Palawija\" then \\nKode = 126\\nelseif penggunaan = \"Sawah Tadah Hujan\" then \\nKode = 127\\nelseif penggunaan = \"Sawah Pasang Surut 2x Padi/Tahun\" then \\nKode = 128\\nelseif penggunaan = \"Sawah Pasang Surut 2x Padi/Tahun + Palawija\" then \\nKode = 129\\nelseif penggunaan = \"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\" then \\nKode = 130\\nelseif penggunaan = \"Sawah Pasang Surut 1x Padi/Tahun\" then \\nKode = 131\\nelseif penggunaan = \"Sawah Pasang Surut 1x Padi/Tahun + Palawija\" then \\nKode = 132\\nelseif penggunaan = \"Tegalan/Ladang\" then \\nKode = 133\\nelseif penggunaan = \"Tanaman Sayuran\" then \\nKode = 134\\nelseif penggunaan = \"Tanaman Bunga\" then \\nKode = 135\\nelseif penggunaan = \"Kebun Campuran\" then \\nKode = 136\\nelseif penggunaan = \"Kebun Sejenis\" then \\nKode = 137\\nelseif penggunaan = \"Perkebunan Besar\" then \\nKode = 138\\nelseif penggunaan = \"Perkebunan Rakyat\" then \\nKode = 139\\nelseif penggunaan = \"Padang Rumput\" then \\nKode = 140\\nelseif penggunaan = \"Sabana\" then \\nKode = 141\\nelseif penggunaan = \"Alang-Alang\" then \\nKode = 142\\nelseif penggunaan = \"Semak Belukar\" then \\nKode = 143\\nelseif penggunaan = \"Hutan Lebat\" then \\nKode = 144\\nelseif penggunaan = \"Hutan Belukar\" then \\nKode = 145\\nelseif penggunaan = \"Hutan Sejenis Alami\" then \\nKode = 146\\nelseif penggunaan = \"Hutan Sejenis Buatan\" then \\nKode = 147\\nelseif penggunaan = \"Kolam Air Tawar/Empang\" then \\nKode = 148\\nelseif penggunaan = \"Tambak\" then \\nKode = 149\\nelseif penggunaan = \"Penggaraman\" then \\nKode = 150\\nelseif penggunaan = \"Waduk\" then \\nKode = 151\\nelseif penggunaan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif penggunaan = \"Rawa\" then \\nKode = 153\\nelseif penggunaan = \"Tanah Rusak\" then \\nKode = 154\\nelseif penggunaan = \"Tanah Tandus\" then \\nKode = 155\\nelseif penggunaan = \"Tanah Terbuka Sementara\" then \\nKode = 156\\nelseif penggunaan = \"Tanah Terbuka\" then \\nKode = 157\\nelseif penggunaan = \"Terminal\" then \\nKode = 158\\nelseif penggunaan = \"Padang Pasir\" then \\nKode = 159\\nelseif penggunaan = \"Dermaga Apung\" then \\nKode = 160\\nelseif penggunaan = \"Rumah di atas air\" then \\nKode = 161\\nelseif penggunaan = \"Mangrove\" then \\nKode = 162\\nelseif penggunaan = \"Gumuk Pasir\" then \\nKode = 163\\nelseif penggunaan = \"Gosong\" then \\nKode = 164\\nelseif penggunaan = \"Terumbu Karang\" then \\nKode = 165\\nelseif penggunaan = \"Pelabuhan Laut\" then \\nKode = 166\\nelseif penggunaan = \"Lainnya\" then \\nKode = 167\\nelseif penggunaan = \"Penginapan\" then \\nKode = 168\\nelseif penggunaan = \"Rumah Makan\" then \\nKode = 169\\nelseif penggunaan = \"SPBU\" then \\nKode = 170\\nelseif penggunaan = \"Perkantoran\" then \\nKode = 171\\nelseif penggunaan = \"Fasilitas Pendidikan\" then \\nKode = 172\\nelseif penggunaan = \"Fasilitas Kesehatan\" then \\nKode = 173\\nelseif penggunaan = \"Fasilitas Peribadatan\" then \\nKode = 174\\nelseif penggunaan = \"Keramba\" then \\nKode = 175\\nelseif penggunaan = \"Pertokoan\" then \\nKode = 176\\nelseif penggunaan = \"Pasar\" then \\nKode = 177\\nelseif penggunaan = \"Dam\" then \\nKode = 178\\nelseif penggunaan = \"Hutan Kota\" then \\nKode = 179\\nelseif penggunaan = \"Tanah Timbul\" then \\nKode = 180\\nelseif penggunaan = \"Obyek Wisata\" then \\nKode = 181\\nelseif penggunaan = \"Gedung Pertemuan\" then \\nKode = 182\\nelseif penggunaan = \"Pembangkit Tenaga Listrik\" then \\nKode = 183\\nelseif penggunaan = \"Rumah Susun\" then \\nKode = 184\\nelseif penggunaan = \"Apartemen\" then \\nKode = 185\\nelseif penggunaan = \"Bandara\" then \\nKode = 186\\nelseif penggunaan = \"Pergudangan\" then \\nKode = 187\\nelseif penggunaan = \"Komplek Militer\" then \\nKode = 188\\nelseif penggunaan = \"Pasir Pantai\" then \\nKode = 189\\nelseif penggunaan = \"Karang/Bebatuan\" then \\nKode = 190\\nelseif penggunaan = \"Lapangan Olahraga\" then \\nKode = 191\\nelseif penggunaan = \"Kawasan Industri\" then \\nKode = 192\\nelseif penggunaan = \"Stasiun KA\" then \\nKode = 193\\nelseif penggunaan = \"Jalur Hijau\" then \\nKode = 194\\nelseif penggunaan = \"Instalasi\" then \\nKode = 195\\nelseif penggunaan = \"Komplek Perbankan\" then \\nKode = 196\\nelseif penggunaan = \"Rumah Toko\" then \\nKode = 197\\nelseif penggunaan = \"Hutan Rawa\" then \\nKode = 198\\nelseif penggunaan = \"Rumah Kantor\" then \\nKode = 199\\nelseif penggunaan = \"Situs Bersejarah\" then \\nKode = 200\\nelseif penggunaan = \"Perairan Bekas Tambang\" then \\nKode = 201\\nelseif penggunaan = \"Tanah Reklamasi\" then \\nKode = 202\\nelseif penggunaan = \"Perternakan\" then \\nKode = 203\\nelseif penggunaan = \"Perikanan\" then \\nKode = 204\\nelseif penggunaan = \"Kawasan Konservasi \" then \\nKode = 205\\nelseif penggunaan = \"Gedung Olahraga\" then \\nKode = 206\\nelseif penggunaan = \"Perbengkelan\" then \\nKode = 207\\nelseif penggunaan = \"Rumah Makan\" then \\nKode = 208\\nelseif penggunaan = \"Fasilitas Sanitasi\" then \\nKode = 209\\nelseif penggunaan = \"Tempat Pelelangan Ikan\" then \\nKode = 210\\nelseif penggunaan = \"Penginapan\" then \\nKode = 211\\nelseif penggunaan = \"Tempat Hiburan\" then \\nKode = 212\\nelseif penggunaan = \"Jalan\" then \\nKode = 980\\nelseif penggunaan = \"Jalan Tol\" then \\nKode = 981\\nelseif penggunaan = \"Sungai\" then \\nKode = 990\\nelseif penggunaan = \"Sungai Besar\" then \\nKode = 991\\nelseif penggunaan = \"Laut Dalam\" then \\nKode = 79\\nelseif penggunaan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode =0\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                                                                except arcpy.ExecuteError, error:
                                                                    print "11 No ptnID"
                    try:
                        arcpy.CalculateField_management(output, "ptnObjName", "[PENGGUNAAN]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnObjName", "[Penggunaan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "ptnObjName", "[penggunaan]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    print"" #arcpy.CalculateField_management(output, "ptnObjName", "[STATUS]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        print"" #arcpy.CalculateField_management(output, "ptnObjName", "[Status]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                           arcpy.CalculateField_management(output, "ptnObjName", "penggunaan", "VB", "'Klasifikasi Penggunaan @ gMAN 2014\\n\\nkode = [ptnID] \\n'ISI KODE DENGAN NAMA KOLOM KODE PENGGUNAAN\\n\\nif kode = 101 then \\npenggunaan =\"Perkampungan Jarang\"\\nelseif kode = 102 then \\npenggunaan =\"Perkampungan Padat\"\\nelseif kode = 103 then \\npenggunaan =\"Perumahan Jarang\"\\nelseif kode = 104 then \\npenggunaan =\"Perumahan Padat\"\\nelseif kode = 105 then \\npenggunaan =\"Emplasemen Sementara\"\\nelseif kode = 106 then \\npenggunaan =\"Emplasemen Tetap\"\\nelseif kode = 161 then \\npenggunaan =\"Rumah di Atas Air\"\\nelseif kode = 184 then \\npenggunaan =\"Rumah Susun\"\\nelseif kode = 185 then \\npenggunaan =\"Apartemen\"\\nelseif kode = 170 then \\npenggunaan =\"SPBU\"\\nelseif kode = 176 then \\npenggunaan =\"Pertokoan\"\\nelseif kode = 177 then \\npenggunaan =\"Pasar\"\\nelseif kode = 196 then \\npenggunaan =\"Komplek Perbankan\"\\nelseif kode = 197 then \\npenggunaan =\"Rumah Toko\"\\nelseif kode = 207 then \\npenggunaan =\"Perbengkelan\"\\nelseif kode = 208 then \\npenggunaan =\"Rumah Makan\"\\nelseif kode = 210 then \\npenggunaan =\"Tempat Pelelangan Ikan\"\\nelseif kode = 211 then \\npenggunaan =\"Penginapan\"\\nelseif kode = 212 then \\npenggunaan =\"Tempat Hiburan\"\\nelseif kode = 171 then \\npenggunaan =\"Perkantoran\"\\nelseif kode = 199 then \\npenggunaan =\"Rumah Kantor\"\\nelseif kode = 113 then \\npenggunaan =\"Industri Aneka Pangan\"\\nelseif kode = 114 then \\npenggunaan =\"Industri Aneka Sandang\"\\nelseif kode = 115 then \\npenggunaan =\"Industri Aneka Kimia dan Serat\"\\nelseif kode = 116 then \\npenggunaan =\"Industri Aneka Bahan Bangunan dan Umum\"\\nelseif kode = 117 then \\npenggunaan =\"Industri Logam Dasar\"\\nelseif kode = 118 then \\npenggunaan =\"Industri Kimia Dasar\"\\nelseif kode = 119 then \\npenggunaan =\"Industri Kecil\"\\nelseif kode = 187 then \\npenggunaan =\"Pergudangan\"\\nelseif kode = 192 then \\npenggunaan =\"Kawasan Industri\"\\nelseif kode = 107 then \\npenggunaan =\"Komplek Olahraga\"\\nelseif kode = 108 then \\npenggunaan =\"Lapangan Golf\"\\nelseif kode = 110 then \\npenggunaan =\"Pemakaman Umum\"\\nelseif kode = 112 then \\npenggunaan =\"Pemakaman Khusus\"\\nelseif kode = 111 then \\npenggunaan =\"Taman Makam Pahlawan\"\\nelseif kode = 158 then \\npenggunaan =\"Terminal\"\\nelseif kode = 160 then \\npenggunaan =\"Dermaga Apung\"\\nelseif kode = 166 then \\npenggunaan =\"Pelabuhan Laut\"\\nelseif kode = 168 then \\npenggunaan =\"Penginapan\"\\nelseif kode = 172 then \\npenggunaan =\"Fasilitas Pendidikan\"\\nelseif kode = 173 then \\npenggunaan =\"Fasilitas Kesehatan\"\\nelseif kode = 174 then \\npenggunaan =\"Fasilitas Peribadatan\"\\nelseif kode = 182 then \\npenggunaan =\"Gedung Pertemuan\"\\nelseif kode = 186 then \\npenggunaan =\"Bandara\"\\nelseif kode = 191 then \\npenggunaan =\"Lapangan Olahraga\"\\nelseif kode = 193 then \\npenggunaan =\"Stasiun Kereta Api\"\\nelseif kode = 206 then \\npenggunaan =\"Gedung Olahraga\"\\nelseif kode = 209 then \\npenggunaan =\"Fasilitas Sanitasi\"\\nelseif kode = 122 then \\npenggunaan =\"Sawah Irigasi 2x Padi/Tahun\"\\nelseif kode = 123 then \\npenggunaan =\"Sawah Irigasi 2x Padi/Tahun + Palawija\"\\nelseif kode = 124 then \\npenggunaan =\"Sawah Irigasi Lebih dari 2x Padi/Tahun\"\\nelseif kode = 125 then \\npenggunaan =\"Sawah Irigasi 1x Padi/Tahun\"\\nelseif kode = 126 then \\npenggunaan =\"Sawah Irigasi 1x Padi/Tahun + Palawija\"\\nelseif kode = 127 then \\npenggunaan =\"Sawah Tadah Hujan\"\\nelseif kode = 128 then \\npenggunaan =\"Sawah Pasang Surut 2x Padi/Tahun\"\\nelseif kode = 129 then \\npenggunaan =\"Sawah Pasang Surut 2x Padi/Tahun + Palawija\"\\nelseif kode = 130 then \\npenggunaan =\"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\"\\nelseif kode = 131 then \\npenggunaan =\"Sawah Pasang Surut 1x Padi/Tahun\"\\nelseif kode = 132 then \\npenggunaan =\"Sawah Pasang Surut 1x Padi/Tahun + Palawija\"\\nelseif kode = 133 then \\npenggunaan =\"Tegalan/Ladang\"\\nelseif kode = 134 then \\npenggunaan =\"Tanaman Sayuran\"\\nelseif kode = 135 then \\npenggunaan =\"Tanaman Bunga\"\\nelseif kode = 136 then \\npenggunaan =\"Kebun Campuran\"\\nelseif kode = 137 then \\npenggunaan =\"Kebun Sejenis\"\\nelseif kode = 138 then \\npenggunaan =\"Perkebunan Besar\"\\nelseif kode = 139 then \\npenggunaan =\"Perkebunan Rakyat\"\\nelseif kode = 148 then \\npenggunaan =\"Kolam Air Tawar/Empang\"\\nelseif kode = 149 then \\npenggunaan =\"Tambak\"\\nelseif kode = 150 then \\npenggunaan =\"Penggaraman\"\\nelseif kode = 175 then \\npenggunaan =\"Keramba\"\\nelseif kode = 203 then \\npenggunaan =\"Perternakan\"\\nelseif kode = 204 then \\npenggunaan =\"Perikanan\"\\nelseif kode = 120 then \\npenggunaan =\"Pertambangan Terbuka\"\\nelseif kode = 121 then \\npenggunaan =\"Pertambangan Tertutup\"\\nelseif kode = 181 then \\npenggunaan =\"Obyek Wisata\"\\nelseif kode = 200 then \\npenggunaan =\"Situs Bersejarah\"\\nelseif kode = 183 then \\npenggunaan =\"Pembangkit Tenaga Listrik\"\\nelseif kode = 188 then \\npenggunaan =\"Komplek Militer\"\\nelseif kode = 205 then \\npenggunaan =\"Kawasan Konservasi\"\\nelseif kode = 151 then \\npenggunaan =\"Waduk\"\\nelseif kode = 178 then \\npenggunaan =\"Dam\"\\nelseif kode = 185 then \\npenggunaan =\"Instalasi\"\\nelseif kode = 980 then \\npenggunaan =\"Jalan\"\\nelseif kode = 981 then \\npenggunaan =\"Jalan Tol\"\\nelseif kode = 109 then \\npenggunaan =\"Taman\"\\nelseif kode = 147 then \\npenggunaan =\"Hutan Sejenis Buatan\"\\nelseif kode = 156 then \\npenggunaan =\"Tanah Terbuka Sementara\"\\nelseif kode = 179 then \\npenggunaan =\"Hutan Kota\"\\nelseif kode = 194 then \\npenggunaan =\"Jalur Hijau\"\\nelseif kode = 202 then \\npenggunaan =\"Tanah Reklamasi\"\\nelseif kode = 79 then \\npenggunaan =\"Laut Dalam\"\\nelseif kode = 80 then \\npenggunaan =\"Laut Dangkal\"\\nelseif kode = 140 then \\npenggunaan =\"Padang Rumput\"\\nelseif kode = 141 then \\npenggunaan =\"Sabana\"\\nelseif kode = 142 then \\npenggunaan =\"Alang-Alang\"\\nelseif kode = 143 then \\npenggunaan =\"Semak Belukar\"\\nelseif kode = 144 then \\npenggunaan =\"Hutan Lebat\"\\nelseif kode = 145 then \\npenggunaan =\"Hutan Belukar\"\\nelseif kode = 146 then \\npenggunaan =\"Hutan Sejenis Alami\"\\nelseif kode = 152 then \\npenggunaan =\"Danau/Telaga/Situ\"\\nelseif kode = 153 then \\npenggunaan =\"Rawa\"\\nelseif kode = 157 then \\npenggunaan =\"Tanah Terbuka\"\\nelseif kode = 159 then \\npenggunaan =\"Padang Pasir\"\\nelseif kode = 162 then \\npenggunaan =\"Mangrove\"\\nelseif kode = 163 then \\npenggunaan =\"Gumuk Pasir\"\\nelseif kode = 164 then \\npenggunaan =\"Gosong\"\\nelseif kode = 165 then \\npenggunaan =\"Terumbu Karang\"\\nelseif kode = 169 then \\npenggunaan =\"Rumah Makan\"\\nelseif kode = 180 then \\npenggunaan =\"Tanah Timbul\"\\nelseif kode = 189 then \\npenggunaan =\"Pasir Pantai\"\\nelseif kode = 190 then \\npenggunaan =\"Karang/Bebatuan\"\\nelseif kode = 198 then \\npenggunaan =\"Hutan Rawa\"\\nelseif kode = 991 then \\npenggunaan =\"Sungai Besar\"\\nelseif kode = 990 then \\npenggunaan =\"Sungai\"\\nelseif kode = 154 then \\npenggunaan =\"Tanah Rusak\"\\nelseif kode = 155 then \\npenggunaan =\"Tanah Tandus\"\\nelseif kode = 201 then \\npenggunaan =\"Perairan Bekas Tambang\"\\nelseif kode = 167 then \\npenggunaan =\"Lainnya\"\\n\\nelse\\npenggunaan =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n")
                                           print "objname clear"
                                        except arcpy.ExecuteError, error:
                                            print ""
                        
                    #arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [ptnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        print ""
                    
                    # ptnRemarks
                    arcpy.AddField_management(output, "ptnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnRemarks", "[KETERANGAN]", "VB", "")
                    except arcpy.ExecuteError, error:
                        try:
                            arcpy.CalculateField_management(output, "ptnRemarks", "[Keterangan]", "VB", "")
                        except arcpy.ExecuteError, error:
                            try:
                                arcpy.CalculateField_management(output, "ptnRemarks", "[keterangan]", "VB", "")
                            except arcpy.ExecuteError, error:
                                try:
                                    arcpy.CalculateField_management(output, "ptnRemarks", "[KET]", "VB", "")
                                except arcpy.ExecuteError, error:
                                    try:
                                        arcpy.CalculateField_management(output, "ptnRemarks", "[Ket]", "VB", "")
                                    except arcpy.ExecuteError, error:
                                        try:
                                            arcpy.CalculateField_management(output, "ptnRemarks", "[ket]", "VB", "")
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
                    # ptnID
                    arcpy.AddField_management(output, "ptnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "ptnID", "[JENIS]", "VB", "")
                    # ptnObjName	
                    arcpy.AddField_management(output, "ptnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "ptnObjName", "pemilikan", "VB", "'Klasifikasi pemilikan @ gMAN2014\\n\\nkode = [ptnID] \\n'ISI KODE =   DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif kode = 1 then \\npemilikan =\"Terdaftar\"\\nelseif kode = 2 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 3 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 980 then \\npemilikan =\"Jalan\"\\nelseif kode = 990 then \\npemilikan =\"Sungai\"\\nelseif kode = 152 then \\npemilikan =\"Danau/Telaga/Situ\"\\n\\nelse\\npemilikan =\"    \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "area", "[LUAS]", "VB", "")
                    # ptnRemarks
                    arcpy.AddField_management(output, "ptnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "ptnRemarks", "[KETERANGAN]", "VB", "")
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
