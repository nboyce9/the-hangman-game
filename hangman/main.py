import random

# def getLevel():
#     level = input("Enter the level (e.g 1 for 'Beginner'): ")
#     return level


# def getCategory():
#     category = input("Enter the category (e.g 1 for 'Fruits'): ")
#     return category


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
    


     
     

if __name__ == "__main__":
    # level = getLevel()
    # category = getCategory()
    # print(f"Level: {level} in {category} category")
    word_list = readFile("temp_words.txt")
    word = getWord(word_list)
    print(f"Random word: {word}")
    blacked_out_word = blackOutWord(word)
    print(f"Blacked out word: {blacked_out_word}")
    guess = guessWordInput()
    print(updateWordFromGuess(guess, word, blacked_out_word))


