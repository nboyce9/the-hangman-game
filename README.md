# **The Hangman Game**

## **Overview**
The Hangman Game is a Python-based word-guessing game where players attempt to guess a randomly selected word by guessing letters or the entire word. The game provides categories for word selection and includes a visual representation of the hangman as lives are lost.

---

## **Features**
- **Category Selection**: Choose from five categories: Plant, Animal, Country, Food, and Sport.
- **Random Word Selection**: Words are fetched from a predefined list or an external API.
- **Hint System**: One letter of the word is revealed as a hint.
- **Lives and Hangman Drawing**: Lose a life for each incorrect guess, with a visual hangman representation.
- **Game Over Screen**: Displays a congratulatory or failure message based on the outcome.

---

## **Setup and Installation**

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:nboyce9/the-hangman-game.git
   cd the-hangman-game
   ```
2. **Install Python**:
   Download and install Python from the [official website](https://www.python.org/downloads/) if it is not already installed. Alternatively, use the following command:
   ```bash
   sudo apt-get install python3
   ```
   *(For Debian-based systems like Ubuntu)*

3. **Install Dependencies**:
   Install the `requests` library using:
   ```bash
   pip install requests
   ```

---

## **How to Play**
1. Start the game by running the command <python3 -m hangman.main> in your terminal
2. Select a category from the available options.
3. Guess letters or the entire word to uncover the hidden word.
4.Avoid incorrect guesses to preserve your lives and win the game!

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.



