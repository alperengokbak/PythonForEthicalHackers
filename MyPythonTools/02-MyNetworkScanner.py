import optparse
import scapy.all as scapy

# Create arp request
# Make broadcasting
# Response


def getInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-i", "--ip", dest="ipAddress",
                           help="Enter your IP Range..")

    (userInput, arguments) = parseObject.parse_args()
    if not userInput.ipAddress:
        print("Enter The IP Address: ")

    return userInput


def arpRequest(ipAddress):
    # Normally, It's default value but one day can be change the documentation. That's why, if you want to make broadcast, you have to use this Mac Address
    answeredList, unAnsweredList = scapy.srp(scapy.Ether(
        dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ipAddress), timeout=2)
    answeredList.summary()


userIpAddress = getInput()
arpRequest(userIpAddress.ipAddress)
