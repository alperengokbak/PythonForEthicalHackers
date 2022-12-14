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
