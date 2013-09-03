import HangSpider

game = HangSpider

def make_guess(guess):
    """If guess is correct return True, else False"""
    if guess in game.puzzle.sentence:
        game.score.guess_was_right(guess)
        return True
    else:
        game.score.guess_was_wrong(guess)
        return False


first_ask = True
while game.score.score < 6:
    print game.art.ascii_combined()
    guess = raw_input(game.userinteraction.ask(first=first_ask))

    if guess.lower() in game.score.all_guesses:
        print "You already guessed that letter"
        continue
    elif (len(guess) != 1) or \
         (guess.lower() not in 'abcdefghijklmnopqrstuvwxyz'):
        print "That is not a letter, please guess a letter in the English alphabet"
        continue
    else:
        first_ask = False
        if make_guess(guess):
            if not game.score.is_puzzle_complete():
                print game.userinteraction.right_guess()
            else:
                print game.userinteraction.game_over(win=True)
                print game.art.ascii_combined()
                break
        else:
            if game.score.score < 6:
                print game.userinteraction.wrong_guess()
            elif game.score.score == 6:
                print game.userinteraction.game_over(win=False)
                print game.art.ascii_combined(game_over=True)
                break
