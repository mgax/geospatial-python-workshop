LOCALITATI_URL = (
    'http://earth.unibuc.ro/geoserver/geospatial/ows'
    '?service=WFS&version=1.0.0&request=GetFeature'
    '&typeName=geospatial:romania_localitati&outputFormat=csv'
)

import csv
import requests
from pyproj import Proj

stereo70 = Proj(init='epsg:31700')

with open('localitati.csv', 'wb') as f:
    out = csv.DictWriter(f, ['judet', 'nume', 'xy'])
    out.writeheader()

    csv_lines = requests.get(LOCALITATI_URL, stream=True).iter_lines()
    for line in csv.DictReader(csv_lines):
        (x, y) = line['the_geom'].split('(')[1].split(')')[0].split()
        out.writerow({
            'judet': line['county_mn'],
            'nume': line['name'],
            'xy': '%s,%s' % (x, y),
        })
