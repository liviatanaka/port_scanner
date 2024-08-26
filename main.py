from fastapi import FastAPI, HTTPException
from scanner import Scanner, ScanIn
import socket


app = FastAPI()

# fastapi dev main.py
scanner = Scanner()

@app.post("/scan/host")
async def scan_host(input: ScanIn):
    print(input)
    try:
        host_port = socket.gethostbyname(input.host)
    except:
        raise HTTPException(status_code=400, detail="Invalid host")
    
    results = scanner.scan_ports(input.host, host_port, input.start_port, input.end_port)
    return results

@app.post("/scan/ip")
async def scan_ip(input: ScanIn):

    results = scanner.scan_ports("", input.host, input.start_port, input.end_port)
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)