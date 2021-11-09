import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
# Control the player
screen.listen()
screen.onkeypress(player.up, "Up")

# Generate Cars
car_manager = CarManager()
# total_cars = random.randint(1,6)
loop_counter = 0

# Create scoreboard
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Generating Traffic
    if loop_counter % 6 == 0:
        car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.traffic:
        if car.distance(player) < 20:
            # Detect collision
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > player.finish_line_y:
        # If the turtle y coordinate position is equal to Finish line, then update score
        scoreboard.increase()
        scoreboard.update_score()
        player.restart()
        # Increase the speed of cars
        car_manager.increase_speed()
    loop_counter += 1

screen.exitonclick()
