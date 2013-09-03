from Puzzle import Puzzle
from Score import Score
from UserInteraction import UserInteraction
from Art import Art

puzzle = Puzzle()
score = Score(puzzle)
art = Art(score, puzzle)
userinteraction = UserInteraction(score)
