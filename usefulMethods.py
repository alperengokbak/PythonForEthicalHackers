from random import randint
from random import shuffle

# Range
#! If we want to create a new list 1 to 20, there is a shortcut for that.

myList = range(20)

for element in myList:
    print(element)

#! At the same time, you can define the starting point.

myList = range(5, 20)

for element in myList:
    print(element)

#! And lastly, we define the step size like string functions.

myList = range(5, 20, 2)

for element in myList:
    print(element)


# Enumerate

index = 0
for number in range(5, 15):
    print(f"Index: {index} number: {number}")
    index += 1

#! We can do same thing with enumerate instead of upside expression.

for element in enumerate(range(5, 15)):
    print(element)

#! We can take separately index and number with enumerate.

for index, number in enumerate(range(5, 15)):
    print(index)
    print(number)

# Random number generator
#! We have to call random library, python allows us in default library.
print(randint(0, 1000))

#! This if we have a sorted list, we can shuffle that list with shuffle library.(import the random library again)
myList2 = list(range(0, 12))
shuffle(myList2)
print(myList2)

# Zip
#! If we have two different list, we can hold the inside same list with zip keyword.
sportList = ["Run", "Swim", "Basketball"]
caloriesList = [100, 200, 300]
newList = list(zip(sportList, caloriesList))
print(newList)

# List Advanced
#! We can add each letter of string inside of the empty list with for loop.
myList3 = list()

myString = "Endless Love"

for element in myString:
    myList3.append(element)
print(myList3)

#! There is short way to do upside code block.

myList4 = [element for element in myString]
print(myList4)

myList5 = [number**5 for number in list(range(5, 12))]
print(myList5)
