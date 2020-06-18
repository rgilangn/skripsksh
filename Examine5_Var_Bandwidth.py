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
BW = 0
hs_size = 2

def mainTopo():
    #Define Initial Topology on Mininet
    os.system('mn -c')
    print('===========================================================================')
    print('===========================================================================')
    net = Mininet(link=TCLink, host=CPULimitedHost)
    net.start()

    Cl1 = net.addHost('Cl1', ip='192.168.1.2/24')
    Cl2 = net.addHost('Cl2', ip='192.168.2.2/24')
    # # Cl3 = net.addHost('Cl3', ip='192.168.3.2/24')
    # # Cl4 = net.addHost('Cl4', ip='192.168.4.2/24')
    # # Cl5 = net.addHost('Cl5', ip='192.168.5.2/24')
    # # Cl6 = net.addHost('Cl6', ip='192.168.6.2/24')
    # # Cl7 = net.addHost('Cl7', ip='192.168.7.2/24')
    # # Cl8 = net.addHost('Cl8', ip='192.168.8.2/24')

    Se1 = net.addHost('Se1', ip='192.168.10.2/24')
    Se2 = net.addHost('Se2', ip='192.168.20.2/24')
    # # Se3 = net.addHost('Se3', ip='192.168.30.2/24')
    # # Se4 = net.addHost('Se4', ip='192.168.40.2/24')
    # # Se5 = net.addHost('Se5', ip='192.168.50.2/24')
    # # Se6 = net.addHost('Se6', ip='192.168.60.2/24')
    # # Se7 = net.addHost('Se7', ip='192.168.70.2/24')
    # # Se8 = net.addHost('Se8', ip='192.168.80.2/24')


    Ro1 = net.addHost('Router1')

    net.addLink(Cl1, Ro1, bw=100)
    net.addLink(Cl2, Ro1, bw=100)
    # net.addLink(Cl3, Ro1, bw=100)
    # net.addLink(Cl4, Ro1, bw=100)
    # net.addLink(Cl5, Ro1, bw=100)
    # net.addLink(Cl6, Ro1, bw=100)
    # net.addLink(Cl7, Ro1, bw=100)
    # net.addLink(Cl8, Ro1, bw=100)

    net.addLink(Se1, Ro1, bw=BW, max_queue_size = maxQ) #, max_queue_size = maxQ
    net.addLink(Se2, Ro1, bw=BW, max_queue_size = maxQ) #
    # net.addLink(Se3, Ro1, bw=BW, max_queue_size = maxQ) #
    # net.addLink(Se4, Ro1, bw=BW, max_queue_size = maxQ) #
    # net.addLink(Se5, Ro1, bw=BW) #
    # net.addLink(Se6, Ro1, bw=BW) #
    # net.addLink(Se7, Ro1, bw=BW) #
    # net.addLink(Se8, Ro1, bw=BW) #


    net.build()
    print('===========================================================================')
    print('===========================================================================')
    Ro1.cmd('ifconfig Router1-eth0 0')
    Ro1.cmd('ifconfig Router1-eth1 0')
    Ro1.cmd('ifconfig Router1-eth2 0')
    Ro1.cmd('ifconfig Router1-eth3 0')
    # Ro1.cmd('ifconfig Router1-eth4 0')
    # Ro1.cmd('ifconfig Router1-eth5 0')
    # Ro1.cmd('ifconfig Router1-eth6 0')
    # Ro1.cmd('ifconfig Router1-eth7 0')
    # Ro1.cmd('ifconfig Router1-eth8 0')
    # Ro1.cmd('ifconfig Router1-eth9 0')
    # Ro1.cmd('ifconfig Router1-eth10 0')
    # Ro1.cmd('ifconfig Router1-eth11 0')
    # Ro1.cmd('ifconfig Router1-eth12 0')
    # Ro1.cmd('ifconfig Router1-eth13 0')
    # Ro1.cmd('ifconfig Router1-eth14 0')
    # Ro1.cmd('ifconfig Router1-eth15 0')

    Ro1.cmd('ifconfig Router1-eth0')
    Ro1.cmd('ifconfig Router1-eth1')
    Ro1.cmd('ifconfig Router1-eth2')
    Ro1.cmd('ifconfig Router1-eth3')
    # Ro1.cmd('ifconfig Router1-eth4')
    # Ro1.cmd('ifconfig Router1-eth5')
    # Ro1.cmd('ifconfig Router1-eth6')
    # Ro1.cmd('ifconfig Router1-eth7')
    # Ro1.cmd('ifconfig Router1-eth8')
    # Ro1.cmd('ifconfig Router1-eth9')
    # Ro1.cmd('ifconfig Router1-eth10')
    # Ro1.cmd('ifconfig Router1-eth11')
    # Ro1.cmd('ifconfig Router1-eth12')
    # Ro1.cmd('ifconfig Router1-eth13')
    # Ro1.cmd('ifconfig Router1-eth14')
    # Ro1.cmd('ifconfig Router1-eth15')

    Ro1.cmd("ip addr add 192.168.1.1/24 brd + dev Router1-eth0")
    Ro1.cmd("ip addr add 192.168.2.1/24 brd + dev Router1-eth1")
    Ro1.cmd("ip addr add 192.168.10.1/24 brd + dev Router1-eth2")
    Ro1.cmd("ip addr add 192.168.20.1/24 brd + dev Router1-eth3")

    # Ro1.cmd("ip addr add 192.168.10.1/24 brd + dev Router1-eth4")
    # Ro1.cmd("ip addr add 192.168.20.1/24 brd + dev Router1-eth5")
    # Ro1.cmd("ip addr add 192.168.30.1/24 brd + dev Router1-eth6")
    # Ro1.cmd("ip addr add 192.168.40.1/24 brd + dev Router1-eth7")

    # Ro1.cmd("ip addr add 192.168.30.1/24 brd + dev Router1-eth8")
    # Ro1.cmd("ip addr add 192.168.40.1/24 brd + dev Router1-eth9")
    # Ro1.cmd("ip addr add 192.168.50.1/24 brd + dev Router1-eth10")
    # Ro1.cmd("ip addr add 192.168.60.1/24 brd + dev Router1-eth11")

    # Ro1.cmd("ip addr add 192.168.50.1/24 brd + dev Router1-eth12")
    # Ro1.cmd("ip addr add 192.168.60.1/24 brd + dev Router1-eth13")
    # Ro1.cmd("ip addr add 192.168.70.1/24 brd + dev Router1-eth14")
    # Ro1.cmd("ip addr add 192.168.80.1/24 brd + dev Router1-eth15")

    Ro1.cmd('sysctl -w net.ipv4.ip_forward=1')

    Cl1.cmd('ip route add default via 192.168.1.1')
    Cl2.cmd('ip route add default via 192.168.2.1')
    # Cl3.cmd('ip route add default via 192.168.3.1')
    # Cl4.cmd('ip route add default via 192.168.4.1')
    # Cl5.cmd('ip route add default via 192.168.5.1')
    # Cl6.cmd('ip route add default via 192.168.6.1')
    # Cl7.cmd('ip route add default via 192.168.7.1')
    # Cl8.cmd('ip route add default via 192.168.8.1')

    Se1.cmd('ip route add default via 192.168.10.1')
    Se2.cmd('ip route add default via 192.168.20.1')
    # Se3.cmd('ip route add default via 192.168.30.1')
    # Se4.cmd('ip route add default via 192.168.40.1')
    # Se5.cmd('ip route add default via 192.168.50.1')
    # Se6.cmd('ip route add default via 192.168.60.1')
    # Se7.cmd('ip route add default via 192.168.70.1')
    # Se8.cmd('ip route add default via 192.168.80.1')

    print('=================STARTING SCENARIO 4 (Bufferbloat 8 Device)=======================')
    print('===========================================================================')

    ccName = subprocess.check_output('cat /proc/sys/net/ipv4/tcp_congestion_control', shell=True)
    ccName = ccName.replace("\n","")

    print('===========================================================================')

    net.pingAll()
    print('===========================================================================')

    # Se2.cmd('iperf -s &')
    Se1.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperf-server1.txt &')
    Se2.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperf-server2.txt &')
    # Se3.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperf-server3.txt &')
    # Se4.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperf-server4.txt &')
    # Se5.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperf-server5.txt &')
    # Se6.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperf-server6.txt &')
    # Se7.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_iperf-server7.txt &')
    # Se8.cmd('iperf -s  > dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_iperf-server8.txt &')
    
    print('                          Server Iperf Started')
    Se1.cmd('python -m SimpleHTTPServer &')
    Se2.cmd('python -m SimpleHTTPServer &')
    # Se3.cmd('python -m SimpleHTTPServer &')
    # Se4.cmd('python -m SimpleHTTPServer &')
    # Se5.cmd('python -m SimpleHTTPServer &')
    # Se6.cmd('python -m SimpleHTTPServer &')
    # Se7.cmd('python -m SimpleHTTPServer &')
    # Se8.cmd('python -m SimpleHTTPServer &')

    print('=========================================================================')
    ####    STARTING EXAMINE    ####
    print('                TCPDUMP Started Longlived for 65 s Please Wait')
    print('                              Iperf Started')
    Cl1.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/1_LL_.pcapng -i Cl1-eth0 &') #62s
    Cl1.cmd('iperf -c 192.168.10.2 -t 30 -i 1 > dataResult/examine5-2hosts/1_LL_iperfRests.txt &') #30s
    Cl1.cmd('ping 192.168.10.2 -c 30 > dataResult/examine5-2hosts/1_LL_rttRests.txt & ') #30s
    # Cl1.cmd('ping 192.168.10.2 -c 9 ')

    Cl2.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/2_LL_.pcapng -i Cl2-eth0 &') #62s
    Cl2.cmd('iperf -c 192.168.20.2 -t 30 -i 1 > dataResult/examine5-2hosts/2_LL_iperfRests.txt &') #30s
    Cl2.cmd('ping 192.168.20.2 -c 30 > dataResult/examine5-2hosts/2_LL_rttRests.txt & ') #30s
    # Cl2.cmd('ping 192.168.20.2 -c 9 ')
    
    # # Cl3.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/3_LL_.pcapng -i Cl3-eth0 &') #62s
    # Cl3.cmd('iperf -c 192.168.30.2 -t 30 -i 1 > dataResult/examine5-2hosts/3_LL_iperfRests.txt &') #30s
    # Cl3.cmd('ping 192.168.30.2 -c 30 > dataResult/examine5-2hosts/3_LL_rttRests.txt & ') #30s
    # Cl3.cmd('ping 192.168.30.2 -c 9 ')
    
    # # Cl4.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/4_LL_.pcapng -i Cl4-eth0 &') #62s
    # Cl4.cmd('iperf -c 192.168.40.2 -t 30 -i 1 > dataResult/examine5-2hosts/4_LL_iperfRests.txt &') #30s
    # Cl4.cmd('ping 192.168.40.2 -c 30 > dataResult/examine5-2hosts/4_LL_rttRests.txt & ') #30s
    # Cl4.cmd('ping 192.168.40.2 -c 9 ')
        
    # # Cl5.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/5_LL_.pcapng -i Cl5-eth0 &') #62s
    # Cl5.cmd('iperf -c 192.168.50.2 -t 30 -i 1 > dataResult/examine5-2hosts/5_LL_iperfRests.txt &') #30s
    # Cl5.cmd('ping 192.168.50.2 -c 30 > dataResult/examine5-2hosts/5_LL_rttRests.txt & ') #30s
    # Cl5.cmd('ping 192.168.50.2 -c 9 ')

    # # Cl6.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/6_LL_.pcapng -i Cl6-eth0 &') #62s
    # Cl6.cmd('iperf -c 192.168.60.2 -t 30 -i 1 > dataResult/examine5-2hosts/6_LL_iperfRests.txt &') #30s
    # Cl6.cmd('ping 192.168.60.2 -c 30 > dataResult/examine5-2hosts/6_LL_rttRests.txt & ') #30s
    # Cl6.cmd('ping 192.168.60.2 -c 9 ')
            
    # # Cl7.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/7_LL_.pcapng -i Cl7-eth0 &') #62s
    # Cl7.cmd('iperf -c 192.168.70.2 -t 30 -i 1 > dataResult/examine5-2hosts/7_LL_iperfRests.txt &') #30s
    # Cl7.cmd('ping 192.168.70.2 -c 30 > dataResult/examine5-2hosts/7_LL_rttRests.txt & ') #30s
    # Cl7.cmd('ping 192.168.70.2 -c 9 ')
            
    # # Cl8.cmd('tcpdump -G 35 -W 1 -w /home/reghn/Documents/pcapngs/8_LL_.pcapng -i Cl8-eth0 &') #62s
    # Cl8.cmd('iperf -c 192.168.80.2 -t 30 -i 1 > dataResult/examine5-2hosts/8_LL_iperfRests.txt &') #30s
    # Cl8.cmd('ping 192.168.80.2 -c 30 > dataResult/examine5-2hosts/8_LL_rttRests.txt & ') #30s
    # Cl8.cmd('ping 192.168.80.2 -c 9 ')

    time.sleep(2)

    #pidCode = subprocess.check_output('pidof tcpdump', shell=True)
    # pidCode = pidCode.replace("\n","")
    # Cl1.cmd('kill '+str(pidCode)+'')
    #### rename file ####

    os.system('mv /home/reghn/Documents/pcapngs/1_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_CL1.pcapng')
    os.system('mv dataResult/examine5-2hosts/1_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperfRests_Cl1.txt')
    os.system('mv dataResult/examine5-2hosts/1_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_rttRests._Cl1.txt')

    os.system('mv /home/reghn/Documents/pcapngs/2_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_CL2.pcapng')
    os.system('mv dataResult/examine5-2hosts/2_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperfRests_Cl2.txt')
    os.system('mv dataResult/examine5-2hosts/2_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_rttRests._Cl2.txt')
    
    # os.system('mv /home/reghn/Documents/pcapngs/3_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_CL3.pcapng')
    # os.system('mv dataResult/examine5-2hosts/3_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperfRests_Cl3.txt')
    # os.system('mv dataResult/examine5-2hosts/3_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_rttRests._Cl3.txt')
    
    # os.system('mv /home/reghn/Documents/pcapngs/4_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_CL4.pcapng')
    # os.system('mv dataResult/examine5-2hosts/4_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperfRests_Cl4.txt')
    # os.system('mv dataResult/examine5-2hosts/4_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_rttRests._Cl4.txt')
    
    # os.system('mv /home/reghn/Documents/pcapngs/5_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_CL5.pcapng')
    # os.system('mv dataResult/examine5-2hosts/5_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperfRests_Cl5.txt')
    # os.system('mv dataResult/examine5-2hosts/5_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_rttRests._Cl5.txt')
    
    # os.system('mv /home/reghn/Documents/pcapngs/6_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+''+str(hs_size)+'__LL_CL6.pcapng')
    # os.system('mv dataResult/examine5-2hosts/6_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_iperfRests_Cl6.txt')
    # os.system('mv dataResult/examine5-2hosts/6_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_'+str(hs_size)+'_LL_rttRests._Cl6.txt')
    
    # os.system('mv /home/reghn/Documents/pcapngs/7_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_CL7.pcapng')
    # os.system('mv dataResult/examine5-2hosts/7_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_iperfRests_Cl7.txt')
    # os.system('mv dataResult/examine5-2hosts/7_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_rttRests._Cl7.txt')
    
    # os.system('mv /home/reghn/Documents/pcapngs/8_LL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_CL8.pcapng')
    # os.system('mv dataResult/examine5-2hosts/8_LL_iperfRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_iperfRests_Cl8.txt')
    # os.system('mv dataResult/examine5-2hosts/8_LL_rttRests.txt dataResult/examine5-2hosts/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_LL_rttRests._Cl8.txt')
    
    print('=========================================================================')
    print('                          Python HTTP Server Start')
    print('=========================================================================')
    
    os.system('echo              Shortlived Started for 10 s Please Wait')

    # Cl1.cmd('tcpdump -G 25 -W 1 -w /home/reghn/Documents/pcapngs/_SL_.pcapng -i Cl1-eth0 &')
    
    Cl1.cmdPrint('wget -q 192.168.10.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL_Cl1.png &')    
    #os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl1')

    # os.system('mv /home/reghn/Documents/pcapngs/_SL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_SL_.pcapng')

    Cl2.cmdPrint('wget -q 192.168.20.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL_Cl2.png &')
    # os.system('mv /home/reghn/Documents/pcapngs/_SL_.pcapng /home/reghn/Documents/pcapngs/'+str(ccName)+'_'+str(maxQ)+'_'+str(BW)+'_SL_Cl2.pcapng')
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl2')

    # Cl3.cmdPrint('wget -q 192.168.30.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL_Cl3.png &')    
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl3')


    # Cl4.cmdPrint('wget -q 192.168.40.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL.png &')    
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl4')

    # Cl5.cmdPrint('wget -q 192.168.50.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL.png &')    
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl5')

    # Cl6.cmdPrint('wget -q 192.168.60.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL.png &')    
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl6')

    # Cl7.cmdPrint('wget -q 192.168.70.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL.png &')    
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl7')

    # Cl8.cmdPrint('wget -q 192.168.80.2:8000 &')
    # os.system('scrot --delay 2 '+str(ccName)+''+str(maxQ)+'_'+str(BW)+'restSL.png &')    
    # os.system('mv restSL.png restSL'+str(ccName)+''+str(maxQ)+'_'+str(BW)+'_Cl8')


    print('=========================================================================')
    print("                         Processing all file's   ")
    Cl1.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    Se2.cmdPrint('sysctl  net.ipv4.tcp_congestion_control')
    print("QUEUE_SIZE", maxQ)
    print("LINK_BANDWIDTH, RO-SE ", BW)
    print("HOST_SIZE ",hs_size)
    print('=========================================================================')
    time.sleep(40)

    
    # CLI(net)
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
    Bw_Exp = [0.512, 0.256]
    maxq = [20, 200, 2000, 20000]
    for BW in Bw_Exp:
        for maxQ in maxq:
            runAll()
        # runAll()
    