import socket

def port_scan(*args):
    if not args:
        print("Usage: port-scan <host> [start_port-end_port]")
        return

    host = args[0]

    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Invalid host: {host}")
        return

    start_port = 1
    end_port = 100000
    if len(args) > 1 and "-" in args[1]:
        try:
            start_port, end_port = map(int, args[1].split("-"))
        except ValueError:
            print("Invalid port range, using default 1-1024")

    print(f"Scanning {host} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
