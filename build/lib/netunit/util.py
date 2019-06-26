import socket
from ipaddress import ip_address, ip_network, ip_interface

import netifaces as netifaces


def tcp_probe(interface: ip_interface, destination_ip: ip_address, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    try:
        sock.bind((str(interface.ip), 0))
    except OSError as e:
        raise Exception("Could not bind source ip {} ({})".format(interface, e))

    sock.settimeout(1)

    try:
        if sock.connect_ex((str(destination_ip), port)) == 0:
            return True
        else:
            return False
    finally:
        sock.close()


def get_local_ips() -> [ip_interface]:
    addresses = map(lambda x: netifaces.ifaddresses(x), netifaces.interfaces())
    ips = [value[0]["addr"] for sublist in addresses for key, value in sublist.items() if key == 2]

    return list(map(lambda x: ip_interface(x), ips))


def get_interface_for_network(network: ip_network) -> ip_interface:
    for interface in get_local_ips():
        if interface in network:
            return interface

    return None

# print(get_ip_for_network(ip_network("192.168.178.0/24")))
