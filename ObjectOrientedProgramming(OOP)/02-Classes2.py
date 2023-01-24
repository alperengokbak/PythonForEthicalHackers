class DogYear():

    yearFactor = 7

    #! We can assign default value, when creating a new attribute.
    def __init__(self, age=5):
        self.age = age
        self.dogYear = self.age * 7

    def calculate(self):
        return self.age * self.yearFactor


myPet = DogYear(3)
print(myPet.dogYear)

print("**************")

# Inheritance


class Class1():
    def __init__(self):
        print("Created Class1")

    def method1(self):
        print("Method1")

    def method2(self):
        print("Method2")


class Class2(Class1):
    #! Shortly, inheritance allows to use same methods inside of the "Class1". Actually, we extend the main class inside of the subclass.
    def __init__(self):
        print("Created Class2")
        Class1.__init__(self)

    #! Override
    def method1(self):
        print("Method1 override")

    def method3(self):
        print("Method3")


myInstance = Class1()
myInstance.method1()
myInstance.method2()

print("*************")

myInstance2 = Class2()
myInstance2.method1()
myInstance2.method3()

print("*************")

# Polymorphism


class Apple():
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name + " 100 Calories"


class Banana():
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name + " 200 Calories"


banana = Banana("banana")
apple = Apple("apple")

fruitList = [apple, banana]

for fruit in fruitList:
    print(fruit.info())
