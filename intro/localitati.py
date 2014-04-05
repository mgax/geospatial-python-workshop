import csv
from pyproj import Proj

stereo70 = Proj(init='epsg:31700')

vaci = 0
oi = 0
porci = 0
capre = 0
oameni = 0

vaci_total = 0
oi_total = 0

for line in csv.DictReader(open('localitati.csv')):
    if line['judet'] == 'Cluj':
        (x, y) = line['xy'].split(',')
        (lat, lng) = stereo70(int(x), int(y), inverse=True)
        print '%.2f' % lat, '%.2f' % lng, line['nume']
        vaci += int(line['vaci'])
        oi += int(line['oi'])
        porci += int(line['porci'])
        capre += int(line['capre'])
        oameni += int(line['oameni'])

    vaci_total += int(line['vaci'])
    oi_total += int(line['oi'])

print 'vaci_total:', vaci_total
print 'oi_total:', oi_total
print 'vaci:', vaci
print 'oi:', oi
print 'capre:', capre
print 'porci:', porci
print 'oameni:', oameni
