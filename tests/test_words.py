import unittest
import hangman.words as words


class TestMain(unittest.TestCase):
    def test_getCategoryString(self):
        userInput = 2
        result = "animal"
        self.assertEqual(result, words.getCategoryString(userInput))

    