import urllib

workspaceVector = "/home/instructor/Desktop/Data/";
fileDownload = workspaceVector + "judeteCSV.csv"
url = "http://127.0.0.1/data/judete.csv"

urllib.urlretrieve(url,fileDownload)
