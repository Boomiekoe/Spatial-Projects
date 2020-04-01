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
with open('gdb_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lompati = 0
    
    for line in csv_reader:
        if lompati > 0:
            try:
                # Local variables:
                gdb_in = line[0]
                gdb_out = line[1]
                htn_in = line[2]
                htn_out = line[3]
                #print
                #print gdb_in
                #print gdb_out
                #Change workspace
            
                try:
                    arcpy.env.workspace = str(os.path.join(tools_folder,gdb_in))
                    arcpy.env.overwriteOutput = True
                    gdb_output = output = str(os.path.join(tools_folder,gdb_out))
                    print arcpy.env.workspace
                    # Process: Project (moving)
                    print 'Moving ' + gdb_in + ' to Database'
                    datasetlist = arcpy.ListDatasets("*", "Feature")
                    for dataset in datasetlist:
                        feature_list = arcpy.ListFeatureClasses("*","ALL",dataset)
                        for fc in feature_list:
                            print 'Moving Feature ' + fc + ' to Database '+ gdb_output
                            output = str(os.path.join(tools_folder,gdb_out))+"/"+fc
                            arcpy.Copy_management(fc,output)
                    print "Moving RTRW " + gdb_in +" complete"

                except arcpy.ExecuteError, error:
                    print "skip RTRW"
                    continue
                try:
                    arcpy.env.workspace = str(os.path.join(tools_folder,htn_in))
                    arcpy.env.overwriteOutput = True
                    gdb_output = output = str(os.path.join(tools_folder,htn_out))
                    print arcpy.env.workspace
                    # Process: Project (moving)
                    print 'Moving ' + htn_in + ' to Database'
                    for file in os.listdir(arcpy.env.workspace):
                        if file.endswith (".shp"):
                            out_hut = str(os.path.join(tools_folder,htn_out))
                            #arcpy.Copy_management(file,out_hut)
                            arcpy.FeatureClassToGeodatabase_conversion(Input_Features= file, Output_Geodatabase = out_hut)

                    print "Moving Hutan " + htn_in +" complete"
                    print out_hut
                except arcpy.ExecuteError, error:
                    print "skip hutan"
                    continue
                print "Moving " + gdb_in +" and " + htn_in +" complete"    
                
            except arcpy.ExecuteError, error:
                print "Something went wrong handling " + ". Here's a traceback:"
                print "Moving " + gdb_in +" failed"
                continue
                

            
            
        else:
            
            pass
            
        lompati = lompati +1












