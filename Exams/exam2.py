name = input("Name: ")
print("Hello " + name + " time to play hangman!")

word = "Endless"
guessString = ""
remainingLife = 10

while ((remainingLife != 0)):
    characterLeft = 0

    for letter in word:
        if letter in guessString:
            print(letter)
        else:
            print("-")
            characterLeft += 1
    if (characterLeft == 0):
        print("You have found the word!!")
        break

    guessWord = input("Guess a letter: ")
    guessString += guessWord

    if guessWord not in word:
        remainingLife -= 1
        print("Wrong!")
        print(f"You have left {remainingLife} life.")

    if (remainingLife == 0):
        print("You have no left life!!!")
        break
