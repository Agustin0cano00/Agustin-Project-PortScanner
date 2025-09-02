import socket
from common_ports import ports_and_services


def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Resolver target a IP
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        # Si es dominio inválido
        if not target.replace(".", "").isdigit():
            return "Error: Invalid hostname"
        else:
            return "Error: Invalid IP address"

    # Intentar obtener el hostname si es una IP válida
    hostname = None
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except Exception:
        pass

    # Escaneo de puertos
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    # Modo Verbose
    if verbose:
        if hostname and not target.replace(".", "").isdigit():
            result_str = f"Open ports for {target} ({ip})\n"
        elif hostname:
            result_str = f"Open ports for {hostname} ({ip})\n"
        else:
            result_str = f"Open ports for {ip}\n"

        result_str += "PORT     SERVICE\n"
        for port in open_ports:
            service = ports_and_services.get(port, "unknown")
            result_str += f"{port:<9}{service}\n"
        return result_str.strip()

    return open_ports
