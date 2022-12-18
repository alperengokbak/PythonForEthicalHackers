import scapy.all as scapy
import optparse
from scapy_http import http


def getInterface():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-i", "--iface", dest="interface",
                           help="You have to put these commands -i or --iface before your interface.")

    userInput = parseObject.parse_args()[0]

    return userInput.interface


def listenPacket(interface):
    scapy.sniff(iface=interface, store=False, prn=analyzePackets)


def analyzePackets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


userInput = getInterface()
listenPacket(userInput)
