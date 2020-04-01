import csv
print "Selamat Datang"

open ('Absen.csv') as Data:
    Data_csv = csv.reader (Data, delimiter=',')    
