# Lesson 1

# list = []
# dict = {}
# set = {}
# tuple = ()

#! We can reach some functions like that, list.append(). Type list or other ones. And put the dot.
#! Tuple's value cannot be change after created.
#! Sets value cannot be loop. Display just one time.
#! dict["key1"] = "value1". You can add the value inside the dict.
#! If we want to reach dictionary values, you can write two brackets.
# print(myDictionary4["key3"]["key4"])

#! Slicing
#! Starting second index and display coming from second index.
# print(myString2[2:])
#! Display index until second one.(Stoping point, Stoping index)
# print(myString2[:2])
# print(myString2[3:4])  # Display index third one between fourth one.

#! Step Size
# print(myString2[::2])  # We can define the step size. Growing two by two.
#! Display the whole string, but starting from the end of the string.
# print(myString2[::-1])

# Lesson 2

#! We use "and" instead of "&&" in Python.
#print(x >= 5 and y >= x)

#! We use "or" instead of "||" in Python.
#print(x >= 5 or y <= x)

#! Lastly, "not" will display the opposite values.
#print(not x == y)


# ! We say formatting, If we want to display the p with string expression, use the "f" in front of first bracket.
# print(f"Value p: {p}")

#! If we want to find remaining from the division. Use "%" expression.

# Lesson 3

# ! If we put the "*" in front of the defined argument. That meaning is user can write as many elements as user want. But usually we don't use any word after the "*". Programmers write "args" for that expression.
# def summation3(*args):
#    return sum(args)

# ! "**kwargs" keyword argument will give to us dictionary formatting result. The critical point is "**" double stars. Actually, It does everything.
# def example_func(**kwargs):
#    print(kwargs)

# ! Map function take the elements of the list. And put them in the defined function. Lastly, again put them in list.
#print(list(map(divide, myList)))

# Filter
#! Filter function create a list and if return True value, It will put the list returned value. If return False value, will do nothing.
#print(list(filter(controlString3, myCityList)))


# Decorator

# ! We can call the function inside a another function too.
#decoratorFunc = decoratorFunciton(func2)
# decoratorFunc()

#! There is a shortcut here. We don't have to do confused steps, if we define the function "@decoratorFunc" pyhton will do same steps in background.
# @decoratorFunciton
# def func2():
#    print("Hello World")
# func2()


# Lesson 4
# class Musician():
# ? We have to create a special function that "def __init__". Init coming from initilaze. When you create a instance from the class, I mean new instance. You have to call the "__init__" function. You write the properties of your object. In this way, when anyone create a instance from your class. They have to define these properties. That's why, we use the __init__ function.
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
