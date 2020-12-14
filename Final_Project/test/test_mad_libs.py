import unittest
from mad_libs import MadLib
from story_templates import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.madlib = MadLib()

    def test_object_created(self):
        # Test object attributes
        self.assertEqual(self.madlib.story, 'None')
        self.assertEqual(self.madlib.word_dict, {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': [], 'Place': []})

    def test_set_story(self):
        # Test set story method
        self.madlib.set_story(star_wars_story)
        self.assertEqual(self.madlib.story, star_wars_story)

    def test_use_word_bank(self):
        # Test use word bank method
        self.madlib.use_word_bank()
        self.assertEqual(self.madlib.word_dict, {'Noun': ['sock', 'ball', 'hat', 'mouse'], 'Verb': ['run', 'swim', 'bark', 'cry'],
                                                 'Adjective': ['red', 'small', 'big', 'angry', 'happy'], 'Adverb': ['happily', 'intensely', 'anxiously', 'hopelessly'],
                                                 'Plural noun': ['toes', 'frogs', 'pillows', 'candy bars'], 'Past tense verb': ['sprinted', 'yelled', 'cried', 'panicked'],
                                                 'Name': ['Obama', 'Dwayne Johnson', 'Tom Hanks', 'Taylor Swift'], 'Place': ['New York', 'China', 'Iowa', 'Berlin']})

    def test_check_word_bank(self):
        # Test check word bank - Empty word bank
        self.assertEqual(self.madlib.check_word_bank(), {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': [], 'Place': []})

        # Test check word bank - Non empty word bank
        self.madlib.add_word('Name', "Dylan")
        self.madlib.add_word('Place', "Des Moines")
        self.assertEqual(self.madlib.check_word_bank(), {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': ["Dylan"], 'Place': ["Des Moines"]})

    def test_add_word_good_input(self):
        # Test add word - Valid words
        self.madlib.add_word('Noun', "rock")
        self.assertEqual(self.madlib.word_dict['Noun'], ['rock'])

        self.madlib.add_word('Verb', "run")
        self.assertEqual(self.madlib.word_dict['Verb'], ['run'])

        self.madlib.add_word('Adjective', "tall")
        self.assertEqual(self.madlib.word_dict['Adjective'], ['tall'])

        self.madlib.add_word('Adverb', "softly")
        self.assertEqual(self.madlib.word_dict['Adverb'], ['softly'])

        self.madlib.add_word('Plural noun', "socks")
        self.assertEqual(self.madlib.word_dict['Plural noun'], ['socks'])

        self.madlib.add_word('Past tense verb', "wrote")
        self.assertEqual(self.madlib.word_dict['Past tense verb'], ['wrote'])

        self.madlib.add_word('Name', "Dylan")
        self.assertEqual(self.madlib.word_dict['Name'], ['Dylan'])

        self.madlib.add_word('Place', "Des Moines")
        self.assertEqual(self.madlib.word_dict['Place'], ['Des Moines'])

    def test_add_word_bad_input(self):
        # Test add word - Invalid words, returns 0
        self.assertEqual(self.madlib.add_word('Noun', "25"), 0)

        self.assertEqual(self.madlib.add_word('Verb', "$$"), 0)

        self.assertEqual(self.madlib.add_word('Adjective', "*@"), 0)

        self.assertEqual(self.madlib.add_word('Adverb', "267%"), 0)

        self.assertEqual(self.madlib.add_word('Plural noun', "socks3"), 0)

        self.assertEqual(self.madlib.add_word('Past tense verb', "(wrote)"), 0)

        self.assertEqual(self.madlib.add_word('Name', "Dylan+THOMAS"), 0)

        self.assertEqual(self.madlib.add_word('Place', "Des Moines:::"), 0)

    def test_clear_dict(self):
        # Test clear dict - Empty dict
        self.madlib.clear_dict()
        self.assertEqual(self.madlib.word_dict, {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': [], 'Place': []})

        # Test clear dict - Not empty
        self.madlib.word_dict = {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': ["Dylan"], 'Place': ["Des Moines"]}
        self.madlib.clear_dict()
        self.assertEqual(self.madlib.word_dict, {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': [], 'Place': []})

    def test_find_word(self):
        # Test find word - (Random, but should return from the available words in the dict)
        self.madlib.use_word_bank()
        self.assertIn(self.madlib.find_word('Noun', self.madlib.word_dict), ['sock', 'ball', 'hat', 'mouse'])
        self.assertIn(self.madlib.find_word('Verb', self.madlib.word_dict), ['run', 'swim', 'bark', 'cry'])
        self.assertIn(self.madlib.find_word('Adjective', self.madlib.word_dict), ['red', 'small', 'big', 'angry', 'happy'])
        self.assertIn(self.madlib.find_word('Adverb', self.madlib.word_dict), ['happily', 'intensely', 'anxiously', 'hopelessly'])

        self.assertIn(self.madlib.find_word('Plural noun', self.madlib.word_dict), ['toes', 'frogs', 'pillows', 'candy bars'])
        self.assertIn(self.madlib.find_word('Past tense verb', self.madlib.word_dict), ['sprinted', 'yelled', 'cried', 'panicked'])
        self.assertIn(self.madlib.find_word('Name', self.madlib.word_dict), ['Obama', 'Dwayne Johnson', 'Tom Hanks', 'Taylor Swift'])
        self.assertIn(self.madlib.find_word('Place', self.madlib.word_dict), ['New York', 'China', 'Iowa', 'Berlin'])

    def test_create_story_insufficient_words(self):
        # Test create story insufficient words - No words in dict
        self.madlib.word_dict = {'Noun': [], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': [], 'Past tense verb': [], 'Name': [], 'Place': []}
        self.madlib.set_story(dog_story)
        self.assertEqual(self.madlib.create_story(), "InsufficientWordsError: Not enough words for this story, continue entering words\n")

        # Test create story insufficient words - Some words, but not all required
        self.madlib.word_dict = {'Noun': ['sock', 'ball'], 'Verb': [], 'Adjective': [], 'Adverb': [], 'Plural noun': ['toes'], 'Past tense verb': [], 'Name': ['Betty', 'Bill'], 'Place': []}
        self.assertEqual(self.madlib.create_story(), "InsufficientWordsError: Not enough words for this story, continue entering words\n")

    def tearDown(self):
        del self.madlib


if __name__ == '__main__':
    unittest.main()
