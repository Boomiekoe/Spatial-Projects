import arcpy
import csv
import sys
import os


# 1 Folder Relatif
script_folder = sys.path[0]
tools_folder = os.path.dirname(script_folder)

#Buka CSV
with open('list_shp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for line in csv_reader:
        #gdb = 'Aceh.gdb' #line[0]
        #dataset = 'Pemanfaatan'
        #arcpy.env.workspace = str(os.path.join(tools_folder,gdb,dataset))
        featureclass = line[1]

        #for feature in featureclass:
        #print featureclass
        try:
            field_names = [f.name for f in arcpy.ListFields(featureclass)]
            fieldname = str(field_names)
            fieldname = fieldname.replace(" u","")
            fieldname = fieldname.replace("u","")
            fieldname = fieldname.replace("'OBJECTID',","")
            fieldname = fieldname.replace("'Shape',","")
            fieldname = fieldname.replace("'Shape_Length',","")
            fieldname = fieldname.replace("'Shape_Area',","")
            fieldname = fieldname.replace("'Shape_Leng',","")
            fieldname = fieldname.replace("'OBJECTID_1',","")
            fieldname = fieldname.replace("'SHAPE',","")
            fieldname = fieldname.replace("'SHAPE_Length',","")
            fieldname = fieldname.replace("'SHAPE_Area',","")
            fieldname = fieldname.replace("'SHAPE_Leng',","")
            print featureclass + ";" + fieldname
        except:
            print featureclass + ";['']"
            continue
            #### field sisa
            #fieldsisa = str(fieldname)
            #fieldsisa = fieldsisa.replace("'objID','objType','objYear','wapName','wakName','wacName','pfnID','pfnObjName','area','pfnRemarks'","")
            #fieldsisa = fieldsisa.replace("'objID'","")
            #fieldsisa = fieldsisa.replace("'objType'","")
            #fieldsisa = fieldsisa.replace("'objYear'","")
            #fieldsisa = fieldsisa.replace("'wapName'","")
            #fieldsisa = fieldsisa.replace("'wakName'","")
            #fieldsisa = fieldsisa.replace("'wacName'","")
            #fieldsisa = fieldsisa.replace("'pfnID'","")
            #fieldsisa = fieldsisa.replace("'pfnObjName'","")
            #fieldsisa = fieldsisa.replace("'pfnObjName'","")
            #fieldsisa = fieldsisa.replace("'area'","")
            #fieldsisa = fieldsisa.replace("'pfnRemarks'","")
            #fieldsisa = fieldsisa.replace(",,","")
                   
                
