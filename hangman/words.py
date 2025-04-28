import requests
import json

def writeToFile(words):
    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")


def getCategoryString( category):
    match category:
        case 1:
            category = "plant"
        case 2: 
            category = "animal"
        case 3:
            category = "country"
        case 4: 
            category = "food"
        case 5: 
            category = "sport"
    return category


def get_words(category):
    # url = "https://www.wordgamedb.com/api/v1/words/random/"

    categ = getCategoryString(category)
    words = []
    for i in range(3, 13):
        url = f"https://www.wordgamedb.com/api/v1/words/?category={categ}&numLetters={i}"

        response = requests.get(url)
        if response.status_code == 200:
            x = response.json()
            for item in x:
                words.append(item["word"])
        else:
            print("Error:", response.status_code)
            return []
        
    writeToFile(words)
    return words
