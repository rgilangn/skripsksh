from mininet.log import setLogLevel
from mininet.cli import CLI 
from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.link import TCLink
from mininet.node import CPULimitedHost
import os
import time
import subprocess

def mainTopo():
    #Define Initial Topology on Mininet
    os.system('mn -c')

    net = Mininet(link=TCLink, host=CPULimitedHost)
    net.start()

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

    #Starting Scenatrio
    print('=================STARTING SCENARIO 1 (Various Queue)=======================')
    print('===========================================================================')
    Cl1.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    Se2.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    ccName = subprocess.check_output('cat /proc/sys/net/ipv4/tcp_congestion_control', shell=True)
    print('===========================================================================')

    net.pingAll()
    print('===========================================================================')

    Se2.cmd('iperf -s  &')
    print('                          Server Iperf Started')
    print('=========================================================================')
    ####    STARTING EXAMINE    ####
    print('                TCPDUMP Started Longlived for 65 s Please Wait')
    print('                              Iperf Started')
    Cl1.cmd('tcpdump -G 62 -W 1 -w /home/reghn/Documents/testdumpLL.pcapng -i Cl1-eth0 &')
    Cl1.cmd('iperf -c 192.168.2.2 -t 60 -i 1 > /home/reghn/Documents/testperfLL.txt &')
    Cl1.cmd('ping 192.168.2.2 -c 65 > /home/reghn/Documents/testpingLL.txt ')
    #### rename file ####
    os.system('mv /home/reghn/Documents/testdumpLL.pcapng /home/reghn/Documents/testdumpLL'+str(ccName)+'')
    os.system('mv /home/reghn/Documents/testperfLL.txt /home/reghn/Documents/testperfLL'+str(ccName)+'')
    os.system('mv /home/reghn/Documents/testpingLL.txt /home/reghn/Documents/testpingLL'+str(ccName)+'')
    print('=========================================================================')
    
    Se2.cmd('python -m SimpleHTTPServer &')
    print('                          Python HTTP Server Start')
    print('=========================================================================')
    Cl1.cmd('tcpdump -G 5 -W 1 -w /home/reghn/Documents/testdumpSL.pcapng -i Cl1-eth0 &')
    print('                TCPDUMP Shortlived Started for 5 s Please Wait')
    Cl1.cmdPrint('wget 192.168.2.2:8000')
    

    os.system('scrot rest'+str(ccName)+'')
    os.system('mv /home/reghn/Documents/testdumpSL.pcapng /home/reghn/Documents/testdumpSL'+str(ccName)+'')
    print('=========================================================================')


    CLI(net)
    net.stop()

if __name__ =='__main__':
    setLogLevel('info')
    mainTopo()