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
with open('Pfn_input.csv') as csv_file:
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
                output = str('pfn_')+ lines
                jens = line[3]
                pfn = 'Pemanfaatan'
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
                arcpy.env.workspace = str(os.path.join(tools_folder,gdb,pfn))
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
                               
                    # pfnID -- pfnObjName
                    arcpy.AddField_management(output, "pfnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.AddField_management(output, "pfnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "pfnID", ID, "VB", "")
                        arcpy.CalculateField_management(output, "pfnObjName", "pemanfaatan", "VB", "'Klasifikasi pemanfaatan @ gMAN 2014\\n\\nkode = [pfnID] \\n'ISI KODE DENGAN NAMA KOLOM KODE pemanfaatan\\n\\nif kode = 101 then \\npemanfaatan =\"Perkampungan Jarang\"\\nelseif kode = 102 then \\npemanfaatan =\"Perkampungan Padat\"\\nelseif kode = 103 then \\npemanfaatan =\"Perumahan Jarang\"\\nelseif kode = 104 then \\npemanfaatan =\"Perumahan Padat\"\\nelseif kode = 105 then \\npemanfaatan =\"Emplasemen Sementara\"\\nelseif kode = 106 then \\npemanfaatan =\"Emplasemen Tetap\"\\nelseif kode = 161 then \\npemanfaatan =\"Rumah di Atas Air\"\\nelseif kode = 184 then \\npemanfaatan =\"Rumah Susun\"\\nelseif kode = 185 then \\npemanfaatan =\"Apartemen\"\\nelseif kode = 170 then \\npemanfaatan =\"SPBU\"\\nelseif kode = 176 then \\npemanfaatan =\"Pertokoan\"\\nelseif kode = 177 then \\npemanfaatan =\"Pasar\"\\nelseif kode = 196 then \\npemanfaatan =\"Komplek Perbankan\"\\nelseif kode = 197 then \\npemanfaatan =\"Rumah Toko\"\\nelseif kode = 207 then \\npemanfaatan =\"Perbengkelan\"\\nelseif kode = 208 then \\npemanfaatan =\"Rumah Makan\"\\nelseif kode = 210 then \\npemanfaatan =\"Tempat Pelelangan Ikan\"\\nelseif kode = 211 then \\npemanfaatan =\"Penginapan\"\\nelseif kode = 212 then \\npemanfaatan =\"Tempat Hiburan\"\\nelseif kode = 171 then \\npemanfaatan =\"Perkantoran\"\\nelseif kode = 199 then \\npemanfaatan =\"Rumah Kantor\"\\nelseif kode = 113 then \\npemanfaatan =\"Industri Aneka Pangan\"\\nelseif kode = 114 then \\npemanfaatan =\"Industri Aneka Sandang\"\\nelseif kode = 115 then \\npemanfaatan =\"Industri Aneka Kimia dan Serat\"\\nelseif kode = 116 then \\npemanfaatan =\"Industri Aneka Bahan Bangunan dan Umum\"\\nelseif kode = 117 then \\npemanfaatan =\"Industri Logam Dasar\"\\nelseif kode = 118 then \\npemanfaatan =\"Industri Kimia Dasar\"\\nelseif kode = 119 then \\npemanfaatan =\"Industri Kecil\"\\nelseif kode = 187 then \\npemanfaatan =\"Pergudangan\"\\nelseif kode = 192 then \\npemanfaatan =\"Kawasan Industri\"\\nelseif kode = 107 then \\npemanfaatan =\"Komplek Olahraga\"\\nelseif kode = 108 then \\npemanfaatan =\"Lapangan Golf\"\\nelseif kode = 110 then \\npemanfaatan =\"Pemakaman Umum\"\\nelseif kode = 112 then \\npemanfaatan =\"Pemakaman Khusus\"\\nelseif kode = 111 then \\npemanfaatan =\"Taman Makam Pahlawan\"\\nelseif kode = 158 then \\npemanfaatan =\"Terminal\"\\nelseif kode = 160 then \\npemanfaatan =\"Dermaga Apung\"\\nelseif kode = 166 then \\npemanfaatan =\"Pelabuhan Laut\"\\nelseif kode = 168 then \\npemanfaatan =\"Penginapan\"\\nelseif kode = 172 then \\npemanfaatan =\"Fasilitas Pendidikan\"\\nelseif kode = 173 then \\npemanfaatan =\"Fasilitas Kesehatan\"\\nelseif kode = 174 then \\npemanfaatan =\"Fasilitas Peribadatan\"\\nelseif kode = 182 then \\npemanfaatan =\"Gedung Pertemuan\"\\nelseif kode = 186 then \\npemanfaatan =\"Bandara\"\\nelseif kode = 191 then \\npemanfaatan =\"Lapangan Olahraga\"\\nelseif kode = 193 then \\npemanfaatan =\"Stasiun Kereta Api\"\\nelseif kode = 206 then \\npemanfaatan =\"Gedung Olahraga\"\\nelseif kode = 209 then \\npemanfaatan =\"Fasilitas Sanitasi\"\\nelseif kode = 122 then \\npemanfaatan =\"Sawah Irigasi 2x Padi/Tahun\"\\nelseif kode = 123 then \\npemanfaatan =\"Sawah Irigasi 2x Padi/Tahun + Palawija\"\\nelseif kode = 124 then \\npemanfaatan =\"Sawah Irigasi Lebih dari 2x Padi/Tahun\"\\nelseif kode = 125 then \\npemanfaatan =\"Sawah Irigasi 1x Padi/Tahun\"\\nelseif kode = 126 then \\npemanfaatan =\"Sawah Irigasi 1x Padi/Tahun + Palawija\"\\nelseif kode = 127 then \\npemanfaatan =\"Sawah Tadah Hujan\"\\nelseif kode = 128 then \\npemanfaatan =\"Sawah Pasang Surut 2x Padi/Tahun\"\\nelseif kode = 129 then \\npemanfaatan =\"Sawah Pasang Surut 2x Padi/Tahun + Palawija\"\\nelseif kode = 130 then \\npemanfaatan =\"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\"\\nelseif kode = 131 then \\npemanfaatan =\"Sawah Pasang Surut 1x Padi/Tahun\"\\nelseif kode = 132 then \\npemanfaatan =\"Sawah Pasang Surut 1x Padi/Tahun + Palawija\"\\nelseif kode = 133 then \\npemanfaatan =\"Tegalan/Ladang\"\\nelseif kode = 134 then \\npemanfaatan =\"Tanaman Sayuran\"\\nelseif kode = 135 then \\npemanfaatan =\"Tanaman Bunga\"\\nelseif kode = 136 then \\npemanfaatan =\"Kebun Campuran\"\\nelseif kode = 137 then \\npemanfaatan =\"Kebun Sejenis\"\\nelseif kode = 138 then \\npemanfaatan =\"Perkebunan Besar\"\\nelseif kode = 139 then \\npemanfaatan =\"Perkebunan Rakyat\"\\nelseif kode = 148 then \\npemanfaatan =\"Kolam Air Tawar/Empang\"\\nelseif kode = 149 then \\npemanfaatan =\"Tambak\"\\nelseif kode = 150 then \\npemanfaatan =\"Penggaraman\"\\nelseif kode = 175 then \\npemanfaatan =\"Keramba\"\\nelseif kode = 203 then \\npemanfaatan =\"Perternakan\"\\nelseif kode = 204 then \\npemanfaatan =\"Perikanan\"\\nelseif kode = 120 then \\npemanfaatan =\"Pertambangan Terbuka\"\\nelseif kode = 121 then \\npemanfaatan =\"Pertambangan Tertutup\"\\nelseif kode = 181 then \\npemanfaatan =\"Obyek Wisata\"\\nelseif kode = 200 then \\npemanfaatan =\"Situs Bersejarah\"\\nelseif kode = 183 then \\npemanfaatan =\"Pembangkit Tenaga Listrik\"\\nelseif kode = 188 then \\npemanfaatan =\"Komplek Militer\"\\nelseif kode = 205 then \\npemanfaatan =\"Kawasan Konservasi\"\\nelseif kode = 151 then \\npemanfaatan =\"Waduk\"\\nelseif kode = 178 then \\npemanfaatan =\"Dam\"\\nelseif kode = 185 then \\npemanfaatan =\"Instalasi\"\\nelseif kode = 980 then \\npemanfaatan =\"Jalan\"\\nelseif kode = 981 then \\npemanfaatan =\"Jalan Tol\"\\nelseif kode = 109 then \\npemanfaatan =\"Taman\"\\nelseif kode = 147 then \\npemanfaatan =\"Hutan Sejenis Buatan\"\\nelseif kode = 156 then \\npemanfaatan =\"Tanah Terbuka Sementara\"\\nelseif kode = 179 then \\npemanfaatan =\"Hutan Kota\"\\nelseif kode = 194 then \\npemanfaatan =\"Jalur Hijau\"\\nelseif kode = 202 then \\npemanfaatan =\"Tanah Reklamasi\"\\nelseif kode = 79 then \\npemanfaatan =\"Laut Dalam\"\\nelseif kode = 80 then \\npemanfaatan =\"Laut Dangkal\"\\nelseif kode = 140 then \\npemanfaatan =\"Padang Rumput\"\\nelseif kode = 141 then \\npemanfaatan =\"Sabana\"\\nelseif kode = 142 then \\npemanfaatan =\"Alang-Alang\"\\nelseif kode = 143 then \\npemanfaatan =\"Semak Belukar\"\\nelseif kode = 144 then \\npemanfaatan =\"Hutan Lebat\"\\nelseif kode = 145 then \\npemanfaatan =\"Hutan Belukar\"\\nelseif kode = 146 then \\npemanfaatan =\"Hutan Sejenis Alami\"\\nelseif kode = 152 then \\npemanfaatan =\"Danau/Telaga/Situ\"\\nelseif kode = 153 then \\npemanfaatan =\"Rawa\"\\nelseif kode = 157 then \\npemanfaatan =\"Tanah Terbuka\"\\nelseif kode = 159 then \\npemanfaatan =\"Padang Pasir\"\\nelseif kode = 162 then \\npemanfaatan =\"Mangrove\"\\nelseif kode = 163 then \\npemanfaatan =\"Gumuk Pasir\"\\nelseif kode = 164 then \\npemanfaatan =\"Gosong\"\\nelseif kode = 165 then \\npemanfaatan =\"Terumbu Karang\"\\nelseif kode = 169 then \\npemanfaatan =\"Rumah Makan\"\\nelseif kode = 180 then \\npemanfaatan =\"Tanah Timbul\"\\nelseif kode = 189 then \\npemanfaatan =\"Pasir Pantai\"\\nelseif kode = 190 then \\npemanfaatan =\"Karang/Bebatuan\"\\nelseif kode = 198 then \\npemanfaatan =\"Hutan Rawa\"\\nelseif kode = 991 then \\npemanfaatan =\"Sungai Besar\"\\nelseif kode = 990 then \\npemanfaatan =\"Sungai\"\\nelseif kode = 154 then \\npemanfaatan =\"Tanah Rusak\"\\nelseif kode = 155 then \\npemanfaatan =\"Tanah Tandus\"\\nelseif kode = 201 then \\npemanfaatan =\"Perairan Bekas Tambang\"\\nelseif kode = 167 then \\npemanfaatan =\"Lainnya\"\\n\\nelse\\npemanfaatan =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n")
                    except arcpy.ExecuteError, error:
                        arcpy.CalculateField_management(output, "pfnObjName", objName, "VB", "")
                        arcpy.CalculateField_management(output, "pfnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [pfnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [pfnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n") 
                    
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        print "" 
                    # pfnRemarks
                    arcpy.AddField_management(output, "pfnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "pfnRemarks", remarks, "VB", "")
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
                   # pfnID
                    arcpy.AddField_management(output, "pfnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    
                    # pfnObjName	
                    arcpy.AddField_management(output, "pfnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "pfnID", ID, "VB", "")
                        arcpy.CalculateField_management(output, "pfnObjName", "pemanfaatan", "VB", "'Klasifikasi pemanfaatan @ gMAN 2014\\n\\nkode = [pfnID] \\n'ISI KODE DENGAN NAMA KOLOM KODE pemanfaatan\\n\\nif kode = 101 then \\npemanfaatan =\"Perkampungan Jarang\"\\nelseif kode = 102 then \\npemanfaatan =\"Perkampungan Padat\"\\nelseif kode = 103 then \\npemanfaatan =\"Perumahan Jarang\"\\nelseif kode = 104 then \\npemanfaatan =\"Perumahan Padat\"\\nelseif kode = 105 then \\npemanfaatan =\"Emplasemen Sementara\"\\nelseif kode = 106 then \\npemanfaatan =\"Emplasemen Tetap\"\\nelseif kode = 161 then \\npemanfaatan =\"Rumah di Atas Air\"\\nelseif kode = 184 then \\npemanfaatan =\"Rumah Susun\"\\nelseif kode = 185 then \\npemanfaatan =\"Apartemen\"\\nelseif kode = 170 then \\npemanfaatan =\"SPBU\"\\nelseif kode = 176 then \\npemanfaatan =\"Pertokoan\"\\nelseif kode = 177 then \\npemanfaatan =\"Pasar\"\\nelseif kode = 196 then \\npemanfaatan =\"Komplek Perbankan\"\\nelseif kode = 197 then \\npemanfaatan =\"Rumah Toko\"\\nelseif kode = 207 then \\npemanfaatan =\"Perbengkelan\"\\nelseif kode = 208 then \\npemanfaatan =\"Rumah Makan\"\\nelseif kode = 210 then \\npemanfaatan =\"Tempat Pelelangan Ikan\"\\nelseif kode = 211 then \\npemanfaatan =\"Penginapan\"\\nelseif kode = 212 then \\npemanfaatan =\"Tempat Hiburan\"\\nelseif kode = 171 then \\npemanfaatan =\"Perkantoran\"\\nelseif kode = 199 then \\npemanfaatan =\"Rumah Kantor\"\\nelseif kode = 113 then \\npemanfaatan =\"Industri Aneka Pangan\"\\nelseif kode = 114 then \\npemanfaatan =\"Industri Aneka Sandang\"\\nelseif kode = 115 then \\npemanfaatan =\"Industri Aneka Kimia dan Serat\"\\nelseif kode = 116 then \\npemanfaatan =\"Industri Aneka Bahan Bangunan dan Umum\"\\nelseif kode = 117 then \\npemanfaatan =\"Industri Logam Dasar\"\\nelseif kode = 118 then \\npemanfaatan =\"Industri Kimia Dasar\"\\nelseif kode = 119 then \\npemanfaatan =\"Industri Kecil\"\\nelseif kode = 187 then \\npemanfaatan =\"Pergudangan\"\\nelseif kode = 192 then \\npemanfaatan =\"Kawasan Industri\"\\nelseif kode = 107 then \\npemanfaatan =\"Komplek Olahraga\"\\nelseif kode = 108 then \\npemanfaatan =\"Lapangan Golf\"\\nelseif kode = 110 then \\npemanfaatan =\"Pemakaman Umum\"\\nelseif kode = 112 then \\npemanfaatan =\"Pemakaman Khusus\"\\nelseif kode = 111 then \\npemanfaatan =\"Taman Makam Pahlawan\"\\nelseif kode = 158 then \\npemanfaatan =\"Terminal\"\\nelseif kode = 160 then \\npemanfaatan =\"Dermaga Apung\"\\nelseif kode = 166 then \\npemanfaatan =\"Pelabuhan Laut\"\\nelseif kode = 168 then \\npemanfaatan =\"Penginapan\"\\nelseif kode = 172 then \\npemanfaatan =\"Fasilitas Pendidikan\"\\nelseif kode = 173 then \\npemanfaatan =\"Fasilitas Kesehatan\"\\nelseif kode = 174 then \\npemanfaatan =\"Fasilitas Peribadatan\"\\nelseif kode = 182 then \\npemanfaatan =\"Gedung Pertemuan\"\\nelseif kode = 186 then \\npemanfaatan =\"Bandara\"\\nelseif kode = 191 then \\npemanfaatan =\"Lapangan Olahraga\"\\nelseif kode = 193 then \\npemanfaatan =\"Stasiun Kereta Api\"\\nelseif kode = 206 then \\npemanfaatan =\"Gedung Olahraga\"\\nelseif kode = 209 then \\npemanfaatan =\"Fasilitas Sanitasi\"\\nelseif kode = 122 then \\npemanfaatan =\"Sawah Irigasi 2x Padi/Tahun\"\\nelseif kode = 123 then \\npemanfaatan =\"Sawah Irigasi 2x Padi/Tahun + Palawija\"\\nelseif kode = 124 then \\npemanfaatan =\"Sawah Irigasi Lebih dari 2x Padi/Tahun\"\\nelseif kode = 125 then \\npemanfaatan =\"Sawah Irigasi 1x Padi/Tahun\"\\nelseif kode = 126 then \\npemanfaatan =\"Sawah Irigasi 1x Padi/Tahun + Palawija\"\\nelseif kode = 127 then \\npemanfaatan =\"Sawah Tadah Hujan\"\\nelseif kode = 128 then \\npemanfaatan =\"Sawah Pasang Surut 2x Padi/Tahun\"\\nelseif kode = 129 then \\npemanfaatan =\"Sawah Pasang Surut 2x Padi/Tahun + Palawija\"\\nelseif kode = 130 then \\npemanfaatan =\"Sawah Pasang Surut Lebih dari 2x Padi/Tahun\"\\nelseif kode = 131 then \\npemanfaatan =\"Sawah Pasang Surut 1x Padi/Tahun\"\\nelseif kode = 132 then \\npemanfaatan =\"Sawah Pasang Surut 1x Padi/Tahun + Palawija\"\\nelseif kode = 133 then \\npemanfaatan =\"Tegalan/Ladang\"\\nelseif kode = 134 then \\npemanfaatan =\"Tanaman Sayuran\"\\nelseif kode = 135 then \\npemanfaatan =\"Tanaman Bunga\"\\nelseif kode = 136 then \\npemanfaatan =\"Kebun Campuran\"\\nelseif kode = 137 then \\npemanfaatan =\"Kebun Sejenis\"\\nelseif kode = 138 then \\npemanfaatan =\"Perkebunan Besar\"\\nelseif kode = 139 then \\npemanfaatan =\"Perkebunan Rakyat\"\\nelseif kode = 148 then \\npemanfaatan =\"Kolam Air Tawar/Empang\"\\nelseif kode = 149 then \\npemanfaatan =\"Tambak\"\\nelseif kode = 150 then \\npemanfaatan =\"Penggaraman\"\\nelseif kode = 175 then \\npemanfaatan =\"Keramba\"\\nelseif kode = 203 then \\npemanfaatan =\"Perternakan\"\\nelseif kode = 204 then \\npemanfaatan =\"Perikanan\"\\nelseif kode = 120 then \\npemanfaatan =\"Pertambangan Terbuka\"\\nelseif kode = 121 then \\npemanfaatan =\"Pertambangan Tertutup\"\\nelseif kode = 181 then \\npemanfaatan =\"Obyek Wisata\"\\nelseif kode = 200 then \\npemanfaatan =\"Situs Bersejarah\"\\nelseif kode = 183 then \\npemanfaatan =\"Pembangkit Tenaga Listrik\"\\nelseif kode = 188 then \\npemanfaatan =\"Komplek Militer\"\\nelseif kode = 205 then \\npemanfaatan =\"Kawasan Konservasi\"\\nelseif kode = 151 then \\npemanfaatan =\"Waduk\"\\nelseif kode = 178 then \\npemanfaatan =\"Dam\"\\nelseif kode = 185 then \\npemanfaatan =\"Instalasi\"\\nelseif kode = 980 then \\npemanfaatan =\"Jalan\"\\nelseif kode = 981 then \\npemanfaatan =\"Jalan Tol\"\\nelseif kode = 109 then \\npemanfaatan =\"Taman\"\\nelseif kode = 147 then \\npemanfaatan =\"Hutan Sejenis Buatan\"\\nelseif kode = 156 then \\npemanfaatan =\"Tanah Terbuka Sementara\"\\nelseif kode = 179 then \\npemanfaatan =\"Hutan Kota\"\\nelseif kode = 194 then \\npemanfaatan =\"Jalur Hijau\"\\nelseif kode = 202 then \\npemanfaatan =\"Tanah Reklamasi\"\\nelseif kode = 79 then \\npemanfaatan =\"Laut Dalam\"\\nelseif kode = 80 then \\npemanfaatan =\"Laut Dangkal\"\\nelseif kode = 140 then \\npemanfaatan =\"Padang Rumput\"\\nelseif kode = 141 then \\npemanfaatan =\"Sabana\"\\nelseif kode = 142 then \\npemanfaatan =\"Alang-Alang\"\\nelseif kode = 143 then \\npemanfaatan =\"Semak Belukar\"\\nelseif kode = 144 then \\npemanfaatan =\"Hutan Lebat\"\\nelseif kode = 145 then \\npemanfaatan =\"Hutan Belukar\"\\nelseif kode = 146 then \\npemanfaatan =\"Hutan Sejenis Alami\"\\nelseif kode = 152 then \\npemanfaatan =\"Danau/Telaga/Situ\"\\nelseif kode = 153 then \\npemanfaatan =\"Rawa\"\\nelseif kode = 157 then \\npemanfaatan =\"Tanah Terbuka\"\\nelseif kode = 159 then \\npemanfaatan =\"Padang Pasir\"\\nelseif kode = 162 then \\npemanfaatan =\"Mangrove\"\\nelseif kode = 163 then \\npemanfaatan =\"Gumuk Pasir\"\\nelseif kode = 164 then \\npemanfaatan =\"Gosong\"\\nelseif kode = 165 then \\npemanfaatan =\"Terumbu Karang\"\\nelseif kode = 169 then \\npemanfaatan =\"Rumah Makan\"\\nelseif kode = 180 then \\npemanfaatan =\"Tanah Timbul\"\\nelseif kode = 189 then \\npemanfaatan =\"Pasir Pantai\"\\nelseif kode = 190 then \\npemanfaatan =\"Karang/Bebatuan\"\\nelseif kode = 198 then \\npemanfaatan =\"Hutan Rawa\"\\nelseif kode = 991 then \\npemanfaatan =\"Sungai Besar\"\\nelseif kode = 990 then \\npemanfaatan =\"Sungai\"\\nelseif kode = 154 then \\npemanfaatan =\"Tanah Rusak\"\\nelseif kode = 155 then \\npemanfaatan =\"Tanah Tandus\"\\nelseif kode = 201 then \\npemanfaatan =\"Perairan Bekas Tambang\"\\nelseif kode = 167 then \\npemanfaatan =\"Lainnya\"\\n\\nelse\\npemanfaatan =\"\"\\nend if\\n\\n\\n\\n\\n\\n\\n")
                    except arcpy.ExecuteError, error:
                        arcpy.CalculateField_management(output, "pfnObjName", objName, "VB", "")
                        arcpy.CalculateField_management(output, "pfnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [pfnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [pfnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")    
                        
                    #arcpy.CalculateField_management(output, "pfnID", "Kode", "VB", "'Klasifikasi Kode Pemilikan @ gMAN 2014\\n\\npemilikan = [pfnObjName] \\n'ISI KODE DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif pemilikan = \"Terdaftar\" then \\nKode = 1\\nelseif pemilikan = \"Belum Terdaftar\" then \\nKode = 2\\nelseif pemilikan = \"Waduk\" then \\nKode = 151\\nelseif pemilikan = \"Danau/Telaga/Situ\" then \\nKode = 152\\nelseif pemilikan = \"Jalan\" then \\nKode = 980\\nelseif pemilikan = \"Jalan Tol\" then \\nKode = 981\\nelseif pemilikan = \"Sungai\" then \\nKode = 990\\nelseif pemilikan = \"Sungai Besar\" then \\nKode = 991\\nelseif pemilikan = \"Laut Dalam\" then \\nKode = 79\\nelseif pemilikan = \"Laut Dangkal\" then \\nKode = 80\\n\\nelse\\nkode = [pfnObjName] \\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    try:
                        arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    except arcpy.ExecuteError, error:
                        print ""
                    
                    # pfnRemarks
                    arcpy.AddField_management(output, "pfnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    try:
                        arcpy.CalculateField_management(output, "pfnRemarks", remarks, "VB", "")
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
                    # pfnID
                    arcpy.AddField_management(output, "pfnID", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "pfnID", "[JENIS]", "VB", "")
                    # pfnObjName	
                    arcpy.AddField_management(output, "pfnObjName", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "pfnObjName", "pemilikan", "VB", "'Klasifikasi pemilikan @ gMAN2014\\n\\nkode = [pfnID] \\n'ISI KODE =   DENGAN NAMA KOLOM KODE PEMILIKAN\\n\\nif kode = 1 then \\npemilikan =\"Terdaftar\"\\nelseif kode = 2 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 3 then \\npemilikan =\"Belum Terdaftar\"\\nelseif kode = 980 then \\npemilikan =\"Jalan\"\\nelseif kode = 990 then \\npemilikan =\"Sungai\"\\nelseif kode = 152 then \\npemilikan =\"Danau/Telaga/Situ\"\\n\\nelse\\npemilikan =\"    \"\\nend if\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
                    # area  
                    arcpy.AddField_management(output, "area", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "area", "[LUAS]", "VB", "")
                    # pfnRemarks
                    arcpy.AddField_management(output, "pfnRemarks", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                    arcpy.CalculateField_management(output, "pfnRemarks", "[KETERANGAN]", "VB", "")
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
