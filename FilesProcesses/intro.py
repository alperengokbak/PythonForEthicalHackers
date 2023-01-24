myFile = open("example.txt")
# Always cursor keep going to at the end of the line. That's why, we have to return the cursor first line again.
myFile.read()
# If we want to return the cursor first line again, we can use the ".seek" method.
myFile.seek(0)
myFile.close()

# ! We can do automaticlly with "with" command.
with open("example.txt") as myFile:
    fileRead = myFile.read()

#! If you define the mode as like below line, python just allows you to do inside of the brackets modes.These are "r","w","a"
with open("example.txt", mode="w") as myFile:
    myFile.write("Test121212121")

with open("example.txt", mode="a") as myFile:
    myFile.write("\ntest5")

with open("example.txt", mode="r") as myFile:
    fileRead = myFile.read()

print(fileRead)
