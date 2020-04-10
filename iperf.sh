#!/bin/bash 
#qsize=$1

iperf -c 192.168.2.2 -t 60 -i 1  > dataResult/iperfRests.txt & 
ping 192.168.2.2 -c 60 > dataResult/rttRests.txt &

echo "started iperf and pingComm"

