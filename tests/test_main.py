import unittest
import hangman.main


class TestMain(unittest.TestCase):

    def test_getWord(self):
        # Test if the getWord function returns a word from the list
        word_list = ["apple", "banana", "cherry"]
        result = hangman.main.getWord(word_list)
        self.assertIn(result, word_list)

    def test_blackOutWord(self):
        word = "fleet"
        blacked_out_word = hangman.main.blackOutWord(word)
        # Check if the blacked out word has the same length as the original word
        self.assertEqual(len(blacked_out_word), len(word))

    def test_updateWordFromGuessCorrectLetter(self):
        word = "apple"
        blacked_out_word = "a____"
        guess = "p"
        updated_word = hangman.main.updateWordFromGuess(guess, word, blacked_out_word)
        # Check if the updated word has the correct letters revealed
        self.assertEqual(updated_word, "app__")
    
    def test_updateWordFromGuessIncorrectLetter(self):
        word = "apple"
        blacked_out_word = "a____"
        guess = "acorn"
        updated_word = hangman.main.updateWordFromGuess(guess, word, blacked_out_word)
        # Check if the updated word remains unchanged
        self.assertEqual(updated_word, "a____")
    
    def test_isCorrectGuessTrue(self):
        word = "apple"
        guess = "p"
        result = hangman.main.isCorrectGuess(guess, word)
        # Check if the guess is correct
        self.assertTrue(result)
    
    def test_isCorrectGuessFalse(self):
        word = "apple"
        guess = "z"
        result = hangman.main.isCorrectGuess(guess, word)
        # Check if the guess is incorrect
        self.assertFalse(result)

    def test_drawHangman(self):
        # Test if the drawHangman function prints the correct hangman state
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        hangman.main.drawHangman(3)
        sys.stdout = sys.__stdout__

        expected_output = "/----\n|   0\n|\n|\n|\n_______\n"
        self.assertEqual(captured_output.getvalue(), expected_output)         

    

if __name__ == "__main__":
    unittest.main()