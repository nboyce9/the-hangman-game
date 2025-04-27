import unittest
import hangman.main as main


class TestMain(unittest.TestCase):

    def test_getWord(self):
        # Test if the getWord function returns a word from the list
        word_list = ["apple", "banana", "cherry"]
        result = main.getWord(word_list)
        self.assertIn(result, word_list)  # Check if the result is in the list


if __name__ == "__main__":
    unittest.main()