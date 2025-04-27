import random

# def getLevel():
#     level = input("Enter the level (e.g 1 for 'Beginner'): ")
#     return level


# def getCategory():
#     category = input("Enter the category (e.g 1 for 'Fruits'): ")
#     return category
isGameOver = False

def readFile(filename):
    with open(filename, 'r') as file:
            data = file.readlines()
            # print(data)
            return data
    
def getWord(word_list):
     word = random.choice(word_list)
     return word.strip()

def blackOutWord(word):
    letterIndex = random.randint(0, len(word) - 1)
    hintLetter = word[letterIndex]
    for i in range(len(word)):
        if word[i] != hintLetter:
            word = word.replace(word[i], "_")
    return word

def guessWordInput():
    user_input = input("Enter your guessed word: ")
    return user_input

    
    
def updateWordFromGuess(guess, word, blacked_out_word):
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
    if guess in word:
        return True
    else:
        return False
    
def drawHangman(lives):
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

def gameOpening():
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
    
    
def runGame():
    initial_lives = 5
    gameOpening()
    word_list = readFile("temp_words.txt")
    word = getWord(word_list)
    blacked_out_word = blackOutWord(word)
    print(f"Random word: {word}")
    print(f"Blacked out word: {blacked_out_word}")
    while not isGameOver:
        guess = guessWordInput()
        blacked_out_word = updateWordFromGuess(guess, word, blacked_out_word)
        if isCorrectGuess(guess, word):
            print("Congratulations! You've guessed the word!")
            break
        else:
            print(f"Updated word: {blacked_out_word}")
        initial_lives -= 1
        drawHangman(initial_lives)
        if initial_lives == 0:
            gameOver()
            print(f"The word was '{word}'")
            break
        print(f"Lives left: {initial_lives}")
        print(f"Blacked out word: {blacked_out_word}")

    


     
     

if __name__ == "__main__":
    # level = getLevel()
    # category = getCategory()
    # print(f"Level: {level} in {category} category")
    runGame()


