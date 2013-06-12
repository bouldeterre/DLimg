import urllib.request
from bs4 import BeautifulSoup
import os

page = urllib.request.urlopen("http://www.google.com")
soup = BeautifulSoup(page)

out_folder = "./test/"
filename = "http://91.121.132.199/SeriousO/News/Ban/1349748407bannierePost3.png".split("/")[-1]
outpath = os.path.join(out_folder, filename)
print(outpath)

urllib.request.urlretrieve("http://91.121.132.199/SeriousO/News/Ban/1349748407bannierePost3.png", outpath)