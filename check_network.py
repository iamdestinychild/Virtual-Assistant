import socket
import subprocess
import ping3
from threading import Thread

# get the local IP address of the computer
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except socket.error:
        ip_address = "Unable to get local IP address"
    finally:
        s.close()
    return ip_address

def ping_test(host):
    try:
        latency = ping3.ping(host)
        if latency is not None:
            return latency
        else:
            return -1
    except ping3.errors.PingError:
        return -1
    