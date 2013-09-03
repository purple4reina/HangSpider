from Puzzle import Puzzle

class Score:

    def __init__(self, puzzle_object):
        self.score = 0
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.all_guesses = []
        self.puzzle_object = puzzle_object

    def guess_was_wrong(self, guess):
        self.score += 1
        if guess not in self.incorrect_guesses:
            self.incorrect_guesses.append(guess.lower())
        else:
            raise AssertionError("Guess has already been made")
        self._update_all_guesses()

    def guess_was_right(self, guess):
        if guess not in self.correct_guesses:
            self.correct_guesses.append(guess.lower())
        else:
            raise AssertionError("Guess has already been made")
        self._update_all_guesses()

    def is_puzzle_complete(self):
        sentence = self.puzzle_object.sentence
        for letter in sentence:
            if letter == ' ':
                continue
            elif letter not in self.all_guesses:
                return False
        else:
            return True

    def _update_all_guesses(self):
        self.all_guesses = self.correct_guesses + self.incorrect_guesses
