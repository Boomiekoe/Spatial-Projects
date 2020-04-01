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

#get user
sql = """select * from shp""" # where id > 292925
conn_mysql = MySQLdb.connect("localhost","root","","bpn")
cursor = conn_mysql.cursor()
cursor.execute(sql)
result = cursor.fetchall()
conn_mysql.close()
header = []
for get_data in result:
    id = get_data[0]
    data = get_data[1]
    data = data.replace('.shp','.dbf')
    print data
    try :
        table = DBF(data, load=True)
        get_json_colom = table.records[0]
    except :
        pass
        get_json_colom = ""
    get_json_colom = str(get_json_colom).replace('OrderedDict([','')
    get_json_colom = get_json_colom.replace('])','')
    get_json_colom = get_json_colom.split('), (')
    #print get_json_colom
    for getdata in get_json_colom:
        getdata = str(getdata).replace("u'","")
        getdata = getdata.replace("'","")
        getdata = getdata.replace("(","")
        getdata = getdata.replace(")","")
        getdata = getdata.split(", ")
        getdata = getdata[0]
        header.append(getdata)
    print header
 #end   
    sql = 'UPDATE shp SET struktur = "%s" where id = "%s"'%(str(header), id)
    conn_mysql = MySQLdb.connect("localhost","root","","bpn")
    cursor = conn_mysql.cursor()
    try:
        # Execute the SQL command
        cursor.execute('SET NAMES utf8mb4')
        cursor.execute("SET CHARACTER SET utf8mb4")
        cursor.execute(sql)
        # Commit your changes in the database
        conn_mysql.commit()
        print "success"
        print sql
    except Exception,e:
        print str(e)
        # Rollback in case there is any error
        conn_mysql.rollback()
        print "error"
        print sql
    conn_mysql.close()
    header = []
    #get_colom = json.loads(get_json_colom)
    #print(get_json_colom)
    #break
