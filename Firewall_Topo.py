#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink

class MyTopology(Topo):
    """
    A basic topology
    """
    def __init__(self):
        Topo.__init__(self)

        # Set Up Topology Here
        switch1 = self.addSwitch('Switch1')    ## Adds a Switch
        switch2 = self.addSwitch('Switch2')    ## Adds a Switch
        switch3 = self.addSwitch('Switch3')    ## Adds a Switch

        User1 = self.addHost('User1')       ## Adds a Host
        User2 = self.addHost('User2')       ## Adds a Host
        Server1 = self.addHost('Server1')       ## Adds a Host
        Server2 = self.addHost('Server2')       ## Adds a Host
        Laptop = self.addHost('Laptop')       ## Adds a Host
        Ipad = self.addHost('Ipad')       ## Adds a Host
        Phone = self.addHost('Phone')       ## Adds a Host

        self.addLink(User1, switch1, delay='20ms')      ## Add a link
        self.addLink(User2, switch1, delay='20ms')      ## Add a link
        self.addLink(Laptop, switch1, delay='35ms')      ## Add a link
        self.addLink(switch1, switch2, delay='20ms')
 
        self.addLink(switch2, switch3, delay='20ms')     
        self.addLink(Phone, switch2, delay='20ms')     
        self.addLink(Ipad, switch2, delay='20ms')
	
        self.addLink(Server1, switch3, delay='20ms')     
        self.addLink(Server2, switch3, delay='50ms')     

if __name__ == '__main__':
    """
    If this script is run as an executable (by chmod +x), this is
    what it will do
    """

    topo = MyTopology()   		 ## Creates the topology
    net = Mininet( topo=topo, link=TCLink )   	 ## Loads the topology
    net.start()                      ## Starts Mininet

    # Commands here will run on the simulated topology
    CLI(net)

    net.stop()                       ## Stops Mininet
