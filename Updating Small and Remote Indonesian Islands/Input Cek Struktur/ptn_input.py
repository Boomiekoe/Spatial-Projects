print "Memulai Tool"
import arcpy
import csv
import sys
import os

# 1. Mendapatkan folder relatif berdasarkan lokasi script.
script_folder = sys.path[0]
tools_folder = os.path.dirname(script_folder)
#print tools_folder
#print arcpy.env.workspace

#exit()
with open('Ptn_input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[1]
                prov = line[6]
                gdb = prov +str('.gdb')
                line13 = line[13]
                lines = line13.replace(" ","")
                output = str('ptn_')+ lines
                jens = line[3]
                ptn = 'Penggunaan'
                # Field 
                thn = line[5]
                kab = str('"')+line[7]+str('"')
                kec = str('"')+line[8]+str('"')
                pro = str('"')+line[6]+str('"')
                types = str('"')+line[4]+str('"')
                ID = str('[')+line[9]+str(']')
                objName = str('[')+line[10]+str(']')
                remarks = str('[')+line[11]+str(']')
                fields = line[2]
                fields = str(fields).replace("', '",";")
                fields = fields.replace("['",'"')
                fields = fields.replace("']",'"')
                                
                #print
                print shp
                print output
                #Change workspace
                arcpy.env.workspace = str(os.path.join(tools_folder,gdb,ptn))
                arcpy.env.overwriteOutput = True
                print arcpy.env.workspace
                folder = arcpy.env.workspace
                # Process: Project (moving)
                print 'Moving Feature ' + output + ' to Database'
            
                #project 
                try:
                    arcpy.Project_management(shp, output, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "", "", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
                except arcpy.ExecuteError, error:
                    arcpy.FeatureClassToFeatureClass_conversion(shp, folder, output, "", "", "")
                #Process : Adding Field
                print 'Create Format Fields for Feature ' + output
                print jens
                if jens == "1":
                    print "Bidang"
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
                               
                    # ptnID -- ptnObjName
                    arcpy.AddField_management(output, "ptnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.AddField_management(output, "ptnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnID", ID, "VB", "")
                        arcpy.CalculateField_management(output, "ptnObjName", "penggunaan", "VB", "'Klasifikasi Penggunaan @ gMAN 2014\\n\\nkode = [ptnID] \\n'ISI KODE DENGAN NAMA KOLOM KODE PENGGUNAAN\\n\\nif kode = 101 then \\npenggunaan =\"Perkampungan Jarang\"\\nelseif kode = 102 then \\npenggunaan =\"Perkampungan Padat\"\\nelseif kode = 103 then \\npenggunaan =\"Perumahan Jarang\"\\nelseif kode = 104 then \\npenggunaan =\"Perumahan Padat\"\\nelseif kode = 105 then \\npenggunaan =\"Emplasemen Sementara\"\\nelseif kode = 106 then \\npenggunaan =\"Emplasemen Tetap\"\\nelseif kode = 161 then \\npenggunaan =\"Rumah di Atas Air\"\\nelseif kode = 184 then \\npenggunaan =\"Rumah Susun\"\\nelseif kode = 185 then \\npenggunaan =\"Apartemen\"\\nelseif kode = 170 then \\npenggunaan =\"SPBU\"\\nelseif kode = 176 then \\npenggunaan =\"Pertokoan\"\\nelseif kode = 177 then \\npenggunaan =\"Pasar\"\\nelseif kode = 196 then \\npenggunaan =\"Komplek Perbankan\"\\nelseif kode = 197 then \\npenggunaan =\"Rumah Toko\"\\nelseif kode = 207 then \\npenggunaan =\"Perbengkelan\"\\nelseif kode = 208 then \\npenggunaan =\"Rumah Makan\"\\nelseif kode = 210 then \\npenggunaan =\"Tempat Pelelangan Ikan\"\\nelseif kode = 211 then \\npenggunaan =\"Penginapan\"\\nelseif kode = 212 then \\npenggunaan =\"Tempat Hiburan\"\\nelseif kode = 171 then \\npenggunaan =\"Perkantoran\"\\nelseif kode = 199 then \\npenggunaan =\"Rumah Kantor\"\\nelseif kode = 113 then \\npenggunaan =\"Industri Aneka Pangan\"\\nelseif kode = 114 then \\npenggunaan =\"Industri Aneka Sandang\"\\nelseif kode = 115 then \\npenggunaan =\"Industri Aneka Kimia dan Serat\"\\nelseif kode = 116 then \\npenggunaan =\"Industri Aneka Bahan Bangunan dan Umum\"\\nelseif kode = 117 then \\npenggunaan =\"Industri Logam Dasar\"\\nelseif kode = 118 then \\npenggunaan =\"Industri Kimia Dasar\"\\nelseif kode = 119 then \\npenggunaan =\"Industri Kecil\"\\nelseif kode = 187 then \\npenggunaan =\"Pergudangan\"\\nelseif kode = 192 then \\npenggunaan =\"Kawasan Industri\"\\nelseif kode = 107 then \\npenggunaan =\"Komplek Olahraga\"\\nelseif kode = 108 then \\npenggunaan =\"Lapangan Golf\"\\nelseif kode = 110 then \\npenggunaan =\"Pemakaman Umum\"\\nelseif kode = 112 then \\npenggunaan =\"Pemakaman Khusus\"\\nelseif kode = 111 then \\npenggunaan =\"Taman Makam Pahlawan\"\\nelseif kode = 158 then \\npenggunaan =\"Terminal\"\\nelseif kode = 160 then \\npenggunaan =\"Dermaga Apung\"\\nelseif kode = 166 then \\npenggunaan =\"Pelabuhan Laut\"\\nelseif kode = 168 then \\npenggunaan =\"Penginapan\"\\nelseif kode = 172 then \\npenggunaan =\"Fasilitas Pendidikan\"\\nelseif kode = 173 then \\npenggunaan =\"Fasilitas Kesehatan\"\\nelseif kode = 174 then \\npenggunaan =\"Fasilitas Peribadatan\"\\nelseif kode = 182 then \\npenggunaan =\"Gedung Pertemuan\"\\nelseif kode = 186 then \\npenggunaan =\"Bandara\"\\nelseif kode = 191 then \\npenggunaan =\"Lapangan Olahraga\"\\nelseif kode = 193 then \\npenggunaan =\"Stasiun Kereta Api\"\\nelseif kode = 206 then \\npenggunaan =\"Gedung Olahraga\"\\nelseif kode = 209 then \\npenggunaan =\"Fasilitas Sanitasi\"\\nelseif kode = 122 then \\npenggunaan =\"Sawah Irigasi 2x Padi/Tahun\"\\nelseif kode = 123 then \\npenggunaan =\"Sawah Irigasi 2x Padi/Tahun + Palawija\"\\nelseif kode = 124 then \\npenggunaan =\"Sawah Irigasi Lebih dari 2x Padi/Tahun\"\\nelseif kode = 125 then \\npenggunaan =\"Sawah Irigasi 1x Padi/Tahun\"\\nelseif kode = 126 then \\npenggunaan =\"Sawah Irigasi 1x Padi/Tahun + Palawija\"\\nelseif kode = 127 then \\npenggunaan =\"Sawah Tadah Hujan\"\\nelseif kode = 128 then \\npenggunaan =\"Sawah Pasang Surut 2x Padi/Tahun\"\\nelseif kode = 129 then \\npenggunaan =\"Sawah Pasang Surut 2x Padi/Tahun + Palawija\"\\nelseif kode = 130 then \\npenggunaan =\"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\"\\nelseif kode = 131 then \\npenggunaan =\"Sawah Pasang Surut 1x Padi/Tahun\"\\nelseif kode = 132 then \\npenggunaan =\"Sawah Pasang Surut 1x Padi/Tahun + Palawija\"\\nelseif kode = 133 then \\npenggunaan =\"Tegalan/Ladang\"\\nelseif kode = 134 then \\npenggunaan =\"Tanaman Sayuran\"\\nelseif kode = 135 then \\npenggunaan =\"Tanaman Bunga\"\\nelseif kode = 136 then \\npenggunaan =\"Kebun Campuran\"\\nelseif kode = 137 then \\npenggunaan =\"Kebun Sejenis\"\\nelseif kode = 138 then \\npenggunaan =\"Perkebunan Besar\"\\nelseif kode = 139 then \\npenggunaan =\"Perkebunan Rakyat\"\\nelseif kode = 148 then \\npenggunaan =\"Kolam Air Tawar/Empang\"\\nelseif kode = 149 then \\npenggunaan =\"Tambak\"\\nelseif kode = 150 then \\npenggunaan =\"Penggaraman\"\\nelseif kode = 175 then \\npenggunaan =\"Keramba\"\\nelseif kode = 203 then \\npenggunaan =\"Perternakan\"\\nelseif kode = 204 then \\npenggunaan =\"Perikanan\"\\nelseif kode = 120 then \\npenggunaan =\"Pertambangan Terbuka\"\\nelseif kode = 121 then \\npenggunaan =\"Pertambangan Tertutup\"\\nelseif kode = 181 then \\npenggunaan =\"Obyek Wisata\"\\nelseif kode = 200 then \\npenggunaan =\"Situs Bersejarah\"\\nelseif kode = 183 then \\npenggunaan =\"Pembangkit Tenaga Listrik\"\\nelseif kode = 188 then \\npenggunaan =\"Komplek Militer\"\\nelseif kode = 205 then \\npenggunaan =\"Kawasan Konservasi\"\\nelseif kode = 151 then \\npenggunaan =\"Waduk\"\\nelseif kode = 178 then \\npenggunaan =\"Dam\"\\nelseif kode = 185 then \\npenggunaan =\"Instalasi\"\\nelseif kode = 980 then \\npenggunaan =\"Jalan\"\\nelseif kode = 981 then \\npenggunaan =\"Jalan Tol\"\\nelseif kode = 109 then \\npenggunaan =\"Taman\"\\nelseif kode = 147 then \\npenggunaan =\"Hutan Sejenis Buatan\"\\nelseif kode = 156 then \\npenggunaan =\"Tanah Terbuka Sementara\"\\nelseif kode = 179 then \\npenggunaan =\"Hutan Kota\"\\nelseif kode = 194 then \\npenggunaan =\"Jalur Hijau\"\\nelseif kode = 202 then \\npenggunaan =\"Tanah Reklamasi\"\\nelseif kode = 79 then \\npenggunaan =\"Laut Dalam\"\\nelseif kode = 80 then \\npenggunaan =\"Laut Dangkal\"\\nelseif kode = 140 then \\npenggunaan =\"Padang Rumput\"\\nelseif kode = 141 then \\npenggunaan =\"Sabana\"\\nelseif kode = 142 then \\npenggunaan =\"Alang-Alang\"\\nelseif kode = 143 then \\npenggunaan =\"Semak Belukar\"\\nelseif kode = 144 then \\npenggunaan =\"Hutan Lebat\"\\nelseif kode = 145 then \\npenggunaan =\"Hutan Belukar\"\\nelseif kode = 146 then \\npenggunaan =\"Hutan Sejenis Alami\"\\nelseif kode = 152 then \\npenggunaan =\"Danau/Telaga/Situ\"\\nelseif kode = 153 then \\npenggunaan =\"Rawa\"\\nelseif kode = 157 then \\npenggunaan =\"Tanah Terbuka\"\\nelseif kode = 159 then \\npenggunaan =\"Padang Pasir\"\\nelseif kode = 162 then \\npenggunaan =\"Mangrove\"\\nelseif kode = 163 then \\npenggunaan =\"Gumuk Pasir\"\\nelseif kode = 164 then \\npenggunaan =\"Gosong\"\\nelseif kode = 165 then \\npenggunaan =\"Terumbu Karang\"\\nelseif kode = 169 then \\npenggunaan =\"Rumah Makan\"\\nelseif kode = 180 then \\npenggunaan =\"Tanah Timbul\"\\nelseif kode = 189 then \\npenggunaan =\"Pasir Pantai\"\\nelseif kode = 190 then \\npenggunaan =\"Karang/Bebatuan\"\\nelseif kode = 198 then \\npenggunaan =\"Hutan Rawa\"\\nelseif kode = 991 then \\npenggunaan =\"Sungai Besar\"\\nelseif kode = 990 then \\npenggunaan =\"Sungai\"\\nelseif kode = 154 then \\npenggunaan =\"Tanah Rusak\"\\nelseif kode = 155 then \\npenggunaan =\"Tanah Tandus\"\\nelseif kode = 201 then \\npenggunaan =\"Perairan Bekas Tambang\"\\nelseif kode = 167 then \\npenggunaan =\"Lainnya\"\\n\\nelse\\npenggunaan =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n")
                    except arcpy.ExecuteError, error:
                        arcpy.CalculateField_management(output, "ptnObjName", objName, "VB", "")
                        arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [ptnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n") 
                    
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        print "" 
                    # ptnRemarks
                    arcpy.AddField_management(output, "ptnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnRemarks", remarks, "VB", "")
                    except arcpy.ExecuteError, error:
                        print ""
                    #Process : Delete Field
                    print "Removing Fields : " +fields
                    arcpy.DeleteField_management(output, fields)
#2
                elif jens == "2":
                    print "Pulau"
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
                        arcpy.CalculateField_management(output, "ptnID", ID, "VB", "")
                        arcpy.CalculateField_management(output, "ptnObjName", "penggunaan", "VB", "'Klasifikasi Penggunaan @ gMAN 2014\\n\\nkode = [ptnID] \\n'ISI KODE DENGAN NAMA KOLOM KODE PENGGUNAAN\\n\\nif kode = 101 then \\npenggunaan =\"Perkampungan Jarang\"\\nelseif kode = 102 then \\npenggunaan =\"Perkampungan Padat\"\\nelseif kode = 103 then \\npenggunaan =\"Perumahan Jarang\"\\nelseif kode = 104 then \\npenggunaan =\"Perumahan Padat\"\\nelseif kode = 105 then \\npenggunaan =\"Emplasemen Sementara\"\\nelseif kode = 106 then \\npenggunaan =\"Emplasemen Tetap\"\\nelseif kode = 161 then \\npenggunaan =\"Rumah di Atas Air\"\\nelseif kode = 184 then \\npenggunaan =\"Rumah Susun\"\\nelseif kode = 185 then \\npenggunaan =\"Apartemen\"\\nelseif kode = 170 then \\npenggunaan =\"SPBU\"\\nelseif kode = 176 then \\npenggunaan =\"Pertokoan\"\\nelseif kode = 177 then \\npenggunaan =\"Pasar\"\\nelseif kode = 196 then \\npenggunaan =\"Komplek Perbankan\"\\nelseif kode = 197 then \\npenggunaan =\"Rumah Toko\"\\nelseif kode = 207 then \\npenggunaan =\"Perbengkelan\"\\nelseif kode = 208 then \\npenggunaan =\"Rumah Makan\"\\nelseif kode = 210 then \\npenggunaan =\"Tempat Pelelangan Ikan\"\\nelseif kode = 211 then \\npenggunaan =\"Penginapan\"\\nelseif kode = 212 then \\npenggunaan =\"Tempat Hiburan\"\\nelseif kode = 171 then \\npenggunaan =\"Perkantoran\"\\nelseif kode = 199 then \\npenggunaan =\"Rumah Kantor\"\\nelseif kode = 113 then \\npenggunaan =\"Industri Aneka Pangan\"\\nelseif kode = 114 then \\npenggunaan =\"Industri Aneka Sandang\"\\nelseif kode = 115 then \\npenggunaan =\"Industri Aneka Kimia dan Serat\"\\nelseif kode = 116 then \\npenggunaan =\"Industri Aneka Bahan Bangunan dan Umum\"\\nelseif kode = 117 then \\npenggunaan =\"Industri Logam Dasar\"\\nelseif kode = 118 then \\npenggunaan =\"Industri Kimia Dasar\"\\nelseif kode = 119 then \\npenggunaan =\"Industri Kecil\"\\nelseif kode = 187 then \\npenggunaan =\"Pergudangan\"\\nelseif kode = 192 then \\npenggunaan =\"Kawasan Industri\"\\nelseif kode = 107 then \\npenggunaan =\"Komplek Olahraga\"\\nelseif kode = 108 then \\npenggunaan =\"Lapangan Golf\"\\nelseif kode = 110 then \\npenggunaan =\"Pemakaman Umum\"\\nelseif kode = 112 then \\npenggunaan =\"Pemakaman Khusus\"\\nelseif kode = 111 then \\npenggunaan =\"Taman Makam Pahlawan\"\\nelseif kode = 158 then \\npenggunaan =\"Terminal\"\\nelseif kode = 160 then \\npenggunaan =\"Dermaga Apung\"\\nelseif kode = 166 then \\npenggunaan =\"Pelabuhan Laut\"\\nelseif kode = 168 then \\npenggunaan =\"Penginapan\"\\nelseif kode = 172 then \\npenggunaan =\"Fasilitas Pendidikan\"\\nelseif kode = 173 then \\npenggunaan =\"Fasilitas Kesehatan\"\\nelseif kode = 174 then \\npenggunaan =\"Fasilitas Peribadatan\"\\nelseif kode = 182 then \\npenggunaan =\"Gedung Pertemuan\"\\nelseif kode = 186 then \\npenggunaan =\"Bandara\"\\nelseif kode = 191 then \\npenggunaan =\"Lapangan Olahraga\"\\nelseif kode = 193 then \\npenggunaan =\"Stasiun Kereta Api\"\\nelseif kode = 206 then \\npenggunaan =\"Gedung Olahraga\"\\nelseif kode = 209 then \\npenggunaan =\"Fasilitas Sanitasi\"\\nelseif kode = 122 then \\npenggunaan =\"Sawah Irigasi 2x Padi/Tahun\"\\nelseif kode = 123 then \\npenggunaan =\"Sawah Irigasi 2x Padi/Tahun + Palawija\"\\nelseif kode = 124 then \\npenggunaan =\"Sawah Irigasi Lebih dari 2x Padi/Tahun\"\\nelseif kode = 125 then \\npenggunaan =\"Sawah Irigasi 1x Padi/Tahun\"\\nelseif kode = 126 then \\npenggunaan =\"Sawah Irigasi 1x Padi/Tahun + Palawija\"\\nelseif kode = 127 then \\npenggunaan =\"Sawah Tadah Hujan\"\\nelseif kode = 128 then \\npenggunaan =\"Sawah Pasang Surut 2x Padi/Tahun\"\\nelseif kode = 129 then \\npenggunaan =\"Sawah Pasang Surut 2x Padi/Tahun + Palawija\"\\nelseif kode = 130 then \\npenggunaan =\"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\"\\nelseif kode = 131 then \\npenggunaan =\"Sawah Pasang Surut 1x Padi/Tahun\"\\nelseif kode = 132 then \\npenggunaan =\"Sawah Pasang Surut 1x Padi/Tahun + Palawija\"\\nelseif kode = 133 then \\npenggunaan =\"Tegalan/Ladang\"\\nelseif kode = 134 then \\npenggunaan =\"Tanaman Sayuran\"\\nelseif kode = 135 then \\npenggunaan =\"Tanaman Bunga\"\\nelseif kode = 136 then \\npenggunaan =\"Kebun Campuran\"\\nelseif kode = 137 then \\npenggunaan =\"Kebun Sejenis\"\\nelseif kode = 138 then \\npenggunaan =\"Perkebunan Besar\"\\nelseif kode = 139 then \\npenggunaan =\"Perkebunan Rakyat\"\\nelseif kode = 148 then \\npenggunaan =\"Kolam Air Tawar/Empang\"\\nelseif kode = 149 then \\npenggunaan =\"Tambak\"\\nelseif kode = 150 then \\npenggunaan =\"Penggaraman\"\\nelseif kode = 175 then \\npenggunaan =\"Keramba\"\\nelseif kode = 203 then \\npenggunaan =\"Perternakan\"\\nelseif kode = 204 then \\npenggunaan =\"Perikanan\"\\nelseif kode = 120 then \\npenggunaan =\"Pertambangan Terbuka\"\\nelseif kode = 121 then \\npenggunaan =\"Pertambangan Tertutup\"\\nelseif kode = 181 then \\npenggunaan =\"Obyek Wisata\"\\nelseif kode = 200 then \\npenggunaan =\"Situs Bersejarah\"\\nelseif kode = 183 then \\npenggunaan =\"Pembangkit Tenaga Listrik\"\\nelseif kode = 188 then \\npenggunaan =\"Komplek Militer\"\\nelseif kode = 205 then \\npenggunaan =\"Kawasan Konservasi\"\\nelseif kode = 151 then \\npenggunaan =\"Waduk\"\\nelseif kode = 178 then \\npenggunaan =\"Dam\"\\nelseif kode = 185 then \\npenggunaan =\"Instalasi\"\\nelseif kode = 980 then \\npenggunaan =\"Jalan\"\\nelseif kode = 981 then \\npenggunaan =\"Jalan Tol\"\\nelseif kode = 109 then \\npenggunaan =\"Taman\"\\nelseif kode = 147 then \\npenggunaan =\"Hutan Sejenis Buatan\"\\nelseif kode = 156 then \\npenggunaan =\"Tanah Terbuka Sementara\"\\nelseif kode = 179 then \\npenggunaan =\"Hutan Kota\"\\nelseif kode = 194 then \\npenggunaan =\"Jalur Hijau\"\\nelseif kode = 202 then \\npenggunaan =\"Tanah Reklamasi\"\\nelseif kode = 79 then \\npenggunaan =\"Laut Dalam\"\\nelseif kode = 80 then \\npenggunaan =\"Laut Dangkal\"\\nelseif kode = 140 then \\npenggunaan =\"Padang Rumput\"\\nelseif kode = 141 then \\npenggunaan =\"Sabana\"\\nelseif kode = 142 then \\npenggunaan =\"Alang-Alang\"\\nelseif kode = 143 then \\npenggunaan =\"Semak Belukar\"\\nelseif kode = 144 then \\npenggunaan =\"Hutan Lebat\"\\nelseif kode = 145 then \\npenggunaan =\"Hutan Belukar\"\\nelseif kode = 146 then \\npenggunaan =\"Hutan Sejenis Alami\"\\nelseif kode = 152 then \\npenggunaan =\"Danau/Telaga/Situ\"\\nelseif kode = 153 then \\npenggunaan =\"Rawa\"\\nelseif kode = 157 then \\npenggunaan =\"Tanah Terbuka\"\\nelseif kode = 159 then \\npenggunaan =\"Padang Pasir\"\\nelseif kode = 162 then \\npenggunaan =\"Mangrove\"\\nelseif kode = 163 then \\npenggunaan =\"Gumuk Pasir\"\\nelseif kode = 164 then \\npenggunaan =\"Gosong\"\\nelseif kode = 165 then \\npenggunaan =\"Terumbu Karang\"\\nelseif kode = 169 then \\npenggunaan =\"Rumah Makan\"\\nelseif kode = 180 then \\npenggunaan =\"Tanah Timbul\"\\nelseif kode = 189 then \\npenggunaan =\"Pasir Pantai\"\\nelseif kode = 190 then \\npenggunaan =\"Karang/Bebatuan\"\\nelseif kode = 198 then \\npenggunaan =\"Hutan Rawa\"\\nelseif kode = 991 then \\npenggunaan =\"Sungai Besar\"\\nelseif kode = 990 then \\npenggunaan =\"Sungai\"\\nelseif kode = 154 then \\npenggunaan =\"Tanah Rusak\"\\nelseif kode = 155 then \\npenggunaan =\"Tanah Tandus\"\\nelseif kode = 201 then \\npenggunaan =\"Perairan Bekas Tambang\"\\nelseif kode = 167 then \\npenggunaan =\"Lainnya\"\\n\\nelse\\npenggunaan =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n")
                    except arcpy.ExecuteError, error:
                        arcpy.CalculateField_management(output, "ptnObjName", objName, "VB", "")
                        arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [ptnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")    
                        
                    #arcpy.CalculateField_management(output, "ptnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [ptnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [ptnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        print ""
                    
                    # ptnRemarks
                    arcpy.AddField_management(output, "ptnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "ptnRemarks", remarks, "VB", "")
                    except arcpy.ExecuteError, error:
                        print ""
                    #Process : Delete Field
                    print "Removing Fields : " +fields
                    arcpy.DeleteField_management(output, fields) 
                    
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
