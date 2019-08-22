import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_excel('latihan.xls', header=3,skipfooter=2,na_values='-')
data1.rename(columns={'Unnamed: 0':'Provinsi'}, inplace=True)
data1.dropna()
data2 = pd.read_excel('latihan.xls', header=3,skipfooter=3,na_values='-')
data2.rename(columns={'Unnamed: 0':'Provinsi'}, inplace=True)
data2.dropna()

dataIndonesia = data1.iloc[[33],1:]
thIndonesia = list(dataIndonesia.columns)
jmlIndonesia = list(dataIndonesia.values[0])[:]

dataTerkecil = data1[data1[1971] == data1[1971].min()]
thDataTerkecil = list(dataTerkecil.columns)[1:]
jmlDataTerkecil = list(dataTerkecil.values[0])[1:]

dataTerbesar = data2[data2[2000] == data2[2000].max()]
thDataTerbesar = list(dataTerbesar.columns)[1:]
jmlDataTerbesar = list(dataTerbesar.values[0])[1:]

plt.plot(
    thIndonesia,jmlIndonesia,'r-',
    thDataTerkecil,jmlDataTerkecil,'g-',
    thDataTerbesar,jmlDataTerbesar,'b-')
plt.grid(True)
plt.legend(['Jumlah Penduduk Indonesia Tiap Tahun','Jumlah Penduduk Tiap Tahun dimana Jumlah Penduduk ditahun 1971 Terkecil','Jumlah Penduduk Tiap Tahun dimana Jumlah Penduduk ditahun 2000 Terbesar'])
plt.show()