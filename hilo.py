import random
# The player starts the game with 300 points.
# Individual cards are represented as a number from 1 to 13.
# The current card is displayed.
# The player guesses if the next one will be higher or lower.
# The the next card is displayed.
# The player earns 100 points if they guessed correctly.
# The player loses 75 points if they guessed incorrectly.
# If a player reaches 0 points the game is over.
# If a player has more than 0 points they decide if they want to keep playing.
# If a player decides not to play again the game is over

class game:

    def start(self):
        self.points = 300
        answer = input('Do you want to play high low? [y/n]' )
        if answer == "n":
            print("goodbye")
            print(f'Your final pints are {self.points}!')
            return
        while True:
            self.card = random.randint(1,13)
            print(f'The card number is {self.card}')
            if self.check_answer():
                answer = input(f'Your points are now {self.points}! Do you want to try again? [y,n]')
                if answer == "n":
                    print("goodbye")
                    print(f'Your final points are {self.points}!')
                    return
            else:
                print("You lose")
                return

    def check_answer(self):
        x = input('Do you think the next card will be higher or lower? [h/l]')
        while True:
            nextCard = random.randint(1,13)
            print(f'The next card number is {nextCard}')
            if nextCard >= self.card:
                if x == "h":
                    self.points = self.points + 100
                else:
                    self.points = self.points - 75
            else:
                if x == "h":
                    self.points = self.points - 75
                else:
                    self.points = self.points + 100
            
            if self.points < 1:
                return False
            return True
        


g = game()
g.start()

