import random

class UserInteraction:

    def __init__(self, score_object):
        self.score_object = score_object
        self.how_mean = 0

    def ask(self, first=False):
        if first:
            prompt = "first"
        else:
            prompt = "next"
        asking = "Please make your {} guess:  ".format(prompt)
        return asking

    def wrong_guess(self):
        self.how_mean += 1
        if self.how_mean in [1, 2]:
            responses = [
                "Your guess was incorrect",
                "That is not a correct letter",
                "Nice try, but that is not right",
                "That is a good guess, but unfortunately not a correct one",
                "That's not right, you'll do better next try though I'm sure of it",
                        ]
        elif self.how_mean in [3, 4]:
            responses = [
                "That is not correct, you can do better than that!",
                "Yet another incorrect guess",
                "Wow, I really thought you were smarter than that",
                "Dude. Just dude. Come on already!",
                "Holy bonkers! What were you thinking!?",
                "Doh!",
                        ]
        elif self.how_mean == 5:
            responses = [
                "You are really terrible at this, only one wrong guess left sucker!",
                "Hahaha! I am so going to beat you!",
                "You are going down!",
                "One more wrong answer till you're hung"
                "Wow you suck, you do realize you're playing against a computer right?",
                "I could do better in my sleep!",
                "Even a monkey could do better than that!",
                "You're pathetic!"
                        ]
        elif self.how_mean == 6:
            self.game_over()
            return
        else:
            raise AssertionError("Error: how_mean level out of range")
        return random.choice(responses)

    def right_guess(self):
        if self.how_mean > 0:
            self.how_mean -= 1
        if self.how_mean in [0, 1, 2]:
            responses = [
                "That is correct",
                "Good one!",
                "You're right, keep it up",
                        ]
        elif self.how_mean in [3, 4]:
            responses = [
                "Thank goodness that's a correct answer",
                "Okay, you are smarter than I first thought",
                "Nice work",
                "Keep it up and you might actually win",
                        ]
        else:
            raise AssertionError("Error: how_mean level out of range")
        return random.choice(responses)

    def game_over(self, win=True):
        score = self.score_object.score
        if not win:
            responses = [
                "You lose!",
                "That's it, I win!",
                "Better luck next time loser!",
                        ]
        elif win and score > 0:
            responses = [
                "Congratulations! You won!"
                        ]
        elif win and score == 0:
            responses = [
                "Wow! Great work! Perfect game!",
                "Shut out game, awesome work!",
                        ]
        else:
            raise Exception("Something went wrong")
        return random.choice(responses)
