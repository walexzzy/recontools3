import socket
import os
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-H", dest="tgtHost", type=str, help="specify target host minus the last octet i.e. x.x.x.")
args = parser.parse_args()
tgtHost = args.tgtHost
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Server is Vulnerable: ' + banner.strip('\n'))
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] ' + filename + ' does not exist.')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] ' + filename + ' access denied.')
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        exit(0)
        portlist = [21,22,25,80,110,443]
        for x in range(147, 150):
            ip ='tgtHost' + str(x)
            for port in portList:
                banner = retBanner(ip, port)
                if banner:
                    print("[+]"+ ip + ": " + banner)
                    checkVulns(banner, filename)
if __name__ == '__main__':
    main()
