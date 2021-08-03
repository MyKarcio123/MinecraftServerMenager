import requests
import re
import os
from pathlib import Path
from firstLaunch import launch
from bs4 import BeautifulSoup

def downoland(version,path):
    path = path+"\\server.jar"
    print(path)
    URL = "https://mcversions.net/download/"+version
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    button = soup.find(class_="text-xs whitespace-nowrap py-3 px-8 bg-green-700 hover:bg-green-900 rounded text-white no-underline font-bold transition-colors duration-200")
    button = str(button)
    link = re.search(r'href=\"(.*?)\"',button).group(1)
    r = requests.get(link, allow_redirects=True)
    if not (os.path.exists("files")):
        os.mkdir("files")
    open(path, 'wb').write(r.content)
    fname = Path(path)
    while(True):
        if(fname.exists()):
            return True