@@ -1,3 +1,93 @@
@@ -1,3 +1,95 @@
'''Implement your solution in this file.
Make sure that you decompose your solution into appropriate 
functions and that you include appropriate documentation.'''
functions and that you include appropriate documentation.'''
functions and that you include appropriate documentation.'''
import random
import string
def load_words():
    # Load words from the words.txt file
    try:
        with open("words.txt", "r") as file:
            word_list = file.read().split()
        return word_list
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        return []
def choose_word(word_list):
    return random.choice(word_list) if word_list else ""
def hangman():
    word_list = load_words()
    
    if not word_list:
        return  # Exit the game if no words are available
    
    secret_word = choose_word(word_list).lower()
    unique_letters = set(secret_word)
    
    guesses_remaining = 10
    warnings_remaining = 3
    letters_guessed = set()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_remaining > 0:
        print("-" * 20)
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"Warnings remaining: {warnings_remaining}")
        print("Letters not yet guessed:", ''.join(sorted(set(string.ascii_lowercase) - letters_guessed)))
        
        # Display the current guessed word
        guessed_word = ''.join([char if char in letters_guessed else '-' for char in secret_word])
        print(f"Current word: {guessed_word}")
        
        # Check if the word has been guessed
        if unique_letters <= letters_guessed:
            print(f"Congratulations, you guessed the word: {secret_word}!")
            score = guesses_remaining * len(unique_letters)
            print(f"Your score is: {score}")
            return
        
        # Get user's guess
        guess = input("Please guess a letter: ").lower()
        
        # Handle invalid input
        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Invalid input! You have {warnings_remaining} warnings left.")
            else:
                guesses_remaining -= 1
                print(f"Invalid input! You lost a guess. Guesses remaining: {guesses_remaining}")
            continue
        
        # Handle already guessed letters
        if guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"You've already guessed that letter! Warnings left: {warnings_remaining}")
            else:
                guesses_remaining -= 1
                print(f"You've already guessed that letter! Guesses remaining: {guesses_remaining}")
            continue
        
        # Add guess to the set of guessed letters
        letters_guessed.add(guess)
        
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good guess: {guessed_word}")
        else:
            if guess in vowels:
                guesses_remaining -= 2
                print(f"The letter '{guess}' is not in the word. You lost 2 guesses.")
            else:
                guesses_remaining -= 1
                print(f"The letter '{guess}' is not in the word. You lost 1 guess.")
        
    # If the loop ends, the player has run out of guesses
    print(f"Sorry, you've run out of guesses. The word was: {secret_word}. Better luck next time!")
# Run the game
hangman()
