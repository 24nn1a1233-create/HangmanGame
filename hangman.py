import random

words = ["python", "apple", "school", "computer", "flower"]

word = random.choice(words)

guessed = []

attempts = 6

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_ "

    print("\nWord:", display)

    if "_ " not in display:
        print("🎉 You Won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The word was:", word)