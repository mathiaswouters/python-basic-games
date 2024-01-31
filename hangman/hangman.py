import random

def initialize_game():
    user_name = input("Enter your name: ")
    print("Hello " + user_name + ", you are going to play hangman.\nHave fun !!!")
    print("\n-------------------------------------------------------------------------------------\n")

    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

    random_word = random.choice(words)
    words_length = len(random_word)
    print("The number of letters in the word is: " + str(words_length))
    
    return random_word, words_length

def play_hangman(random_word, words_length):
    guess_attempts = 7  # Initialize the number of guess attempts.
    correct_guesses = ""  # Initialize a string to store correct guesses.
    displayed_word = ["*"] * words_length  # Initialize the displayed word as asterisks.

    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    while guess_attempts > 0:
        # Print the current hangman stage.
        print(hangman_stages[7 - guess_attempts])

        # Display the current state of the word with asterisks and guessed letters.
        print("".join(displayed_word))

        # Get a letter guess from the player and convert it to lowercase.
        attempt = input("Enter a letter: ").lower()

        # Check if the input is valid (a single letter).
        if len(attempt) != 1 or not attempt.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the guessed letter is correct.
        if attempt in random_word and attempt not in correct_guesses:
            print("Correct!")
            correct_guesses += attempt
            for i in range(words_length):
                if random_word[i] == attempt:
                    displayed_word[i] = attempt
        else:
            print("Incorrect!")
            if guess_attempts == 1:
                # If it's the last guess, print the final hangman stage.
                print(hangman_stages[6])
            guess_attempts -= 1  # Decrement guess attempts only for incorrect guesses.

        # Display the number of remaining guess attempts.
        print("You can guess " + str(guess_attempts) + " more times")

        # Check if the player has guessed the entire word correctly.
        if "".join(displayed_word) == random_word:
            print("Congratulations! You've won. The word is: " + random_word)
            return

    # If the player runs out of guess attempts, display the correct word.
    print("Sorry, you've run out of guesses. The word was: " + random_word)

if __name__ == "__main__":
    random_word, words_length = initialize_game()
    play_hangman(random_word, words_length)
