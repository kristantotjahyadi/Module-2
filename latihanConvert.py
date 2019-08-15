import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'alfaindah25',
    database = 'marvel')

# MEMBUAT DATABASE DAN TABEL DALAM MYSQL===========================

kursor = dbku.cursor()
data = [('Spiderman', 25, 'Jakarta'),
('Black Panther', 32, 'Wakanda'),
('Black Widow', 27, 'Cianjur'),
('Doctor Strange', 41, 'Bogor'),
('Hulk', 40, 'Garut'),
('Warmachine', 46, 'Jombang'),
('Captain Marvel', 22, 'Bogor'),
('Ant Man', 37, 'Jakarta')]
querydb = ('''insert into avengers (title,usia,kota) values
(%s, %s, %s)''')
kursor.executemany(querydb, data)
dbku.commit()

# MENGUBAH MYSQL MENJADI CSV=======================================

import csv
koleksi = []
kursor.execute('select * from avengers')
for i in kursor.fetchall():
    data = {'id' : i[0], 'title' : i[1], 'usia': i[2], 'kota': i[3]}
    koleksi.append(data)
with open('mysqltocsv.csv', 'w', newline= '') as x:
    kolom = list(koleksi[0].keys())
    tulis = csv.DictWriter(x, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(koleksi)

# MENGUBAH MYSQL MENJADI JSON=======================================

import json
with open('mysqltojson.json','w') as y:
    json.dump(koleksi,y)

# MENGUBAH JSON MENJADI CSV=========================================
import csv
import json
with open('mysqltojson.json') as x:
    dataJson = json.load(x)
with open('jsontocsv.csv', 'w', newline='') as y:
    kolom = list(dataJson[0].keys())
    tulis = csv.DictWriter(y, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(dataJson)

# MENGUBAH CSV MENJADI JSON=========================================
koleksi = []
with open('jsontocsv.csv','r') as z:
    baca = csv.DictReader(z)
    for i in baca:
        koleksi.append(dict(i))
with open('csvtojson.json', 'w') as x:
    json.dump(koleksi, x)

# MENGUBAH CSV MENJADI MYSQL========================================
koleksi = []
koleksiku = []
with open('mysqltocsv.csv','r') as x:
    baca = csv.DictReader(x)
    for i in baca:
        koleksi.append(list(dict(i).values()))
for j in koleksi:
    koleksiku.append(tuple(j))
querydb = ('''insert into superhero (id, title, usia, kota) values
(%s,%s,%s,%s)''')
kursor.executemany(querydb,koleksiku)
dbku.commit()

# MENGUBAH JSON MENJADI MYSQL========================================
import json
koleksi = []
with open('csvtojson.json') as x:
    dataJson = json.load(x)
for i in dataJson:
    koleksi.append(tuple(dict(i).values()))
querydb = ('''insert into superheroes (id,title,usia,kota) values
(%s,%s,%s,%s)''')
kursor.executemany(querydb, koleksi)
dbku.commit()

# MENGUBAH JSON MENJADI MONGODB======================================
import json
import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
database = input('Masukkan database yang diinginkan : ')
db = x[database]
collection = input('Masukkan collection yang diinginkan : ')
col = db[collection]
with open('csvtojson.json') as y:
    data = json.load(y)
z = col.insert_many(data)

# MENGUBAH CSV MENJADI MONGODB==========================================
import csv
import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
database = input('Masukkan database yang diinginkan : ')
db = x[database]
collection = input('Masukkan collection yang diinginkan : ')
col = db[collection]
data = []
with open('jsontocsv.csv', 'r') as x:
    baca = csv.DictReader(x)
    for i in baca:
        data.append(dict(i))
z = col.insert_many(data)

# MENGUBAH MYSQL MENJADI MONGODB========================================
import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
database = input('Masukkan database yang diinginkan : ')
db = x[database]
collection = input('Masukkan collection yang diinginkan : ')
col = db[collection]
koleksi = []
kursor.execute(''' select * from avengers ''')
for data in kursor.fetchall():
    koleksi.append({'id' : data[0], 'title' : data[1], 'usia' : data[2], 'kota' : data[3]})
z = col.insert_many(koleksi)

# MENGUBAH MONGODB MENJADI JSON=========================================
import pymongo
import json
x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['avengers']
col = db['teams']
data = (list(col.find()))
koleksi = []
for i in data:
    koleksi.append({'_id': str(i['_id']), 'id' : i['id'], 'title' : i['title'], 'usia' : i['usia'], 'kota' : i['kota']})
with open('mongodbtojson.json', 'w') as x:
    json.dump(koleksi,x)

# MENGUBAH MONGODB MENJADI CSV==========================================
import csv
import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['avengers']
col = db['teams']
koleksi = []
data = (list(col.find()))
for i in data:
    koleksi.append({'_id': str(i['_id']), 'id' : i['id'], 'title' : i['title'], 'usia' : i['usia'], 'kota' : i['kota']})
with open('mongodbtocsv.csv', 'w',newline='') as y:
    kolom = koleksi[0].keys()
    tulis = csv.DictWriter(y, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(koleksi)

# MENGUBAH MONGODB MENJADI MYSQL=====================================================
import pymongo
x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['avengers']
col = db['teams']
koleksi = []
data = (list(col.find()))
for i in data:
    hasil = ({'_id': str(i['_id']), 'id' : i['id'], 'title' : i['title'], 'usia' : i['usia'], 'kota' : i['kota']})
    koleksi.append(tuple(hasil.values()))
querydb = (''' insert into avengersss (
    _id, id, title, usia, kota) values(
        %s,%s,%s,%s,%s) ''')
kursor.executemany(querydb,koleksi)
dbku.commit()