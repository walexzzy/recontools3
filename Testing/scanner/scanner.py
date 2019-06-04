import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-H", dest="tgtHost", type=str, help="specify target host")
parser.add_argument("-p", dest="tgtPort", type=str, help="specify target port")
args = parser.parse_args()
tgtHost = args.tgtHost
tgtPort = args.tgtPort
if (tgtHost is None) | (tgtPort is None):
    print(parser.print_help())
    exit(0)
