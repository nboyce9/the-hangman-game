import requests
import json

def writeToFile(words):
    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

def get_words():
    # url = "https://www.wordgamedb.com/api/v1/words/random/"

    category = 'plant'
    numLetters = 5
    url = f"https://www.wordgamedb.com/api/v1/words/?category={category}&numLetters={numLetters}"

    response = requests.get(url)
    if response.status_code == 200:
        x = response.json()
        words= []
        for i in x:
            words.append(i["word"])
        
    else:
        print("Error:", response.status_code)
        return None
    writeToFile(words)
    

    
# if __name__ == "__main__":
#     words = get_words()
#     writeToFile(words)