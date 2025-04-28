import random
import words


def getCategory():
    """
    Prompts the user to select a category for the game.
    Returns:
        int: The number corresponding to the selected category.
    """

    print("""\nEnter the number of the category you want to play:\n
    1. Plant\n
    2. Animal\n
    3. Country\n
    4. Food\n
    5. Sport\n
    """)
    
    while True:
        try:
            category = int(input("Enter a number of your category: "))
            if category in [1, 2, 3, 4, 5]:
                break
            else:
                print("Please enter a valid number for the category.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    return category


isGameOver = False

def readFile(filename):
    """
    Reads the contents of a file and returns the data as a list of lines.
    Args:
        filename (str): The name of the file to read.
    Returns:
        list: A list of lines from the file.
    """

    with open(filename, 'r') as file:
        data = file.readlines()
        return data
    
def getWord(word_list):
     """
    Selects a random word from a list of words.
    Args:
        word_list (list): A list of words.
    Returns:
        str: A randomly selected word.
    """
     
     word = random.choice(word_list)
     return word.strip()

def blackOutWord(word):
    """
    Replaces all but one random letter in the word with underscores.
    Args:
        word (str): The word to be blacked out.
    Returns:
        str: The word with all but one letter replaced by underscores.
    """

    letterIndex = random.randint(0, len(word) - 1)
    hintLetter = word[letterIndex]
    for i in range(len(word)):
        if word[i] != hintLetter:
            word = word.replace(word[i], "_")
    return word


def guessWordInput():
    """
    Prompts the user to input a guess and validates the input.
    Returns:
        str: The user's guess in lowercase.
    """

    while True:
        user_input = input("Enter your guess: ")
        if user_input and user_input.isalpha():
            break
        else:
            print("Please enter a valid word.")
    return user_input.lower()

    
    
def updateWordFromGuess(guess, word, blacked_out_word):
    """
    Updates the blacked-out word based on the user's correct guesses.
    Args:
        guess (str): The user's guess.
        word (str): The original word.
        blacked_out_word (str): The current state of the blacked-out word.
    Returns:
        str: The updated blacked-out word.
    """
    
    word_list = list(word)
    guessWord_list = list(guess)
    blacked_out_word = list(blacked_out_word)
    for x in guessWord_list:
        if x in word_list:
            for i in range(len(word)):
                if word[i] == x:
                    blacked_out_word[i] = word[i]
    blacked_out_word = "".join(blacked_out_word)
    return blacked_out_word


def isCorrectGuess(guess, word):
    """
    Checks if the user's guess is correct.
    Args:
        guess (str): The user's guess.
        word (str): The original word.
    Returns:
        bool: True if the guess is correct, False otherwise.
    """

    if guess in word:
        return True
    else:
        return False
    
    
def drawHangman(lives):
    """
    Displays the hangman drawing based on the number of lives remaining.
    Args:
        lives (int): The number of lives remaining.
    """

    match lives:
        case 4:
            print("""/----\n|\n|\n|\n|\n_______""")
        case 3:
            print("""/----\n|   0\n|\n|\n|\n_______""")
        case 2:
           print("""/----\n|   0\n|  /|\\\n|\n|\n_______""") 
        case 1:
            print("""/----\n|   0\n|  /|\\\n|   |\n|\n_______""") 
        case 0:
            print("""/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______""")
            gameOver()

def gameOpening():
    """
    Displays the opening screen of the game.
    """

    print(r"""
            *********************************************************************
            *                  _                                 _              *
            *    __      _____| | ___ ___  _ __ ___   ___       | |_ ___        *
            *    \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \      | __/ _ \       *
            *     \ V  V /  __/ | (_| (_) | | | | | |  __/      | || (_) |      *
            *     _\_/\_/ \___|_|\___\___/|_| |_| |_|\___|       \__\___/       *
            *    | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __                  *
            *    | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \                 *
            *    |  _  | (_| | | | | (_| | | | | | | (_| | | | |                *
            *    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|                *
            *                       |___/                                       *
            *********************************************************************
            """)
    print("\nYou have 5 lives to guess the word.")
    print("Good luck!\n")


def gameOver():
    """
    Displays the game over screen.
    """

    print(r"""
            ****************************************************************************
            *                                                                          *
            *                                                                          *
            *       ____                           ___                   _   _   _     *
            *      / ___| __ _ _ __ ___   ___     / _ \__   _____ _ __  | | | | | |    *
            *     | |  _ / _` | '_ ` _ \ / _ \   | | | \ \ / / _ \ '__| | | | | | |    *
            *     | |_| | (_| | | | | | |  __/   | |_| |\ V /  __/ |    |_| |_| |_|    *
            *      \____|\__,_|_| |_| |_|\___|    \___/  \_/ \___|_|    (_) (_) (_)    *
            *                                                                          *
            *                                                                          *
            *                                                                          *
            ****************************************************************************
            """)
    
def lives(initial_lives):
    """
    Decreases the player's lives by 1 and displays the updated hangman drawing.
    Args:
        initial_lives (int): The current number of lives.
    Returns:
        int: The updated number of lives.
    """

    initial_lives -= 1
    drawHangman(initial_lives)
    print(f"Lives left: {initial_lives}")
    return initial_lives 
    
      
def runGame():
    """
    Runs the main game loop, handling user input, word updates, and game state.
    """

    initial_lives = 5
    gameOpening()
    word_list = readFile("words.txt") 
    word = getWord(word_list)
    blacked_out_word = blackOutWord(word)
    print(f"The word: {blacked_out_word}") 
     
    while not isGameOver or initial_lives == 0:
        guess = guessWordInput()
        blacked_out_word = updateWordFromGuess(guess, word, blacked_out_word)
        if isCorrectGuess(blacked_out_word, word) and "_" not in blacked_out_word:
            print("Congratulations! You've guessed the word!")
            break
        initial_lives = lives( initial_lives)
        if initial_lives == 0:
            print(f"The word was '{word}'")
            break

        print(f"The word: {blacked_out_word}")
   

if __name__ == "__main__":
    user_category = getCategory()
    words.get_words(user_category)
    runGame()


