# Data Types
# Integer
# Float (We can describe decimal numbers with float type.)
# Boolean
# String

# Some important notes about processors.
print(2**3)  # ! It shows result of 2*2*2.
print(2**9)  # We can give same example like that, result coming 512.
print(20 % 2)  # We can find remainder like that.
print("*****************************")
# Variables
x = 18
y = 25
print(x+y)
print(x**y)  # ! x^y
print("*****************************")
# ! At the same time, take value from the users, that's not going to be integer value.
# ? If you want to use with integers, you have to specify int(r). Otherwise "r" value will be String value.
#r = input("r: ")
#pi = 3.14
#result = int(r) * 2 * pi
# print(result)
print("*****************************")
# Warning
x = "Hello"
print(type(x))
print(x)
# ! Normally we can't change the value of variable string to integer. But python allows to change.
x = 18
print(type(x))
print(x)
x = "Hello"
print("Lenght: ", len(x))  # Lenght of the variable.
print("*****************************")

# Indexing
myString = "Hello World"
print(myString[4])
print(myString[-1])  # Meaning is starting from the end of the string.
print(myString[-2])

# Slicing
myString2 = "1234567"
# Starting second index and display coming from second index.
print(myString2[2:])
# Display index until second one.(Stoping point, Stoping index)
print(myString2[:2])
print(myString2[3:4])  # Display index third one between fourth one.

# Step Size
print(myString2[::2])  # We can define the step size. Growing two by two.
# Display the whole string, but starting from the end of the string.
print(myString2[::-1])
