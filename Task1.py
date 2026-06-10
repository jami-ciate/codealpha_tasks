import random

words = ["python", "college", "laptop", "gaming", "friend"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display_word = ["_"] * len(word)

print("= HANGMAN GAME =")

while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong Guess!")
        wrong_guesses += 1

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)