"""
Program: mad_libs.py
Author: Dylan Thomas
Last date modified: 12/13/2020 8:44PM
"""

from random import randint
from datetime import datetime
from tkinter import *
from story_templates import *
import copy
import textwrap


class MadLib:
    # Constructor
    def __init__(self):
        story = "None"
        self.story = story
        word_dict = {'Noun': [],
                     'Verb': [],
                     'Adjective': [],
                     'Adverb': [],
                     'Plural noun': [],
                     'Past tense verb': [],
                     'Name': [],
                     'Place': []}
        self.word_dict = word_dict

    def update_gui(self):
        # Create story button enabled
        create_button = Button(window, text="Create Story", width=35, borderwidth=5, state='normal', command=lambda: print(madlib.create_story() + '\n')).grid(row=9, column=0, columnspan=7, padx=10, pady=10)

        # Let the user know which story is currently selected using labels
        if self.story == dog_story:
            dog_selected = Label(window, text="*Dog Selected*", bg='#b2ffce', width=35, font=30).grid(row=4, column=0, columnspan=7)
        elif self.story == fish_story:
            fish_selected = Label(window, text="*Fish Selected*", bg='#b2ffce', width=35, font=30).grid(row=4, column=0, columnspan=7)
        elif self.story == star_wars_story:
            star_wars_selected = Label(window, text="*Star Wars Selected*", bg='#b2ffce', width=35, font=30).grid(row=4, column=0, columnspan=7)
        else:
            love_letter_selected = Label(window, text="*Love Letter Selected*", bg='#b2ffce', width=35, font=30).grid(row=4, column=0, columnspan=7)

    def set_story(self, story_choice):
        # Allows the use of separate buttons to set the object's story attribute
        self.story = story_choice

        # Function only needs called when a story is selected so is hidden from global scope
        def count_word_types():
            # Counts the number of words of each type the user will need to enter for each template
            global noun_count, verb_count, adj_count, adverb_count, plural_noun_count, past_tense_verb_count, name_count, place_count
            noun_count = 0
            verb_count = 0
            adj_count = 0
            adverb_count = 0
            plural_noun_count = 0
            past_tense_verb_count = 0
            name_count = 0
            place_count = 0

            words_in_story = self.story.split()

            for curr_word in words_in_story:
                if curr_word in nounStrings:
                    noun_count += 1
                elif curr_word in verbStrings:
                    verb_count += 1
                elif curr_word in adjStrings:
                    adj_count += 1
                elif curr_word in adverbStrings:
                    adverb_count += 1
                elif curr_word in pluralNounStrings:
                    plural_noun_count += 1
                elif curr_word in pastTenseVerbStrings:
                    past_tense_verb_count += 1
                elif curr_word in nameStrings:
                    name_count += 1
                elif curr_word in placeStrings:
                    place_count += 1

        # Call inner function
        count_word_types()

    def use_word_bank(self):
        # Allows the user to skip the process of entering words by means of a pre-made word dictionary
        self.word_dict = {'Noun': ['sock', 'ball', 'hat', 'mouse'],
                          'Verb': ['run', 'swim', 'bark', 'cry'],
                          'Adjective': ['red', 'small', 'big', 'angry', 'happy'],
                          'Adverb': ['happily', 'intensely', 'anxiously', 'hopelessly'],
                          'Plural noun': ['toes', 'frogs', 'pillows', 'candy bars'],
                          'Past tense verb': ['sprinted', 'yelled', 'cried', 'panicked'],
                          'Name': ['Obama', 'Dwayne Johnson', 'Tom Hanks', 'Taylor Swift'],
                          'Place': ['New York', 'China', 'Iowa', 'Berlin']}
        print("Using pre-made word bank.")
        self.check_words_needed()

    def check_word_bank(self):
        # Allows the user to check what words are currently in the word dictionary
        print(self.word_dict)
        return self.word_dict

    def check_words_needed(self):
        # Calculates and displays the number of each type of word the user still needs to enter or tells the user they have enough to complete the currently selected story
        global noun_count, verb_count, adj_count, adverb_count, plural_noun_count, past_tense_verb_count, name_count, place_count

        if noun_count > len(self.word_dict['Noun']):
            print("Nouns needed: ", (noun_count - len(self.word_dict['Noun'])))
        if verb_count > len(self.word_dict['Verb']):
            print("Verbs needed: ", (verb_count - len(self.word_dict['Verb'])))
        if adj_count > len(self.word_dict['Adjective']):
            print("Adjectives needed: ", (adj_count - len(self.word_dict['Adjective'])))
        if adverb_count > len(self.word_dict['Adverb']):
            print("Adverbs needed: ", (adverb_count - len(self.word_dict['Adverb'])))

        if plural_noun_count > len(self.word_dict['Plural noun']):
            print("Plural Nouns needed: ", (plural_noun_count - len(self.word_dict['Plural noun'])))
        if past_tense_verb_count > len(self.word_dict['Past tense verb']):
            print("Past Tense Verbs needed: ", (past_tense_verb_count - len(self.word_dict['Past tense verb'])))
        if name_count > len(self.word_dict['Name']):
            print("Names needed: ", (name_count - len(self.word_dict['Name'])))
        if place_count > len(self.word_dict['Place']):
            print("Places needed: ", (place_count - len(self.word_dict['Place'])))
        print("\n")

        # Let the user know they have enough words to create the story
        if self.story != "None":
            if (noun_count <= len(self.word_dict['Noun'])) and \
                    (verb_count <= len(self.word_dict['Verb'])) and \
                    (adj_count <= len(self.word_dict['Adjective'])) and \
                    (adverb_count <= len(self.word_dict['Adverb'])) and \
                    (plural_noun_count <= len(self.word_dict['Plural noun'])) and \
                    (past_tense_verb_count <= len(self.word_dict['Past tense verb'])) and \
                    (name_count <= len(self.word_dict['Name'])) and \
                    (place_count <= len(self.word_dict['Place'])):

                print("Enough words included, create story or continue adding words!\n")

    def add_word(self, word_type, word):
        # Add word to word dictionary and call check words needed, input is validated to ensure no numbers or special characters entered
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")

        try:
            if not word_characters.issuperset(word):
                raise InvalidCharacterError
            else:
                self.word_dict[word_type].append(word)
                print(word_type, "added:", word, "\n....................")

                # Call count needed to tell the user what they still need to input
                self.check_words_needed()
        except InvalidCharacterError:
            print("InvalidCharacterError: Number or special character entered, please enter a word!\n")
            return 0

    def clear_dict(self):
        # Resets the word dictionary to be empty
        self.word_dict = {'Noun': [],
                          'Verb': [],
                          'Adjective': [],
                          'Adverb': [],
                          'Plural noun': [],
                          'Past tense verb': [],
                          'Name': [],
                          'Place': []}
        print("Words reset.\n")

    @staticmethod
    def find_word(word_type, current_dict):
        # Pop a random word of the correct type from the word dictionary for use in creating the story
        words = current_dict[word_type]
        count = len(words) - 1
        index = randint(0, count)

        return current_dict[word_type].pop(index)

    def create_story(self):
        # Creates a story if the user has enough words and outputs it to the console and the output file
        try:
            # Prevents use if there are not enough words in the word bank
            if (noun_count > len(self.word_dict['Noun'])) or \
                        (verb_count > len(self.word_dict['Verb'])) or \
                        (adj_count > len(self.word_dict['Adjective'])) or \
                        (adverb_count > len(self.word_dict['Adverb'])) or \
                        (plural_noun_count > len(self.word_dict['Plural noun'])) or \
                        (past_tense_verb_count > len(self.word_dict['Past tense verb'])) or \
                        (name_count > len(self.word_dict['Name'])) or \
                        (place_count > len(self.word_dict['Place'])):
                raise InsufficientWordsError
            else:
                # Create a copy of the word dictionary to be able to remove words as they are used leaving the original dictionary intact
                copy_dict = copy.deepcopy(self.word_dict)

                # Splits the story into a list of individual words
                words_in_story = self.story.split()

                # Main loop, goes through the list searching for keywords and replacing them with words from the user's copied word dictionary
                # Using 'in' to keep punctuation intact, ie 'adjective!' will still be found and changed appropriately
                curr_index = 0
                for curr_word in words_in_story:
                    if curr_word in nounStrings:
                        if curr_word == 'noun':
                            words_in_story[curr_index] = self.find_word('Noun', copy_dict)
                            curr_index += 1
                        elif curr_word == 'noun.':
                            words_in_story[curr_index] = self.find_word('Noun', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'noun!':
                            words_in_story[curr_index] = self.find_word('Noun', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'noun?':
                            words_in_story[curr_index] = self.find_word('Noun', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'noun,':
                            words_in_story[curr_index] = self.find_word('Noun', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in verbStrings:
                        if curr_word == 'verb':
                            words_in_story[curr_index] = self.find_word('Verb', copy_dict)
                            curr_index += 1
                        elif curr_word == 'verb.':
                            words_in_story[curr_index] = self.find_word('Verb', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'verb!':
                            words_in_story[curr_index] = self.find_word('Verb', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'verb?':
                            words_in_story[curr_index] = self.find_word('Verb', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'verb,':
                            words_in_story[curr_index] = self.find_word('Verb', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in adjStrings:
                        if curr_word == 'adjective':
                            words_in_story[curr_index] = self.find_word('Adjective', copy_dict)
                            curr_index += 1
                        elif curr_word == 'adjective.':
                            words_in_story[curr_index] = self.find_word('Adjective', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'adjective!':
                            words_in_story[curr_index] = self.find_word('Adjective', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'adjective?':
                            words_in_story[curr_index] = self.find_word('Adjective', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'adjective,':
                            words_in_story[curr_index] = self.find_word('Adjective', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in adverbStrings:
                        if curr_word == 'adverb':
                            words_in_story[curr_index] = self.find_word('Adverb', copy_dict)
                            curr_index += 1
                        elif curr_word == 'adverb.':
                            words_in_story[curr_index] = self.find_word('Adverb', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'adverb!':
                            words_in_story[curr_index] = self.find_word('Adverb', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'adverb?':
                            words_in_story[curr_index] = self.find_word('Adverb', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'adverb,':
                            words_in_story[curr_index] = self.find_word('Adverb', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in pluralNounStrings:
                        if curr_word == 'pluralnoun':
                            words_in_story[curr_index] = self.find_word('Plural noun', copy_dict)
                            curr_index += 1
                        elif curr_word == 'pluralnoun.':
                            words_in_story[curr_index] = self.find_word('Plural noun', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'pluralnoun!':
                            words_in_story[curr_index] = self.find_word('Plural noun', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'pluralnoun?':
                            words_in_story[curr_index] = self.find_word('Plural noun', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'pluralnoun,':
                            words_in_story[curr_index] = self.find_word('Plural noun', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in pastTenseVerbStrings:
                        if curr_word == 'pasttenseverb':
                            words_in_story[curr_index] = self.find_word('Past tense verb', copy_dict)
                            curr_index += 1
                        elif curr_word == 'pasttenseverb.':
                            words_in_story[curr_index] = self.find_word('Past tense verb', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'pasttenseverb!':
                            words_in_story[curr_index] = self.find_word('Past tense verb', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'pasttenseverb?':
                            words_in_story[curr_index] = self.find_word('Past tense verb', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'pasttenseverb,':
                            words_in_story[curr_index] = self.find_word('Past tense verb', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in nameStrings:
                        if curr_word == 'name':
                            words_in_story[curr_index] = self.find_word('Name', copy_dict)
                            curr_index += 1
                        elif curr_word == 'name.':
                            words_in_story[curr_index] = self.find_word('Name', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'name!':
                            words_in_story[curr_index] = self.find_word('Name', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'name?':
                            words_in_story[curr_index] = self.find_word('Name', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'name,':
                            words_in_story[curr_index] = self.find_word('Name', copy_dict) + ','
                            curr_index += 1
                    elif curr_word in placeStrings:
                        if curr_word == 'place':
                            words_in_story[curr_index] = self.find_word('Place', copy_dict)
                            curr_index += 1
                        elif curr_word == 'place.':
                            words_in_story[curr_index] = self.find_word('Place', copy_dict) + '.'
                            curr_index += 1
                        elif curr_word == 'place!':
                            words_in_story[curr_index] = self.find_word('Place', copy_dict) + '!'
                            curr_index += 1
                        elif curr_word == 'place?':
                            words_in_story[curr_index] = self.find_word('Place', copy_dict) + '?'
                            curr_index += 1
                        elif curr_word == 'place,':
                            words_in_story[curr_index] = self.find_word('Place', copy_dict) + ','
                            curr_index += 1
                    else:
                        curr_index += 1

                # Recombine list into a string
                joined_story = ' '.join([str(item) for item in words_in_story])

                # Format the string so it isn't all on one line
                wrapper = textwrap.TextWrapper(width=50)
                final_story = wrapper.fill(text=joined_story)

                # Open and write the final story to the file, including the date created and newline formatting
                stories_file = open("my_stories.txt", "a")
                now = datetime.now()
                stories_file.write('Story created: ' + now.strftime("%b %d, %Y at %H:%M:%S") + ('\n' * 2))
                stories_file.write(final_story)
                stories_file.write('\n' * 2)
                stories_file.close()

                print('Story created: ' + now.strftime("%b %d, %Y at %H:%M:%S") + '\n')

                # Return the final story so that it will be printed in the console as well
                return final_story

        except InsufficientWordsError:
            return "InsufficientWordsError: Not enough words for this story, continue entering words\n"


class InvalidCharacterError(Exception):
    # Custom exception used for validating the gui entries
    pass


class InsufficientWordsError(Exception):
    # Custom exception used for preventing the user from being able to create a story without the required number of words
    pass


# ---------------------Main---------------------

# Create mad lib class to be used and altered by playing
madlib = MadLib()

# Initialize word type counts to be used globally
noun_count = 0
verb_count = 0
adj_count = 0
adverb_count = 0
plural_noun_count = 0
past_tense_verb_count = 0
name_count = 0
place_count = 0

# Open a new file if it doesn't exist or open the existing file if the user has already played the game
stories_file = open("my_stories.txt", "a")

# GUI Start
window = Tk()
window.title("Mad Libs Creator")
window['bg'] = '#b2ffce'

# ROW ZERO - Title
header_line1 = Label(window, text="MAD LIBS", bg='#b2ffce', width=35, borderwidth=5, font=30).grid(row=0, column=0, columnspan=7)

# ROW ONE - Decorative
deco_line1 = Label(window, text="****************************************************************", bg='#b2ffce', width=45, font=30).grid(row=1, column=0, columnspan=7)

# ROW TWO - Header 1 - Choose story
header_line2 = Label(window, text="CHOOSE STORY", bg='#b2ffce', width=35, borderwidth=5).grid(row=2, column=0, columnspan=7)

# ROW THREE - Story choices buttons
dog_button = Button(window, text="Dog", command=lambda: [madlib.set_story(dog_story), madlib.check_words_needed(), madlib.update_gui()]).grid(row=3, column=0)
fishing_button = Button(window, text="Fishing", command=lambda: [madlib.set_story(fish_story), madlib.check_words_needed(), madlib.update_gui()]).grid(row=3, column=2)
star_wars_button = Button(window, text="Star Wars", command=lambda: [madlib.set_story(star_wars_story), madlib.check_words_needed(), madlib.update_gui()]).grid(row=3, column=4)
love_letter_button = Button(window, text="Love Letter", command=lambda: [madlib.set_story(love_letter_story), madlib.check_words_needed(), madlib.update_gui()]).grid(row=3, column=6)

# ROW FOUR - Story selection notification empty space
responsive_line = Label(window, text="                                                   ", bg='#b2ffce', width=35, font=30).grid(row=4, column=0, columnspan=7)

# ROW FIVE - Header 2 - Word bank
header_line3 = Label(window, text="WORD BANK", bg='#b2ffce', width=35, borderwidth=5).grid(row=5, column=0, columnspan=7, padx=10, pady=10)

# ROW SIX - Word bank button options
pre_made_story = Button(window, text="Pre-Made", command=madlib.use_word_bank).grid(row=6, column=0, pady=15)
check_bank = Button(window, text="Check Bank", command=madlib.check_word_bank).grid(row=6, column=2, pady=15)
clear_bank = Button(window, text="Clear Bank", command=madlib.clear_dict).grid(row=6, column=4, pady=15)
check_needed = Button(window, text="Check Words Needed", command=lambda: madlib.check_words_needed()).grid(row=6, column=6, pady=15)

# ROW SEVEN - Add word buttons and entry - First half
add_noun_button = Button(window, text="     Add Noun      ", command=lambda: madlib.add_word('Noun', noun.get())).grid(row=7, column=0)
add_verb_button = Button(window, text="         Add Verb          ", command=lambda: madlib.add_word('Verb', verb.get())).grid(row=7, column=2)
add_adj_button = Button(window, text="Add Adjective", command=lambda: madlib.add_word('Adjective', adj.get())).grid(row=7, column=4)
add_adverb_button = Button(window, text="Add Adverb", command=lambda: madlib.add_word('Adverb', adverb.get())).grid(row=7, column=6)

noun = StringVar()
verb = StringVar()
adj = StringVar()
adverb = StringVar()

noun_entry = Entry(window, textvariable=noun).grid(row=7, column=1)
verb_entry = Entry(window, textvariable=verb).grid(row=7, column=3)
adj_entry = Entry(window, textvariable=adj).grid(row=7, column=5)
adverb_entry = Entry(window, textvariable=adverb).grid(row=7, column=7)

# ROW EIGHT - Add word buttons and entry - Second half
add_plural_noun_button = Button(window, text="Add Plural Noun", command=lambda: madlib.add_word('Plural noun', plural_noun.get())).grid(row=8, column=0)
add_past_verb_button = Button(window, text="Add Past tense Verb", command=lambda: madlib.add_word('Past tense verb', past_verb.get())).grid(row=8, column=2)
add_name_button = Button(window, text="   Add Name  ", command=lambda: madlib.add_word('Name', name.get())).grid(row=8, column=4)
add_place_button = Button(window, text="  Add Place  ", command=lambda: madlib.add_word('Place', place.get())).grid(row=8, column=6)

plural_noun = StringVar()
past_verb = StringVar()
name = StringVar()
place = StringVar()

plural_noun_entry = Entry(window, textvariable=plural_noun).grid(row=8, column=1)
past_verb_entry = Entry(window, textvariable=past_verb).grid(row=8, column=3)
name_entry = Entry(window, textvariable=name).grid(row=8, column=5)
place_entry = Entry(window, textvariable=place).grid(row=8, column=7)

# ROW NINE - Create story button
create_button = Button(window, text="Create Story", width=35, borderwidth=5, state=DISABLED, command=lambda: print(madlib.create_story())).grid(row=9, column=0, columnspan=7, padx=10, pady=10)

# ROW TEN - Exit button
exit_button = Button(window, text="Exit", command=window.destroy).grid(row=10, column=0, columnspan=7, padx=10, pady=10)

window.mainloop()
