import port_scanner

# Caso 1: rango de puertos normal
print(port_scanner.get_open_ports("scanme.nmap.org", [20, 80]))
print()

# Caso 2: rango de puertos normal en verbose
print(port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True))
print()

# Caso 3: dominio inválido
print(port_scanner.get_open_ports("notarealdomain.abc", [20, 80]))
print()

# Caso 4: IP inválida
print(port_scanner.get_open_ports("256.256.256.256", [20, 80]))
