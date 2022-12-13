number = 10


def multiply(num):
    number = 5
    return number * num


print(multiply(10))

#! LEGB --> L --> Local, E --> Enclosing, G --> Global, B --> Built-in

# ? Global
myString = "Alperen"


def myFunc():
    # ? Enclosing
    myString = "Emine"

    def myFunc2():
        # ? Local
        myString = "Endless"
        print(myString)
    print(myString)
    myFunc2()


myFunc()
print(myString)


y = 10


def newFunc(y):
    #! Normally, If we want to change the global "y". We should assign the "y".
    y = 5
    return y


y = newFunc(y)
print(y)

x = 10


def newFunc2():
    #! But there is a another way to change global variables. We can use the "global" keyword.
    global x
    x = 5
    print(x)


newFunc2()
print(x)
