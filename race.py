import turtle
import random
import time

class TurtleRacer:
    def __init__(self, color, y_position):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(-230, y_position)
        self.turtle.pendown()

    def move(self):
        self.turtle.forward(random.randint(1, 10))

    def reset_position(self):
        self.turtle.penup()
        self.turtle.goto(-230, self.turtle.ycor())
        self.turtle.pendown()

class TurtleRaceGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=400)
        self.screen.title("Turtle Race Game")

        self.colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        self.y_positions = [-150, -90, -30, 30, 90, 150]
        self.turtles = []

        for i in range(6):
            racer = TurtleRacer(self.colors[i], self.y_positions[i])
            self.turtles.append(racer)

        self.user_points = 100
        self.race_on = False
        self.round = 1

        self.setup_screen()
        self.screen.mainloop()

    def setup_screen(self):
        self.screen.clearscreen()
        self.screen.title("Turtle Race Game")
        self.user_bet = self.screen.textinput(f"Round {self.round}: Make your bet", f"You have {self.user_points} points. Which turtle will win the race? Enter a color: ")
        self.bet_amount = int(self.screen.numinput(f"Round {self.round}: Place your bet", "How many points would you like to bet?", minval=1, maxval=self.user_points))
        
        self.start_race()

    def start_race(self):
        self.race_on = False
        self.screen.clearscreen()
        self.screen.title("Turtle Race Game")

        countdown = 3
        for i in range(countdown, 0, -1):
            self.screen.clearscreen()
            self.screen.title(f"Race starts in {i}")
            time.sleep(1)

        self.screen.clearscreen()
        self.race_on = True

        while self.race_on:
            for racer in self.turtles:
                racer.move()
                if racer.turtle.xcor() > 230:
                    self.race_on = False
                    winning_color = racer.turtle.pencolor()
                    self.end_race(winning_color)
                    break

    def end_race(self, winning_color):
        self.screen.clearscreen()
        if winning_color == self.user_bet:
            self.user_points += self.bet_amount
            self.screen.title(f"Congratulations! The {winning_color} turtle won the race! You won {self.bet_amount} points!")
        else:
            self.user_points -= self.bet_amount
            self.screen.title(f"Sorry, the {winning_color} turtle won the race. You lost {self.bet_amount} points.")

        time.sleep(2)

        for racer in self.turtles:
            racer.reset_position()

        if self.user_points <= 0:
            self.screen.title("Game Over! You have no more points.")
        else:
            self.round += 1
            self.setup_screen()

if __name__ == "__main__":
    TurtleRaceGame()
