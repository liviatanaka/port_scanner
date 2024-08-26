import socket
from pydantic import BaseModel
import pandas as pd
import threading
from concurrent.futures import ThreadPoolExecutor

class ScanIn(BaseModel):
    host: str
    start_port: int
    end_port: int

class Scanner:

    def __init__(self):
        self.well_known_ports = pd.read_csv("service-names-port-numbers.csv", index_col="Port Number").to_dict()["Description"]
        self.well_known_ports = {k: v for k, v in self.well_known_ports.items() if type(v) == str}
        self.lock = threading.Lock() 

    def scan_ports(self, host, host_port, start_port, end_port):
        response = {
            "host": host,
            "host_ip": host_port
        }

        open_ports = {}

        def scan(host_, port_):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  
            result = sock.connect_ex((host_, port_))

            if result == 0:
                with self.lock:  
                    if str(port_) in self.well_known_ports:
                        open_ports[port_] = self.well_known_ports[str(port_)]

                    else:
                        open_ports[port_] = "unknown"
                    print(f"Port {port_}: Open - {open_ports[port_]}")
            else:
                print(f"Port {port_}: Closed")
            sock.close()

        # with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            # executor.submit(scan, response["host_ip"], port)
            scan(host_port, port)

        response["open_ports"] = open_ports

        return response
