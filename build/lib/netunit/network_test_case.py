from ipaddress import ip_network, ip_address

from unittest2 import TestCase

from util import tcp_probe, get_interface_for_network


class NetworkTestCase(TestCase):

    @property
    def network(self) -> ip_network:
        raise NotImplementedError("you need to define network property in your test class")

    @classmethod
    def setUpClass(cls):
        cls.interface_ip = get_interface_for_network(cls.network)

    def assertReachable(self, ip: ip_address, port: int):
        if not self.interface_ip:
            self.skipTest("no interface in this net")
        available = tcp_probe(self.interface_ip, ip, port)
        self.assertTrue(available, "{}:{} should be available but is not!".format(ip, port))

    def assertNotReachable(self, ip: ip_address, port: int):
        if not self.interface_ip:
            self.skipTest("no interface in this net")
        available = tcp_probe(self.interface_ip, ip, port)
        self.assertFalse(available, "{}:{} should not be available but it is!".format(ip, port))
