# These are the default pyhton functions.
myString = "Alperen"
print(myString.upper())  # Allows to us make capitalize the whole string.

myStringUpper = myString.upper()
print(myStringUpper)

# Now, we can create a special own functions.
# Input % Return


def helloWorld(string):
    print("Hello " + string)


helloWorld("Alperen")


# !If we want to don't crash the our program, we can define the default value. So, we don't have to give value.
def helloWorld2(string="World"):
    print("Hello " + string)


helloWorld2()


def summation(number1, number2):
    return number1 + number2


print(summation(5, 4))


def controlString(string):

    if string[0] == "m":
        print(string.capitalize())
    else:
        print(string)


controlString("mama")

# Arbitray And Key Word Arguments


def summation2(number1, number2):
    return number1 + number2


# ! If we put the "*" in front of the defined argument. That meaning is user can write as many elements as user want. But usually we don't use any word after the "*". Programmers write "args" for that expression.
def summation3(*args):
    return sum(args)


print(summation3(10, 20, 30, 40))


# ! "**kwargs" keyword argument will give to us dictionary formatting result. The critical point is "**" double stars. Actually, It does everything.
def example_func(**kwargs):
    print(kwargs)


example_func(run=100, swim=200, basketball=300)


def poplularCity(**kwargs):
    if "Miami" in kwargs:
        print("07.2023")
    else:
        print(":(")


poplularCity(Miami=10, LosAngeles=5)
