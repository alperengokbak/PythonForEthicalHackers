import os
from cryptography.fernet import Fernet

fileList = list()


def appendTheList():
    for file in os.listdir():
        if file == "ransom.py" or file == "generatedKey.key" or file == "ransomdecrypter.py":
            continue
        if os.path.isfile(file):
            fileList.append(file)


def decryptedFile():
    for file in fileList:
        with open(file, "rb") as theFile:
            contents = theFile.read()
        contentsDecrypted = Fernet(secretKey).decrypt(contents)
        with open(file, "wb") as theFile:
            theFile.write(contentsDecrypted)


appendTheList()

with open("generatedKey.key", "rb") as generatedKey:
    secretKey = generatedKey.read()

decryptedFile()
