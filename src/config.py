import argparse

parser = argparse.ArgumentParser(description="create schema to a PCAP")
parser.add_argument("pcap", metavar="p", help="path to pcap file")
parser.add_argument("client_ip", metavar="c", help="client's ip")
parser.add_argument("-f", dest="display_filter", metavar="f", help="display filter")
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

args = parser.parse_args()
pcap_path = args.pcap
display_filter = args.display_filter
client_ip = args.client_ip