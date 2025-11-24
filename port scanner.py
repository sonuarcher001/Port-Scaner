import socket

# Simple Port Scanner

target = input("Enter the target IP address: ")

print(f"\nScanning ports on {target}...\n")

# List of common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 443]

for port in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # timeout after 1 secondh
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")

    else:
        print(f"Port {port} is CLOSED")
    
    s.close()
