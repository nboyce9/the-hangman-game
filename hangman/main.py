import random



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
    user_input = input("Enter your guess: ")
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
            gameOver()

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
    
def lives(initial_lives, word):
    initial_lives -= 1
    drawHangman(initial_lives)
    print(f"Lives left: {initial_lives}")
    return initial_lives 
    
      
def runGame():
    initial_lives = 5
    gameOpening()
    word_list = readFile("words.txt") 
    word = getWord(word_list)
    blacked_out_word = blackOutWord(word)
    print(f"Random word: {word}")
    print(f"The word: {blacked_out_word}") 
     
    while not isGameOver or initial_lives == 0:
        guess = guessWordInput()
        blacked_out_word = updateWordFromGuess(guess, word, blacked_out_word)
        if isCorrectGuess(guess, word) and "_" not in blacked_out_word:
            print("Congratulations! You've guessed the word!")
            break
        initial_lives = lives( initial_lives, word)
        if initial_lives == 0:
            print(f"The word was '{word}'")
            break

        print(f"The word: {blacked_out_word}")
   

if __name__ == "__main__":
    print(getCategory())
    runGame()


