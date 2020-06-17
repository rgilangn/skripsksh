from mininet.log import setLogLevel
from mininet.cli import CLI 
from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.link import TCLink
from mininet.node import CPULimitedHost
import os
import time
import subprocess

maxQ = 0

def mainTopo():
    #Define Initial Topology on Mininet
    os.system('mn -c')
    print('===========================================================================')
    print('===========================================================================')
    net = Mininet(link=TCLink, host=CPULimitedHost)
    net.start()

    Cl1 = net.addHost('Cl1', ip='192.168.1.2/24')
    Cl2 = net.addHost('Cl2', ip='192.168.1.4/24')
    Cl3 = net.addHost('Cl3', ip='192.168.1.6/24')
    Cl4 = net.addHost('Cl4', ip='192.168.1.8/24')
    Cl5 = net.addHost('Cl5', ip='192.168.1.10/24')
    Cl6 = net.addHost('Cl6', ip='192.168.1.12/44')
    Cl7 = net.addHost('Cl7', ip='192.168.1.14/24')
    Cl8 = net.addHost('Cl8', ip='192.168.1.16/24')

    Se1 = net.addHost('Se2', ip='192.168.2.2/24')
    Se2 = net.addHost('Se2', ip='192.168.2.4/24')
    Se3 = net.addHost('Se2', ip='192.168.2.6/24')
    Se4 = net.addHost('Se2', ip='192.168.2.8/24')
    Se5 = net.addHost('Se2', ip='192.168.2.10/24')
    Se6 = net.addHost('Se2', ip='192.168.2.12/24')
    Se7 = net.addHost('Se2', ip='192.168.2.14/24')
    Se8 = net.addHost('Se2', ip='192.168.2.16/24')
    Ro1 = net.addHost('Router1')

    net.addLink(Cl1, Ro1, bw=1)
    net.addLink(Se2, Ro1, bw=100) #, max_queue_size = maxQ


    net.build()

    Ro1.cmd('ifconfig Router1-eth0 0')
    Ro1.cmd('ifconfig Router1-eth1 0')
    Ro1.cmd('ifconfig Router1-eth2 0')
    Ro1.cmd('ifconfig Router1-eth3 0')
    Ro1.cmd('ifconfig Router1-eth4 0')
    Ro1.cmd('ifconfig Router1-eth5 0')
    Ro1.cmd('ifconfig Router1-eth6 0')
    Ro1.cmd('ifconfig Router1-eth7 0')

    Ro1.cmd('ifconfig Router1-eth8 0')
    Ro1.cmd('ifconfig Router1-eth9 0')
    Ro1.cmd('ifconfig Router1-eth10 0')
    Ro1.cmd('ifconfig Router1-eth11 0')
    Ro1.cmd('ifconfig Router1-eth12 0')
    Ro1.cmd('ifconfig Router1-eth13 0')
    Ro1.cmd('ifconfig Router1-eth14 0')
    Ro1.cmd('ifconfig Router1-eth15 0')

    Ro1.cmd('ifconfig Router1-eth0')
    Ro1.cmd('ifconfig Router1-eth1')
    Ro1.cmd('ifconfig Router1-eth2')
    Ro1.cmd('ifconfig Router1-eth3')
    Ro1.cmd('ifconfig Router1-eth4')
    Ro1.cmd('ifconfig Router1-eth5')
    Ro1.cmd('ifconfig Router1-eth6')
    Ro1.cmd('ifconfig Router1-eth7')

    
    Ro1.cmd('ifconfig Router1-eth8')
    Ro1.cmd('ifconfig Router1-eth9')
    Ro1.cmd('ifconfig Router1-eth10')
    Ro1.cmd('ifconfig Router1-eth11')
    Ro1.cmd('ifconfig Router1-eth12')
    Ro1.cmd('ifconfig Router1-eth13')
    Ro1.cmd('ifconfig Router1-eth14')
    Ro1.cmd('ifconfig Router1-eth15')

    Ro1.cmd('ifconfig Router1-eth0 hw ether mac=00:00:00:00:02:01')
    Ro1.cmd('ifconfig Router1-eth1 hw ether mac=00:00:00:00:02:02')
    Ro1.cmd('ifconfig Router1-eth2 hw ether mac=00:00:00:00:02:03')
    Ro1.cmd('ifconfig Router1-eth3 hw ether mac=00:00:00:00:02:04')
    Ro1.cmd('ifconfig Router1-eth4 hw ether mac=00:00:00:00:02:05')
    Ro1.cmd('ifconfig Router1-eth5 hw ether mac=00:00:00:00:02:06')
    Ro1.cmd('ifconfig Router1-eth6 hw ether mac=00:00:00:00:02:07')
    Ro1.cmd('ifconfig Router1-eth7 hw ether mac=00:00:00:00:02:08')
    Ro1.cmd('ifconfig Router1-eth8 hw ether mac=00:00:00:00:02:09')
    Ro1.cmd('ifconfig Router1-eth9 hw ether mac=00:00:00:00:02:10')
    Ro1.cmd('ifconfig Router1-eth10 hw ether mac=00:00:00:00:02:11')
    Ro1.cmd('ifconfig Router1-eth11 hw ether mac=00:00:00:00:02:12')
    Ro1.cmd('ifconfig Router1-eth12 hw ether mac=00:00:00:00:02:13')
    Ro1.cmd('ifconfig Router1-eth13 hw ether mac=00:00:00:00:02:14')
    Ro1.cmd('ifconfig Router1-eth14 hw ether mac=00:00:00:00:02:15')
    Ro1.cmd('ifconfig Router1-eth15 hw ether mac=00:00:00:00:02:16')

    Ro1.cmd("ip addr add 192.168.1.1/29 brd + dev Router1-eth0")
    Ro1.cmd("ip addr add 192.168.1.3/29 brd + dev Router1-eth1")
    Ro1.cmd("ip addr add 192.168.1.5/29 brd + dev Router1-eth2")
    Ro1.cmd("ip addr add 192.168.1.7/29 brd + dev Router1-eth3")
    Ro1.cmd("ip addr add 192.168.1.9/29 brd + dev Router1-eth4")
    Ro1.cmd("ip addr add 192.168.1.11/29 brd + dev Router1-eth5")
    Ro1.cmd("ip addr add 192.168.1.13/29 brd + dev Router1-eth6")
    Ro1.cmd("ip addr add 192.168.1.15/29 brd + dev Router1-eth7")

    Ro1.cmd("ip addr add 192.168.2.2/29 brd + dev Router1-eth8")
    Ro1.cmd("ip addr add 192.168.2.4/29 brd + dev Router1-eth9")
    Ro1.cmd("ip addr add 192.168.2.6/29 brd + dev Router1-eth10")
    Ro1.cmd("ip addr add 192.168.2.8/29 brd + dev Router1-eth11")
    Ro1.cmd("ip addr add 192.168.2.10/29 brd + dev Router1-eth12")
    Ro1.cmd("ip addr add 192.168.2.12/29 brd + dev Router1-eth13")
    Ro1.cmd("ip addr add 192.168.2.14/29 brd + dev Router1-eth14")
    Ro1.cmd("ip addr add 192.168.2.16/29 brd + dev Router1-eth15")

    Ro1.cmd('sysctl -w net.ipv4.ip_forward=1')

    Cl1.cmd('ip route add default via 192.168.1.1')
    Cl2.cmd('ip route add default via 192.168.1.3')
    Cl3.cmd('ip route add default via 192.168.1.5')
    Cl4.cmd('ip route add default via 192.168.1.7')
    Cl5.cmd('ip route add default via 192.168.1.9')
    Cl6.cmd('ip route add default via 192.168.1.11')
    Cl7.cmd('ip route add default via 192.168.1.13')
    Cl8.cmd('ip route add default via 192.168.1.15')

    Se1.cmd('ip route add default via 192.168.2.1')
    Se2.cmd('ip route add default via 192.168.2.3')
    Se3.cmd('ip route add default via 192.168.2.5')
    Se4.cmd('ip route add default via 192.168.2.7')
    Se5.cmd('ip route add default via 192.168.2.9')
    Se6.cmd('ip route add default via 192.168.2.11')
    Se7.cmd('ip route add default via 192.168.2.13')
    Se8.cmd('ip route add default via 192.168.2.15')
    

    #Starting Scenatrio
    print('=================STARTING SCENARIO 1 (Various Queue)=======================')
    print('===========================================================================')
    Cl1.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    Se2.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    print("Queue Size : ", maxQ)
    
    ccName = subprocess.check_output('cat /proc/sys/net/ipv4/tcp_congestion_control', shell=True)
    ccName = ccName.replace("\n","")

    print('===========================================================================')

    net.pingAll()
    print('===========================================================================')

    Se2.cmd('iperf -s &')
    # Se2.cmd('iperf -s  > dataResult/examine3/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_iperf-server.txt &')
    print('                          Server Iperf Started')
    Se2.cmd('python -m SimpleHTTPServer &')
    print('                          Python HTTP Server Start')
    print('=========================================================================')
    ####    STARTING EXAMINE    ####
    print('                TCPDUMP Started Longlived for 65 s Please Wait')
    print('                              Iperf Started')
    Cl1.cmd('tcpdump -G 60 -W 1 -w /home/reghn/Documents/pcapngs/_LL_.pcapng -i Cl1-eth0 &') #62s
    Cl1.cmd('iperf -c 192.168.2.2 -t 60 -i 1 > dataResult/examine3/_LL_iperfRests.txt &') #60s
    Cl1.cmd('ping 192.168.2.2 -c 61 > dataResult/examine3/_LL_rttRests.txt &') #61s
    
    time.sleep(10)
    os.system('echo                TCPDUMP Shortlived Started for 10 s Please Wait')
    Cl1.cmdPrint('wget 192.168.2.2:8000')
    os.system('scrot --delay 2 restSL.png')


    # os.system('mv /home/reghn/Documents/pcapngs/_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_.pcapng')
    # os.system('mv dataResult/examine3/_LL_iperfRests.txt dataResult/examine3/'+str(ccName)+'_'+str(maxQ)+'mix_LL_iperfRests.txt')
    # os.system('mv dataResult/examine3/_LL_rttRests.txt dataResult/examine3/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_rttRests.txt')
    print('=========================================================================')
    
    
    
    print('=========================================================================')
    #Cl1.cmd('tcpdump -G 10 -W 1 -w /home/reghn/Documents/pcapngs/_SL_.pcapng -i Cl1-eth0 &')
    
    print("                         Processing all file's   ")
    
    #os.system('mv /home/reghn/Documents/pcapngs/_SL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_SL_.pcapng')
    # os.system('mv restSL.png restSL'+str(ccName)+'_'+str(maxQ)+'_SK1')
    print('=========================================================================')
    time.sleep(60)
    #CLI(net)
    net.stop()

def runAll():
    os.system('sysctl -w net.ipv4.tcp_congestion_control=cubic')
    mainTopo()
    os.system('sysctl -w net.ipv4.tcp_congestion_control=bbr')
    mainTopo()
    os.system('sysctl -w net.ipv4.tcp_congestion_control=ledbat')
    mainTopo()

if __name__ =='__main__':
    setLogLevel('info')
    
    maxq = [20, 200, 2000, 20000]
    for maxQ in maxq:
        runAll()
    