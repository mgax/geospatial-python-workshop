import rasterio, subprocess

workspaceRater = "/home/instructor/Desktop/Data/Landsat/";
#inputFile = workspaceRater + 'B1-L-34-036.tif'
inputFile = workspaceRater + 'L-34-035.tif'

with rasterio.drivers():
    with rasterio.open(inputFile) as src:
        print(src.width, src.height)
        print(src.crs)
        print(src.transform)
        print(src.count)
        print(src.indexes)
        
with rasterio.drivers():
    rasterio.copy(
        inputFile,
        '/home/instructor/Desktop/example-total.jpg',
        driver='JPEG')
