myList = [18, 25, 30, 14]

for num in myList:
    if num == 30:
        break  # ! If the num equals defined variable. Stop the loop.
    print(num)

print("**************")

for num in myList:
    if num == 30:
        # ! If the num equals defined variable. This time pass the defined value and continue next variable.
        continue
    print(num)

print("**************")

for no in myList:
    # ! If we are not going to give value yet, we can use the "pass" keyword.
    pass
