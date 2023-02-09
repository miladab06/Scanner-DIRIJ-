import colorama
import requests, time, sys, os, http.client, socket, threading
from colorama import Fore, Back, Style
def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    for i in range(500):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(500):
        threads[i].start()

    # Locking the script until all threads complete
    for i in range(500):
        threads[i].join()
        if output[i] == 'Listening':
            print (Fore.GREEN+ str(i) + '\t>>>' +Style.RESET_ALL+Fore.RED+'\tOpen ' +' ('+output[i] +') '+Style.RESET_ALL)
            print('----------------------------------------------------------------------------------------------')

    # Printing listening ports from small to large
    #for i in range(65535):
        #if output[i] == 'Listening':
            #print(str(i) + ': ' + output[i])

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay) 
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''