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
     
     

if __name__ == "__main__":
    # level = getLevel()
    # category = getCategory()
    # print(f"Level: {level} in {category} category")
    word_list = readFile("temp_words.txt")
    word = getWord(word_list)
    print(f"Random word: {word}")

