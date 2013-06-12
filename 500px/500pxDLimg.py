"""
dumpimages.py
    Downloads all the images on the supplied URL, and saves them to the
    specified output file ("/result/" by default)

Usage:
    python DLimg.py http://example.com/ [output]
"""


from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, urlunparse 

import urllib.request
import os
import sys
website = "http://500px.com"
searchingURL = "http://500px.com/search?q="

def main(searched, out_folder="./result/"):
    url = searchingURL + searched
    print(url)
    soup = get_soup(url);
    parsed = list(urlparse(url))
    
    count = 0
    #mydivs = soup.find("div", { "class" : "stylelistrow" })
    
    photos =  soup.findAll(False, "photo")
    for photo in photos:
        photo_soup = go_on_photo(photo)
        photo_show = photo_soup.find("div", {"id": "thephoto"})
        line = photo_show('a')
        photo_href = line[0]['href']
        print(photo_href)
        fileName = photo_href.split("/")[-1]
        outpath = os.path.join(out_folder, fileName)
        fileName, fileExtension = os.path.splitext(outpath)
        count=count+1
        fileName = fileName + "_" + str(count) + fileExtension
        print("filename:"+fileName)        
        urllib.request.urlretrieve(photo_href , fileName)
        print("here")
    """
    for image in soup.findAll("img"):
        fileName = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        #print(parsed)        
        outpath = os.path.join(out_folder, fileName)
        fileName, fileExtension = os.path.splitext(outpath)
        count=count+1
        fileName = fileName + "_" + str(count) + fileExtension
        print(fileName)
        if image["src"].lower().startswith("http"):
            urllib.request.urlretrieve(image["src"] , fileName)
        else:
            urllib.request.urlretrieve(urlunparse(parsed), fileName)
    """
def _usage():
    print ("usage: python 500pxDLimg.py word")

def get_soup(url):
    soup = bs(urllib.request.urlopen(url))
    return soup
	
def go_on_photo(photo):
 ##   print(photo)
    links = photo('a')
    href = links[0]['href']
    print("Getting Soup:" + website + href)
    photo_soup = get_soup(website + href);
    return photo_soup
    
	
if __name__ == "__main__":
    if not(len( sys.argv) == 2):
        _usage()
    url = sys.argv[-1]
    out_folder = "./result/"
    if not os.path.exists(out_folder): os.makedirs(out_folder)    
    """if not url.lower().startswith("http"):
        out_folder = sys.argv[-1]
        url = sys.argv[-2]
        if not url.lower().startswith("http"):
            _usage()
            sys.exit(-1)
    """
    main(url, out_folder)