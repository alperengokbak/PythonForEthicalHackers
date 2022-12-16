import subprocess as sub
import optparse
import re


def getInput():
    parseObject = optparse.OptionParser()

    parseObject.add_option("-i", "--interface",
                           dest="interface", help="Interface to change!")

    parseObject.add_option(
        "-m", "--mac", dest="macAddress", help="New MAC Address")

    return parseObject.parse_args()


def changeAddress(userInterface, userMacAddress):
    sub.call(["ifconfig", userInterface, "down"])
    sub.call(["ifconfig", userInterface, "hw", "ether", userMacAddress])
    sub.call(["ifconfig", userInterface, "up"])


def controlMac(interface):
    ifconfig = sub.check_output(["ifconfig", interface])
    newMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if newMac:
        return newMac.group(0)
    else:
        return None


print("Mac Changer started...")

(userInput, arguments) = getInput()
changeAddress(userInput.interface, userInput.macAddress)
finalizedMac = controlMac(str(userInput.interface))
if finalizedMac == userInput.macAddress:
    print("You changed MAC Address successfully...")
else:
    print("Error!")
