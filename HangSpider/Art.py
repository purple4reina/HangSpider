class Art:

    def __init__(self, score_object, puzzle_object):
        self.score_object = score_object
        self.puzzle_object = puzzle_object

    def hangman_art(self):
        level = len(self.score_object.incorrect_guesses)
        if level == 0:
            art = [
            "    +---+      ",
            "    |   |      ",
            "    |          ",
            "    |          ",
            "    |          ",
            "    |          ",
            "    |          ",
            "  -----        ",
              ]
        elif level == 1:
            art = [
            "    +---+      ",
            "    |   |      ", 
            "    |   O      ", 
            "    |          ", 
            "    |          ", 
            "    |          ", 
            "    |          ", 
            "  -----        ", 
              ]
        elif level == 2:
            art = [
            "    +---+      ",
            "    |   |      ", 
            "    |   O      ", 
            "    |   |      ", 
            "    |   |      ", 
            "    |          ", 
            "    |          ", 
            "  -----        ", 
              ]
        elif level == 3:
            art = [
            "    +---+      ",
            "    |   |      ", 
            "    |   O      ", 
            "    |   |      ", 
            "    |   |      ", 
            "    |  /       ", 
            "    |          ", 
            "  -----        ", 
              ]
        elif level == 4:
            art = [
            "    +---+      ",
            "    |   |      ", 
            "    |   O      ", 
            "    |   |      ", 
            "    |   |      ", 
            "    |  / \     ", 
            "    |          ", 
            "  -----        ", 
              ]
        elif level == 5:
            art = [
            "    +---+      ",
            "    |   |      ", 
            "    |   O      ", 
            "    |  _|      ", 
            "    |   |      ", 
            "    |  / \     ", 
            "    |          ", 
            "  -----        ", 
              ]
        elif level == 6:
            art = [
            "    +---+      ",
            "    |   |      ", 
            "    |   O      ", 
            "    |  _|_     ", 
            "    |   |      ", 
            "    |  / \     ", 
            "    |          ", 
            "  -----        ", 
              ]
        else:
            raise AssertionError("Error: Level index out of range")
        return art

    def sentence_art(self, game_over=False):
        sentence = self.puzzle_object.sentence
        all_guesses = self.score_object.all_guesses

        # replace letters
        if not game_over:
            if not ''.join(all_guesses).islower() and len(all_guesses) > 0:
                raise AssertionError("Error: all_guesses list not lowercase")
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            for letter in alphabet:
                if letter not in all_guesses:
                    sentence = sentence.replace(letter, "-")
                    sentence = sentence.replace(letter.swapcase(), "-")

        # split to lines
        word_list = sentence.split(" ")
        beau_lines = []
        line = ""
        for word_index in xrange(len(word_list)):
            word_len = len(word_list[word_index])
            if (word_len + len(line) <= 10) and (word_index != 0):
                line += " " + word_list[word_index]
            elif (word_len + len(line) <= 10) and (word_index == 0):
                line += word_list[word_index]
            else:
                beau_lines.append(line)
                line = word_list[word_index]
        beau_lines.append(line)

        return beau_lines

    def guesses_art(self):
        incorrect_guesses = self.score_object.incorrect_guesses

        box = [
               [" ", "+", "-", "-", "-", "-", "-", "-", "+"],
               [" ", "|", " ", " ", " ", " ", " ", " ", "|"],
               [" ", "+", "-", "-", "-", "-", "-", "-", "+"],
              ]

        for guess_index in xrange(len(incorrect_guesses)):
            box[1][guess_index+2] = incorrect_guesses[guess_index].upper()

        return [''.join(b) for b in box]

    def ascii_combined(self, game_over=False):
        hangman = self.hangman_art()
        sentence = self.sentence_art(game_over=game_over)
        box = self.guesses_art()

        # make sent len eq hang len
        if len(sentence) >= 4:
            err = "Sentence is just too long"
            raise Exception(err)
        else:
            while len(sentence) < 4:
                sentence = [""] + sentence

        # add box and sent
        right_side = [''] + box + sentence

        # zip them together
        full_art = []
        for index in xrange(8):
            line = hangman[index] + right_side[index]
            full_art.append(line)

        return '\n'.join(full_art)
