import requests
import json

def writeToFile(words):
    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

def get_words():
    # url = "https://www.wordgamedb.com/api/v1/words/random/"

    category = 'country'
    words = []
    for i in range(3, 13):
        url = f"https://www.wordgamedb.com/api/v1/words/?category={category}&numLetters={i}"

        response = requests.get(url)
        if response.status_code == 200:
            x = response.json()
            for item in x:
                print(item["word"])
                words.append(item["word"])
        else:
            print("Error:", response.status_code)
            return []
    writeToFile(words)
    return words
    

    
if __name__ == "__main__":
    words = get_words()
    writeToFile(words)