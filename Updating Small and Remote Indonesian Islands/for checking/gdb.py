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
with open('gdb.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    for line in csv_reader:
        if lompati > 0:
            arcpy.env.workspace = str(os.path.join(tools_folder,))
            arcpy.env.overwriteOutput = True
            Prov = line[0]
            print Prov
            #Local variables:
            File_GDB_Location = "E:\\"
            tes_gdb = File_GDB_Location
            Prov_gdb = Prov +str(".gdb")
            # Process: Create File GDB
            print "Membuat GDB " + str(Prov) + ".gdb"
            arcpy.CreateFileGDB_management(File_GDB_Location, Prov, "CURRENT")
            # Pindah workspace
            arcpy.env.workspace = str(os.path.join(tools_folder,Prov_gdb))
            arcpy.env.overwriteOutput = True
            print arcpy.env.workspace
            Admin = "Administrasi"
            Hutan = "Hutan"
            Monev = "Monev"
            pmn = "Pemilikan"
            pnf = "Pemanfaatan"
            ptn = "Penggunaan"
            psn = "Penguasaan"
            RTRW = "RTRW"
            ZPPK = "ZPPK"
            # Process: Create Feature Dataset Admin
            print "Membuat Dataset 10%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, Admin, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset Hutan
            print "Membuat Dataset 20%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, Hutan, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset Monev
            print "Membuat Dataset 30%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, Monev, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset pmn
            print "Membuat Dataset 40%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, pmn, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset pnf
            print "Membuat Dataset 60%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, pnf, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset ptn
            print "Membuat Dataset 70%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, ptn, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset psn
            print "Membuat Dataset 80%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, psn, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset RTRW
            print "Membuat Dataset 90%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, RTRW, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")
            # Process: Create Feature Dataset ZPPK
            print "Membuat Dataset 100%"
            arcpy.CreateFeatureDataset_management(Prov_gdb, ZPPK, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")

            print "repeat"
        else:
            print "finish"
            pass
        lompati = lompati +1
