import csv
import numpy as np
import matplotlib.pyplot as plt

provinsi = []
tahun2015 = []
tahun2016 = []
with open('Persentase Perokok Ri.csv','r') as data:
    baca = csv.DictReader(data)
    for i in baca:
       provinsi.append(dict(i)['Provinsi'])
       tahun2015.append(float(dict(i)['2015']))
       tahun2016.append(float(dict(i)['2016']))

x = np.array(provinsi)
y = np.array(tahun2015)
z = np.array(tahun2016)

# Diagram Garis=========================================================================

plt.subplot(5,1,3)
plt.plot(x,y,'k.')
plt.xticks(x,x,rotation='vertical')
plt.plot(x,y, 'r--',label='2015')
plt.grid(True)
plt.xlabel('Provinsi')
plt.ylabel('Jumlah dalam persen')
plt.title('Grafik Perokok tiap Provinsi')
plt.legend()

plt.subplot(5,1,3)
plt.plot(x,z,'r.')
plt.xticks(x,x,rotation='vertical')
plt.plot(x,z, 'k--',label='2016')
plt.grid(True)
plt.xlabel('Provinsi')
plt.ylabel('Jumlah dalam persen')
plt.legend()

plt.show()

# Diagram Bar============================================================================

label = np.arange(len(x))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(label - width/2, y, width, label='2015')
rects2 = ax.bar(label + width/2, z, width, label='2016')
ax.set_ylabel('Nilai Perokok Tiap Provinsi')
ax.set_title('Presentase Perokok Tiap Provinsi')
ax.set_xticks(label)
ax.set_xticklabels(x,rotation='vertical')
ax.legend()
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x()+rect.get_width()/2,height),
                    xytext=(0,3),
                    textcoords='offset points',
                    ha='center',va='bottom')
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()


