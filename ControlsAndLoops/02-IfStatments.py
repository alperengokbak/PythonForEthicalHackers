if (3 >= 2):
    print("3 is greater than 2")

print("****************")

x = 2
y = 4
if (x > y):
    print("x is greater than y")
elif (x < y):
    print("y is greater than x")
else:
    print("x is equal to y")

print("****************")

superHero = input("What's your super hero: ")
if (superHero == "Superman"):
    print("SuperMan is the best...")
elif (superHero == "Batman"):
    print("Looser...")
elif (superHero == "Captain America"):
    print("That's my boy...")
else:
    print("You will find true way one day.")

print("****************")

a = 10
b = 15
c = 20

if (a > 11 or b > 11):
    print("First time...")
elif (a == b and c >= 15):
    print("Second time...")
elif (not a == b):
    print("Third time...")

print("****************")

isDead = False

if (isDead):  # ! "isDead" expression if "True" display the if statement, otherwise display the else statement. You don't have to use comporison expression.
    print("Character is not dead")
else:
    print("Character is dead")

print("****************")

myString = "Hello World!"

if (myString == "Hello World!"):
    print("Equals!")

if ("Hello" in myString):
    print("True")
else:
    print("False")

print("****************")

myList = [1, 2, 3, 4, 5]

# ! Usually we use "in" with "IF Statement". If include defined value inside of list or string, etc.
if (2 in myList):
    print("Include 2")
else:
    print("Not Include 2")

print("****************")

myDictionary = {"key1": 100, "key2": 200}

if (100 in myDictionary.values()):
    print("Include 100")
else:
    print("Not Include 100")
