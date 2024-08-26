import socket
from pydantic import BaseModel
import pandas as pd
import multiprocessing

class ScanIn(BaseModel):
    host: str
    start_port: int
    end_port: int

class Scanner:

    def __init__(self):
        self.well_known_ports = pd.read_csv("wellKnownPorts.csv", index_col="port").to_dict()["service"]

    

    def scan_ports(self, host, host_port, start_port, end_port):

        print(f"Scanning ports on {host}...")

        response = {
            "host": host,
            "host_ip": host_port
        }

        open_ports = {}
        closed_ports = []

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a connection timeout

            result = sock.connect_ex((host_port, port))

            if result == 0:
                if int(port) in self.well_known_ports:
                    open_ports[port] = self.well_known_ports[port]
                else:
                    open_ports[port] = "unknown"
            else:
                closed_ports.append(port)

            sock.close()
        
        response["open ports"] = open_ports
        response["closed ports"] = closed_ports
        
        return response