import random


def hangTheTraitor():
    if wrongCount == 0:
        print('''|---|
|
|
|
|
|
|___
''')
    if wrongCount == 1:
        print('''|---|
|   O
|
|
|
|
|___
''')
    if wrongCount == 2:
        print('''|---|
|   O
|   |
|
|
|
|___
''')
    if wrongCount == 3:
        print('''|---|
|   O
|   |
|   |
|
|
|___
''')
    if wrongCount == 4:
        print('''|---|
|   O
|   |
|   |
|  /
|
|___
''')
    if wrongCount == 5:
        print('''|---|
|   O
|   |
|   | 
|  / \ 
|
|___
''')
    if wrongCount == 6:
        print('''|---|
|   O
|  \|
|   |
|  / \ 
|
|___
''')
    if wrongCount == 7:
        print('''|---|
|   O
|  \|/
|   | 
|  / \ 
|
|___
''')
        print("You Lose")
        print(f"Correct word: {word}")


def selectWord():
    file = open('hangmanWords.txt')
    words = file.readlines()
    myWord = random.choice(words)
    return myWord


##################################################################################
word = selectWord()  # the correct word
letters = []  # letters of the correct word
secret = []  # the word with blank letters
guessList = []  # the letters already guessed
acceptedCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wrongCount = 0  # the number of wrong guesses

# set up game
for i in range(len(word) - 1):
    letters.append(word[i])
    secret.append("_")

print("Let's Play Hangman")
hangTheTraitor()

# game loop
while wrongCount < 7:
    print(" ".join(secret))
    guess = input(">").lower()
    if len(guess) != 1 or guess not in acceptedCharacters:
        print("Please type a letter.")
    elif guess not in guessList:
        guessList.append(guess)
        try:
            if letters.index(guess) is not None:
                print("Correct!")
                for x in range(len(letters)):
                    if guess == letters[x]:
                        secret[x] = guess
        except ValueError:
            wrongCount += 1
            print("Wrong!")
            hangTheTraitor()
    else:
        print(f"You've already guessed {guess}")
    if secret == letters:
        print(" ".join(secret))
        print("You win!")
        break
