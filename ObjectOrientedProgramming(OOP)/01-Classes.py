# Class
myList = list()  # ! Actually, we have created object from list class.(Instance & Attribute)
# ! We can reach the attribute if we put "." dot after the "myList" instance.
myList.append("element")

# ? There are some case inside of programming language.
#! These are;
#! snake --> my_string and other one is
#! camel --> myString We keep using camel case while creating the class.


class Musician():  # ? We have to create a special function that "def __init__". Init coming from initilaze. When you create a instance from the class, I mean new instance. You have to call the "__init__" function. You write the properties of your object. In this way, when anyone create a instance from your class. They have to define these properties. That's why, we use the __init__ function.
    job = "musician"

    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre

    # Methods
    def sing(self):
        print(self.name + " singing the " + self.genre)


# ! Each methods are special for the each instances.
myMusician = Musician("Alperen", 22, "Rock")
myMusician.sing()
myMusician2 = Musician("Emine", 28, "Traditional")
myMusician2.sing()
