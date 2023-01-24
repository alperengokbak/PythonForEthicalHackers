myList = [1, 2, 3, 4, 5]

for number in myList:
    print(number)

print("******************")

for number in myList:
    newNumber = number * 2
    print(newNumber)

print("******************")

for number in myList:
    if (number % 2 == 1):
        print(number)

print("******************")

myString = "Alperen Gökbak"

for letter in myString:
    print(letter)

print("******************")

myTuple = (1, 1, 2, 4, 5, 2, 2)

for number in myTuple:
    print(number)

print("******************")

myList2 = [("c", "d"), ("e", "f"), ("g", "h")]

for element in myList2:
    print(element)

print("******************")

for x, y in myList2:  # We can split each tuple with for loops.
    print(x)

print("******************")

myDict = {"key": 100, "key2": 200, "key3": 300}

# ! We can display the keys or values with for loop.
for key, value in myDict.items():
    print(key)
