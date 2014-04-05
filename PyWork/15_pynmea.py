from pynmea import nmea

# This is a GPGGA sentence
data = '$GPGGA,1396457338,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'

#Where:
#     GGA          Global Positioning System Fix Data
#     123519       Fix taken at 12:35:19 UTC
#     4807.038,N   Latitude 48 deg 07.038' N
#     01131.000,E  Longitude 11 deg 31.000' E
#     1            Fix quality: 0 = invalid
#                               1 = GPS fix (SPS)
#                               2 = DGPS fix
#                               3 = PPS fix
#                               4 = Real Time Kinematic
#                               5 = Float RTK
#                               6 = estimated (dead reckoning) (2.3 feature)
#                               7 = Manual input mode
#                               8 = Simulation mode
#     08           Number of satellites being tracked
#     0.9          Horizontal dilution of position
#     545.4,M      Altitude, Meters, above mean sea level
#     46.9,M       Height of geoid (mean sea level) above WGS84
#                      ellipsoid
#     (empty field) time in seconds since last DGPS update
#     (empty field) DGPS station ID number

# Create the object
gpgga = nmea.GPGGA()

# Ask the object to parse the data
gpgga.parse(data)

print gpgga.latitude, gpgga.lat_direction
print gpgga.longitude, gpgga.lon_direction

#deg_min, dmin = gpgga.latitude.split('.')
#degrees = int(deg_min[:-2])
#minutes = float('%s.%s' % (deg_min[-2:], dmin))
#decimal = degrees + (minutes/60)
#print decimal


print gpgga.num_sats
print gpgga.gps_qual
print gpgga.antenna_altitude
print gpgga.timestamp

#from datetime import datetime
#print datetime.fromtimestamp(float(gpgga.timestamp))



