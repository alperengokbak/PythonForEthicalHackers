def divide(number):
    return number / 2


myList = list()


def createList(myList):
    for element in range(1, 10):
        myList.append(divide(element))
    print(myList)


createList(myList)

# Map
# ! Map function take the elements of the list. And put them in the defined function. Lastly, again put them in list.
print(list(map(divide, myList)))


def controlString(string):
    if "Endless" in string:
        return True
#! We can reach the same result by using simplier way.


def controlString2(string):
    return "Miami" in string


def controlString3(string):
    return "i" in string


print(controlString("Endless"))
print(controlString2("Endles"))

myCityList = ["Miami", "Los Angeles", "California", "New York"]
print(list(map(controlString2, myCityList)))

# Filter
#! Filter function create a list and if return True value, It will put the list returned value. If return False value, will do nothing.
print(list(filter(controlString3, myCityList)))

# Lambda Function
#! Usually we use the function disposable function.(disposable --> Tek kullanımlık)


def multiply(number):
    return number * 5

#! If we will use the function just one time, we can use the lamda function. There is a simple syntax;


def multiply2(number): return number * 5


#! Each function gives same result for us. But usually we don't use that way. Because has low readability.
print(multiply(5))
print(multiply2(5))

#! We can give one more example about "lambda" function.
myList2 = [2, 4, 6, 8]
# * We don't have to create multiply function to just one time. We can use the lambda function to that process.
print(list(map(lambda x: x*3, myList2)))
