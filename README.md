# Purpose
This project aims to provide some tools to write test suites for network firewalls.

Imagine an office network separated into several subnets all connected through a router firewalling according to the purpose of these networks.
It can be really easy to mess up with firewall rules and unintentionally allow clients in the guest subnet access to protected resources. 

Writing a testsuite can help to have a good amount of confidence on firewall changes.


# Local run


    python setup.py -r requirements.txt
    python setup.py install

# Installation

    pip install netunit
    
# Upload to PyPi

Run from project root:

    python setup.py -r requirements-dev.txt
    ./publish.sh 

# Usage
    
    from netunit import NetworkTestCase
    from ipaddress import ip_network
    
    class MyNetworkTests(NetworkTestCase):
        network = ip_network("192.168.179.0/24")
        
        def test_router_webinterface_access(self):
            self.assertReachable(ip_address("192.168.178.1"), 443)
    
        def test_switching_hardware_access(self):
            self.assertNotReachable(ip_address("192.168.10.2"), 443)
