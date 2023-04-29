import socket
import subprocess

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

# perform a basic ping test to check if network connection is available
def ping_test():
    hostname = "google.com"
    response = subprocess.run(["ping", "-n", "1", hostname], capture_output=True)
    if response.returncode == 0:
        return "Ping test successful. Network connection is available."
    else:
        return "Ping test failed. Network connection is not available."

# check if a specific port is open on a remote host
# def check_port(host, port):
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(3)
#         s.connect((host, port))
#         s.close()
#         return f"Port {port} is open on {host}."
#     except (socket.gaierror, socket.timeout, ConnectionRefusedError):
#         return f"Port {port} is not open on {host}."


def network_ports():
    # Execute the "netstat" command and store the output in the "result" variable
    result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True)

    # Create a dictionary to store the status of each port
    open_ports=[]
    close_ports=[]
    # Split the output into lines and check the status of each port
    for line in result.stdout.splitlines():
        if "LISTENING" in line:
            port = line.split()[-1]
            open_ports.append(int(port))
        elif "ESTABLISHED" in line:
            port = line.split()[-1]
            open_ports.append(int(port))
        elif "TIME_WAIT" in line:
            port = line.split()[1].split(":")[-1]
            close_ports.append(int(port))

    # Print out the status of each port
    # for port, status in port_status.items():
    #     print("Port {}: {}".format(port, status))

    # Check if there are any open ports
    # if len(port_status) == 0:
    #     print("There are no open ports on this computer.")
    # else:
    #     print("There are open ports on this computer.")

    # Check if the network has issues
    if "ESTABLISHED" not in result.stdout:
        check = {
            "open":open_ports,
            "close":close_ports,
            "msg":"The network may have issues."
        }
    else:
        check = {
            "open":open_ports,
            "close":close_ports,
            "msg":"The network may have issues."
        }

    return check

