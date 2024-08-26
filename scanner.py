import socket
from pydantic import BaseModel
import pandas as pd
import threading

class ScanIn(BaseModel):
    host: str
    start_port: int
    end_port: int

class Scanner:

    def __init__(self):
        self.well_known_ports = pd.read_csv("wellKnownPorts.csv", index_col="port").to_dict()["service"]

    def scan_ports(self, host, host_port, start_port, end_port):
        response = {
            "host": host,
            "host_ip": host_port
        }

        open_ports = {}


        def scan(host_, port_):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a connection timeout
            result = sock.connect_ex((host_, port_))

            if result == 0:
                if port_ in self.well_known_ports:
                    open_ports[port_] = self.well_known_ports[port_]
                else:
                    open_ports[port_] = "unknown"


            sock.close()

        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan, args=(response["host_ip"], port))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        response["open_ports"] = open_ports

        return response
