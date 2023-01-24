class Fruits():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):  # ! Normally we put the instance in print(), we could not get the attributes. But if we use the "__str__" method and put the inside of "print()". We will see that inside the __str__ method.
        return f"{self.name} has {self.calories}"

    # ! At the same time, we can use the __len__ method too. Using sytnax similiar to other special methods.
    def __len__(self):
        return self.calories


myFruit = Fruits("Banana", 200)
print(myFruit)
print(len(myFruit))
