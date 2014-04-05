import json

workspaceVector = "/home/instructor/Desktop/Data/Text/";
fileDownload = workspaceVector + "judete.geojson"

json_data=open(fileDownload)
data = json.load(json_data)
json_data.close()

print data["features"][0]["properties"]