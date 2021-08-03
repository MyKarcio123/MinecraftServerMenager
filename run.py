from database import getPath
import os
import threading
import subprocess

def run(object):
    path = getPath(object)
    print(path)
    path = path + "\launch.bat"
    def launch():
        subprocess.call([path])
    threading.Thread(target=launch).start()