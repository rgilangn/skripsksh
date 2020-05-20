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

    Cl1 = net.addHost('Cl1', ip='192.168.1.2/29')
    Se2 = net.addHost('Se2', ip='192.168.2.2/29')
    Ro1 = net.addHost('Router1')

    net.addLink(Cl1, Ro1, bw=100)
    net.addLink(Se2, Ro1, bw=1, max_queue_size = maxQ) #, max_queue_size = maxQ


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
    print("Queue Size : ", maxQ)
    ccName = subprocess.check_output('cat /proc/sys/net/ipv4/tcp_congestion_control', shell=True)
    ccName = ccName.replace("\n","")

    print('===========================================================================')

    net.pingAll()
    print('===========================================================================')

    Se2.cmd('iperf -s  > dataResult/examine3/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_iperf-server.txt &')
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


    os.system('mv /home/reghn/Documents/pcapngs/_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_.pcapng')
    os.system('mv dataResult/examine3/_LL_iperfRests.txt dataResult/examine3/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_iperfRests.txt')
    os.system('mv dataResult/examine3/_LL_rttRests.txt dataResult/examine3/'+str(ccName)+'_'+str(maxQ)+'_mix_LL_rttRests.txt')
    print('=========================================================================')
    
    
    
    print('=========================================================================')
    #Cl1.cmd('tcpdump -G 10 -W 1 -w /home/reghn/Documents/pcapngs/_SL_.pcapng -i Cl1-eth0 &')
    
    print("                         Processing all file's   ")
    
    #os.system('mv /home/reghn/Documents/pcapngs/_SL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_SL_.pcapng')
    os.system('mv restSL.png restSL'+str(ccName)+'_'+str(maxQ)+'_mix')
    print('=========================================================================')
    time.sleep(60)
    #CLI(net)
    net.stop()

def runAll():
    #os.system('sysctl -w net.ipv4.tcp_congestion_control=cubic')
    #mainTopo()
    #os.system('sysctl -w net.ipv4.tcp_congestion_control=bbr')
    #mainTopo()
    os.system('sysctl -w net.ipv4.tcp_congestion_control=ledbat')
    mainTopo()

if __name__ =='__main__':
    setLogLevel('info')
    
    maxq = [20000]
    for maxQ in maxq:
        runAll()
    