# ! We can do automaticlly with "with" command.
with open("example.txt") as myFile:
    fileRead = myFile.read()

print(fileRead)