import subprocess
import os
import threading
import psutil
import socket

def launch(ram,path):
    bat = path+"\launch.bat"
    f = open(bat,'w')
    amount = ram.strip()
    f.write("cd /D " + path + "\n")
    f.write("java -Xmx"+amount+"G -jar server.jar\n")
    f.write("exit")
    f.close()
    print("hey")
    def first_launch():
        subprocess.call([bat])
        print("dziala")
    def kill():
        PROCNAME = "java.exe"
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()
    def start():
        threading.Thread(target=first_launch).start()
        while(True):
            if(os.path.exists(path+"\server.properties")):
                kill()
                break
    start()
    #eula
    if (os.path.exists(path+"\eula.txt")):
        lines = open(path+"\eula.txt",'r+').readlines()
        lines[-1] = "eula=true\n"
        open(path+"\eula.txt",'r+').writelines(lines)
def setProperties(name,difficulty,maxPlayers,pvp,monsters,online,path):
    #get local_ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    ip = "server-ip="+str(ip)+"\n"
    #server.properties
    lines = open(path+"\server.properties",'r+').readlines()
    options = {
        "server-ip=\n":ip,
        "motd=A Minecraft Server\n":"motd="+name+"\n",
        "difficulty=easy\n":"difficulty="+difficulty+"\n",
        "max-players=20\n":"max-players="+maxPlayers+"\n",
        "allow-flight=false\n":"allow-flight="+pvp+"\n",
        "spawn-monsters=true\n":"spawn-monsters="+monsters+"\n",
        "online-mode=true\n":"online-mode="+online+"\n",
        "enable-rcon=false\n":"enable-rcon=true\n"
    }
    print(options)
    for i in range(len(lines)):
        for key in options:
            if(key==lines[i]):
                lines[i]=options[key]
    print(lines)
    open(path+"\server.properties",'r+').writelines(lines)