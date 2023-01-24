# Cannot be same element inside of set.
myList = [1, 2, 3, 1]
print(myList)
print(type(myList))
# Castting
#! We can cast the list to set, or the exact opposite.
#! set(), list(), dict(), tuple()
#!
myset = set(myList)
print(type(myset))
print(myset)

myset2 = {1, 2, 3, 1}
print(myset2)

myset3 = {"a", "b", "a"}  # ! Sets cannot be loop same element.
print(myset3)

myset4 = {}  # ! If we put empty the brackets. Default situtation is "Dictionary"
myset4 = set()  # ! That's why we have to define "set()".
myset4.add(1)
print(myset4)
