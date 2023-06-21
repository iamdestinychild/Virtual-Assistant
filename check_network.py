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


# def ping_test(host):
#     try:
#         # Check if the host is reachable by attempting to resolve its IP address
#         ip_address = socket.gethostbyname(host)
#         if ip_address == '127.0.0.1':
#             # The host is the loopback address, indicating the local machine
#             return 0

#         # Ping the host
#         latency = ping3.ping(ip_address)
#         if latency is not None:
#             return latency
#         else:
#             return -1
#     except (ping3.errors.PingError, socket.gaierror):
#         return -1

def ping_test(host):
    try:
        ip_address = socket.gethostbyname(host)
        if ip_address == '127.0.0.1':
            return 0

        latency = ping3.ping(ip_address)
        if latency is not None:
            return latency
        else:
            return -1
    except (ping3.errors.PingError, socket.gaierror):
        return -1
    except UnicodeError as e:
        return -1
