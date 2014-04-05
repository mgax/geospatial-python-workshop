from pyproj import  Proj
import csv
stereo70 = Proj(init='epsg:31700')
#vaci_total = 0


def process_localitate(line):
    judet = line['judet']
    if judet == 'Cluj':
        #vaci_total += int(line['oi'])
        xy = line['xy']
        x, y = xy.split(',')
        x = int(x)
        y = int(y)
        lat, lng = stereo70(x, y, inverse=True)
        print [lat, lng]



f = open('localitati.csv')
csv_file = csv.DictReader(f)
for l in csv_file:
    process_localitate(l)


#print vaci_total
