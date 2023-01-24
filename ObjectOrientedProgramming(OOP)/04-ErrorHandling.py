def numberPower(num1):
    return num1 ** 2


#! If users entry except number, our program will crash. We don't want happening that. That's why we create "Try, Expect, Finally"
# Try, Expect, Finally

while True:
    try:
        num = int(input("Enter the number: "))
    except:
        print("You must enter the number!!")
        continue
    else:
        print("Ok")
        break
    finally:  # ! Finally keyword will run everytime, even users enter invalid variables too.
        print("Finally!")
