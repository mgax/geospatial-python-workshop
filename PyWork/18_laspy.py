import laspy
import laspy.file as File
workspaceVector = "/home/instructor/Desktop/Data/Text/";
lasFile = workspaceVector + "sample.las"

infile = laspy.file.File(lasFile, mode="r")

point_records = infile.points
#number of points
print len(point_records)
#point format
#pointFormat = infile.point_format
#for spec in pointFormat:
#    print spec.name

#color data
#print infile.blue


#Lets take a look at the header also.
#headerformat = infile.header.header_format
#for spec in headerformat:
#    print(spec.name)


#import matplotlib.pyplot as plt
#plt.hist(infile.intensity)
#plt.title("Histogram of the Intensity Dimension")
#plt.show()
