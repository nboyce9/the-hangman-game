import requests
import json


def writeToFile(words):
    """
    Writes a list of words to a file named 'words.txt'.
    Args:
        words (list): A list of words to write to the file.
    """

    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")


def getCategoryString( category):
    """
    Converts a numeric category input into its corresponding string representation.
    Args:
        category (int): The numeric category selected by the user.
    Returns:
        str: The string representation of the category (e.g., "plant", "animal").
    """

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
    """
    Fetches a list of words from an external API based on the selected category and word length.
    Args:
        category (int): The numeric category selected by the user.
    Returns:
        list: A list of words fetched from the API. If an error occurs, an empty list is returned.
    """
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
