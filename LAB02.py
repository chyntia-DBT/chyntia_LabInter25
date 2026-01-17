secret_word = "victor"
guesses = set()
attempts = 6

print("hangman 2.0")

while attempts > 0:
    guess = input("insert the letter: ").lower()

    if guess in guesses:
        print("Already guessed")
        continue

    guesses.add(guess)

    if guess in secret_word:
        print("correct!")
    else:
        print("incorrect")

    attempts -= 1

    display = ""
    solved = True

    for letter in secret_word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
            solved = False

    print("word:", display)
    print("Attempts left:", attempts)

    if solved:
        print("YOU WIN 🎉")
        break

if not solved:
    print("Game Over")

     


