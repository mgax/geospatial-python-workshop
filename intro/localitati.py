import csv
from pyproj import Proj

stereo70 = Proj(init='epsg:31700')

for line in csv.DictReader(open('localitati.csv')):
    if line['judet'] == 'CJ':
        (x, y) = line['xy'].split(',')
        (lat, lng) = stereo70(int(x), int(y), inverse=True)
        print '%.2f' % lat, '%.2f' % lng, line['nume']
