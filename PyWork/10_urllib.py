import urllib

url = "http://127.0.0.1/data/judete.csv"
judete = urllib.urlopen(url)

print judete.readline()
print judete.readline()
print judete.readline()

