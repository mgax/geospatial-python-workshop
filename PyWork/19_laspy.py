import laspy.file as las_file
import PIL.Image as Image
import sys
import numpy as np
import struct

workspaceVector = "/home/instructor/Desktop/Data/Text/";
lasFile = workspaceVector + "sample.las"



RESOLUTION = (512, 512)
DECIMATION_FACTOR = 10


#read las file
f = las_file.File(lasFile, mode="r")


#decimate
print "decimating by factor {0}".format(DECIMATION_FACTOR)
vx = f.x.astype(np.float32)[::DECIMATION_FACTOR]
vy = f.y.astype(np.float32)[::DECIMATION_FACTOR]
vz = f.z.astype(np.float32)[::DECIMATION_FACTOR]


#normalize each dimension
print "normalizing dimensions"
x_min, x_max = min(vx), max(vx)
y_min, y_max = min(vy), max(vy)
z_min, z_max = min(vz), max(vz)
vx = (vx - x_min) / (x_max - x_min)
vy = (vy - y_min) / (y_max - y_min)
vz = (vz - z_min) / (z_max - z_min)


#create image for heightmap
print "allocating image buffer"
img = Image.new("L", RESOLUTION, 0)
img_buff = img.load()

#splat heigth data
num_points = len(vx)
progress_steps = num_points/200
for i in range(num_points):
    x = int(vx[i] * (RESOLUTION[0]-1))
    y = int(vy[i] * (RESOLUTION[1]-1))
    z = int(vz[i] * 254)
    if img_buff[x,y] == 0:
        img_buff[x,y] = z

    if i % progress_steps == 100:
        percentage = int( float(i*100)/num_points )
        sys.stdout.write( "\rsplatting height data: {0:d}% ".format(percentage+1))
        sys.stdout.flush()


img.save("/home/instructor/Desktop/heightmap.png")