

import socket
import subprocess

def internet(host="8.8.8.8", port = 53, timeout = 3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host,port))
        return  True
    except Exception as ex:
        print(ex)
        return False

try:
    import docx
except Exception as ex:
    print(ex)
    if internet():
        subprocess.run([ "pip" , "install","--user", "docx"])
