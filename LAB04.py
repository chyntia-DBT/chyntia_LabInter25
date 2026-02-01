secret_words = ["red", "blue", "green"]

wins = 0
losses = 0

def choose_word(words):
    word = word[0]
    words.remove(word)
    return word

def display_word(secret,guessed):
    text =""
    for letter in secret:
        if letter in guessed:
            text += letter + " "
        else:
            text += "_"
    return text
while len(secret_words) > 0:

    secret_word = choose_word(secret_words)
    guessed_letters = []
    chances = 5

print("|nNew word!")

while chances > 0:

    print("Word:", display_word(secret_word, guessed_letters))
    print("Chances:", chances)

guess = input("Guess a letter: ").lower()

if not guess.isalpha():
    print("Input must be a letter!")
    continue

if guess in guessed_letters:
    print("Already guessed!")
    continue

guessed_letters.append(guess)

if guess in secret_word:
    print("Correct!")
else:
    print("Wrong!")
    chances -= 1

if "_" not in display_word(secret_word, guessed_letters):
    print("You Win!")
    wins += 1
    break

if chances == 0:
    print("You Lose! Word was:", secret_word)
    losses += 1

print("Score-Wins", wins, "Losseds:", losses)

again = input("Play again? (yes/no)").lower()
if again == "no":
    break

print("\nFinal Score")
print("Wins:", wins)
print("Losses:", losses)
print("Game Over")




