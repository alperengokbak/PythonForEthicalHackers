a = 0
while a < 5:
    print(a)
    # ! Normally, we can increase the value of a like that, a++. but python not allow.
    a += 1

mylist = [1, 2, 3, 4, 5]

# ! "in" keyword controls the whether it is or not inside of the list.
while (3 in mylist):
    mylist.pop()
    print(mylist)
    print("******")

p = 0
while p < 20:
    # ! We display the value of the p with three different ways.
    print("Value p: ", p)
    print("Value p: ", p)
    # ! We say formatting, If we want to display the p, use the "f"
    print(f"Value p: {p}")
    p += 1
