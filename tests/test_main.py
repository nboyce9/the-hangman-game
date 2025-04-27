import unittest
import hangman.main as main


class TestMain(unittest.TestCase):

    def test_getWord(self):
        # Test if the getWord function returns a word from the list
        word_list = ["apple", "banana", "cherry"]
        result = main.getWord(word_list)
        self.assertIn(result, word_list)

    def test_blackOutWord(self):
        word = "fleet"
        blacked_out_word = main.blackOutWord(word)
        # Check if the blacked out word has the same length as the original word
        self.assertEqual(len(blacked_out_word), len(word))

    def test_updateWordFromGuessCorrectLetter(self):
        word = "apple"
        blacked_out_word = "a____"
        guess = "p"
        updated_word = main.updateWordFromGuess(guess, word, blacked_out_word)
        # Check if the updated word has the correct letters revealed
        self.assertEqual(updated_word, "app__")
    
    def test_updateWordFromGuessIncorrectLetter(self):
        word = "apple"
        blacked_out_word = "a____"
        guess = "acorn"
        updated_word = main.updateWordFromGuess(guess, word, blacked_out_word)
        # Check if the updated word remains unchanged
        self.assertEqual(updated_word, "a____")


if __name__ == "__main__":
    unittest.main()