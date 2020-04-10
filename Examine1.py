from mininet.log import setLogLevel
from mininet.cli import CLI 
from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.link import TCLink
from mininet.node import CPULimitedHost
import os


def mainTopo():
    os.system('mn -c')
    net = Mininet(link=TCLink, host=CPULimitedHost)

    Cl1 = net.addHost('Cl1', ip='192.168.1.2/29')
    Se2 = net.addHost('Se2', ip='192.168.2.2/29')
    Ro1 = net.addHost('Router1')

    net.addLink(Cl1, Ro1, bw=100)
    net.addLink(Se2, Ro1, bw=100)

    net.build()

    Ro1.cmd('ifconfig Router1-eth0 0')
    Ro1.cmd('ifconfig Router1-eth1 0')

    Ro1.cmd('ifconfig Router1-eth0')
    Ro1.cmd('ifconfig Router1-eth1')

    Ro1.cmd('ifconfig Router1-eth0 hw ether mac=00:00:00:00:02:01')
    Ro1.cmd('ifconfig Router1-eth1 hw ether mac=00:00:00:00:02:02')

    Ro1.cmd("ip addr add 192.168.1.1/29 brd + dev Router1-eth0")
    Ro1.cmd("ip addr add 192.168.2.1/29 brd + dev Router1-eth1")
    Ro1.cmd('sysctl -w net.ipv4.ip_forward=1')

    Cl1.cmd('ip route add default via 192.168.1.1')
    Se2.cmd('ip route add default via 192.168.2.1')

    print('======================STARTING SCENARIO 1 (NORMAL)============================')
    print('=================================================================================')
    Cl1.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    Se2.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    print('=================================================================================')
    
    net.pingAll() #examine connection
    print('=================================================================================')
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> editing Examines files

    #Cl1.cmdPrint('ping 192.168.1.1 -c 20 > testx.txt')
    print('                             Server Iperf Started')
    Se2.cmd('iperf -s &')
<<<<<<< HEAD
=======
    Se2.cmd('iperf -s -i 1 > ~/dataResult/iperf-serverSide.txt &')
    Se2.cmdPrint('echo iperf started')
    #Cl1.cmdPrint('ping 192.168.1.1 -c 20 > testx.txt')
    
>>>>>>> modify main examine file and add new results folder
=======
>>>>>>> editing Examines files
    CLI(net)
    net.stop()

if __name__ =='__main__':
    setLogLevel('info')
    mainTopo()
    
    
    
