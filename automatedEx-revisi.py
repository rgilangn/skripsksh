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

optlinkWifi = {'bw':100,'delay':'25ms','loss':0.2}
optlink3G = {'bw':100, 'delay':'100ms','loss':0.6}
optlink4G = {'bw':100,'delay':'50ms','loss':0.5}
optlinkWAN = {'bw':100,'delay':'45ms','loss':0.3}
optlinkLocal = {'bw':1, 'delay':'1ms'}

def mainTopo():

    #Define Initial Topology on Mininet
    print('===========================================================================')
    print('===========================================================================')
    os.system('mn -c')
    print('===========================================================================')
    print('===========================================================================')
    net = Mininet(link=TCLink, host=CPULimitedHost)
    net.start()

    Cl1 = net.addHost('Cl1', ip='192.168.1.2/29')
    Se2 = net.addHost('Se2', ip='192.168.2.2/29')
    Ro1 = net.addHost('Router1')
    

    net.addLink(Cl1, Ro1, **optlinkWifi)
    net.addLink(Se2, Ro1, **optlinkLocal) #, max_queue_size = X | max_queue_size = maxQ,

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
    print("Queue Size", maxQ)
    ccName = subprocess.check_output('cat /proc/sys/net/ipv4/tcp_congestion_control', shell=True)
    ccName = ccName.replace("\n","")

    print('===========================================================================')

    net.pingAll()
    print('===========================================================================')
    Se2.cmd('python -m SimpleHTTPServer &')
    print('                          Python HTTP Server Start')
    Se2.cmd('iperf -s  > dataResult/examine-X/'+str(ccName)+'_'+str(maxQ)+'_LL_iperf-server_Wifi.txt &')
    print('                          Server Iperf Started')
    print('=========================================================================')

    ####    STARTING EXAMINE    ####
    print('                TCPDUMP Started Longlived for 65 s Please Wait')
    print('                              Iperf Started')
    Cl1.cmd('tcpdump -G 32 -W 1 -w /home/reghn/Documents/pcapngs/_LL_.pcapng -i Cl1-eth0 &') #62s
    Cl1.cmd('iperf -c 192.168.2.2 -t 30 -i 1 > dataResult/examine-X/_LL_iperfRests.txt &') #60s
    Cl1.cmd('ping 192.168.2.2 -c 30 > dataResult/examine-X/_LL_rttRests.txt &') #61s

    print('=========================================================================')
    time.sleep(5)
    Cl1.cmdPrint('wget 192.168.2.2:8000 &')
    
    #### rename file ####    
    print('=========================================================================')
    print("                         Processing all file's   ")
    print('=========================================================================')
    os.system('mv /home/reghn/Documents/pcapngs/_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_LL_Wifi.pcapng')
    os.system('mv dataResult/examine-X/_LL_iperfRests.txt dataResult/examine-X/'+str(ccName)+'_'+str(maxQ)+'_LL_iperfRests_Wifi.txt')
    os.system('mv dataResult/examine-X/_LL_rttRests.txt dataResult/examine-X/'+str(ccName)+'_'+str(maxQ)+'_LL_rttRests_Wifi.txt')

    
    print('=========================================================================')
    time.sleep(45)
    # CLI(net)
    net.stop()
    print('==========================================================================')

    # run All program 
def runAll():
    os.system('sysctl -w net.ipv4.tcp_congestion_control=ledbat')
    mainTopo()
    os.system('sysctl -w net.ipv4.tcp_congestion_control=bbr')
    mainTopo()
    os.system('sysctl -w net.ipv4.tcp_congestion_control=cubic')
    mainTopo()
    # set congestion control algorithm

if __name__ =='__main__':
    setLogLevel('info')
    maxq = [20, 200, 2000, 20000]
    # for maxQ in maxq:
    #     runAll()
    runAll()
    
