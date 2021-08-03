import requests
import re
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets

versions = []
URL = "https://mcversions.net"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

wyniki = soup.find_all(class_="text-xl leading-snug font-semibold")
for i in wyniki:
    line = str(i)
    line2 = str(i)
    line = re.search(r'</span>(.*?)<br/>',line)
    if(line):
        versions.append(str(line.group(1)))
    else:
        line2 = re.search(r'>(.*?)<br/>', line2)
        if(str(line2.group(1))=="b1.8.1"):
            break
        endVersion = str(line2.group(1))
        endVersion.replace(" ","-")
        versions.append(endVersion)


def addToBox(object):
    for i in versions:
        object.addItem(i)