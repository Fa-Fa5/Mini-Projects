import random
from hangmanwords import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_blanks = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    print(word_blanks)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Guess a word or letter: ").upper()
        
        if len(guess) == 1 and guess.isalpha():  # Guessing a letter
            if guess in guessed_letters:
                print("Already guessed letter, you goldfish.")
            elif guess not in word:
                print("Not in word loser.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("You guessed it right nerd!")
                guessed_letters.append(guess)
                word_as_list = list(word_blanks)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_blanks = "".join(word_as_list)
                
                if "_" not in word_blanks:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # Guessing the whole word
            if guess in guessed_words:
                print("That's correct Brainyy!")
            elif guess != word:
                print("Wrong nigger.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_blanks = word
        else:
            print("Use your brain loser! It's not a letter!")
        
        print(display_hangman(tries))
        print(word_blanks)
        print("\n")
        
    if guessed:
        print("Look who got a brain! Where did you buy it? Congrats btw!")
    else:
        print(f"Haha you lose nigger! The word was '{word}'. Try again loser!")

def display_hangman(tries):
    stages = [
        """
        ___________
        |    |
        |    O
        |   \\|/
        |    |
        |    /\\ 
        """,
        """
        ___________
        |    |
        |    O
        |   \\|/
        |    |
        |    /
        """,
        """
        ___________
        |    |
        |    O
        |   \\|/
        |    |
        |    
        """,
        """
        ___________
        |    |
        |    O
        |   \\|
        |    |
        |   
        """,
        """
        ___________
        |    |
        |    O
        |    |
        |    |
        |    
        """,
        """
        ___________
        |    |
        |    O
        |    
        |    
        |    
        """,
        """
        ___________
        |    |
        |    
        |   
        |    
        |    
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Try again, loser? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()