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
with open('PTN.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                shp = line[0]
                prov = line[1]
                kab = line[2]
                gdb = prov +str('.gdb')
                output = line[4]
                ptn = 'Penggunaan'
                print shp
                print prov
                print kab
                #print gdb
                print output
                #Change workspace
                arcpy.env.workspace = str(os.path.join(tools_folder,gdb,ptn))
                arcpy.env.overwriteOutput = True
                print arcpy.env.workspace
            
                # Process: Project
                arcpy.Project_management(shp, output, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "", "", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")

            except arcpy.ExecuteError, error:
                print "Something went wrong handling " + ". Here's a traceback:"
                print output
                continue

            print "repeat"
            
        else:
            
            pass
            
        lompati = lompati +1
