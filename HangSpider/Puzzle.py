import os
import random


class Puzzle:
    
    def __init__(self):
        self.sentence = self.make_puzzle()

    def random_line(self, file_name):
        pass

    def are_real_words(self, sentence):
        """
        Given a sentence string, return True if all words are in parts of speech files
        """

        sentence_list = sentence.split(" ")
        words_file_dir = os.path.join("/Users/purple4reina/Documents/",
                                      "Programming/textgenerator/",
                                      "parts of speech word files")

        # nouns
        with open(os.path.join(words_file_dir, "nouns/91Knouns.txt")) as nouns:
            nouns_list = nouns.readlines()
            sentence_list_copy = sentence_list.copy()
            print nouns_list
            for word in sentence_list:
                if (word + '\r\n') in nouns_list:
                    sentence_list.remove(word)

    def random_noun(self, length=7):
        with open(os.path.join("/Users/purple4reina/Documents/",
                               "Programming/textgenerator/",
                               "parts of speech word files",
                               "nouns/91Knouns.txt")) as nouns:
            nouns_list = nouns.readlines()
            noun = ''
            while (len(noun) < (length+2)) or (not noun.islower()):
                noun = random.choice(nouns_list)
            return noun[:-2]

    def random_adjective(self, length=5):
        with open(os.path.join("/Users/purple4reina/Documents/",
                               "Programming/textgenerator/",
                               "parts of speech word files",
                               "adjectives/28K adjectives.txt")) as adjectives:
            adjectives_list = adjectives.readlines()
            adjective = ''
            while (len(adjective) < (length+2)) or (not adjective.islower()):
                adjective = random.choice(adjectives_list)
            return adjective[:-2]

    def random_verb(self, length=8, ending=''):
        with open(os.path.join("/Users/purple4reina/Documents/",
                               "Programming/textgenerator/",
                               "parts of speech word files",
                               "verbs/31K verbs.txt")) as verbs:
            verbs_list = verbs.readlines()
            verb = ''
            while (len(verb) < (length+2)) \
                  or (not verb.islower()) \
                  or (not verb[:-2].endswith(ending)):
                verb = random.choice(verbs_list)
            return verb[:-2]

    def make_puzzle(self,
                    pattern_string="{a} {n}",
                    adj_len=7,
                    noun_len =7,
                    verb_len=8,
                    verb_ending=''):
        noun = self.random_noun(length=noun_len)
        adj = self.random_adjective(length=adj_len)
        verb = self.random_verb(length=verb_len, ending=verb_ending)
        try:
            puzzle = pattern_string.format(n=noun, a=adj, v=verb)
        except KeyError:
            err = "Available keys for pattern_string are 'n', 'a', and 'v'"
            raise KeyError(err)
        except IndexError:
            err = "pattern_string must have key 'n', 'a', or 'v'"
            raise IndexError(err)
        return puzzle
