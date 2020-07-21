import random

secret_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hyphen_word = "-" * len(secret_word)
mistakes = 0
guesses = set()

print("H A N G M A N")
decision = input('Type "play" to play the game, "exit" to quit:')
if decision not in ["play", "exit"]:
    decision = input('Type "play" to play the game, "exit" to quit:')
elif decision == "play":
    while mistakes < 8:
        print()
        print(hyphen_word)
        if hyphen_word is secret_word:
            print("""You guessed the word!
            You survived!
            
            """)
            decision = input('Type "play" to play the game, "exit" to quit:')
        else:
            guess = input("Input a letter: ")       
            if len(guess) != 1:
                print("You should input a single letter")
            elif not(guess.islower()):
                print("It is not an ASCII lowercase letter")
            else:            
                if guess in guesses:
                    print("You already typed this letter")
                elif guess not in secret_word:
                    print("No such letter in the word")
                    mistakes += 1
                else:
                    for j in range(len(secret_word)):
                        if guess == secret_word[j]:
                            listed_word = list(hyphen_word)
                            listed_word[j] = guess
                            hyphen_word = "".join(listed_word)
            guesses.add(guess)
    else:
        print("""You are hanged!
        """)
        decision = input('Type "play" to play the game, "exit" to quit:')