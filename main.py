import turtle
import datetime
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("beige")

# Draw the clock face
clock_face = turtle.Turtle()
clock_face.hideturtle()
clock_face.speed(0)
clock_face.pensize(3)
clock_face.penup()
clock_face.goto(0, -200)
clock_face.pendown()
clock_face.circle(200)

# Draw clock ticks
for hour in range(12):
    clock_face.penup()
    clock_face.goto(0, 0)
    clock_face.setheading(90 - (hour * 30))
    clock_face.forward(170)
    clock_face.pendown()
    clock_face.forward(20)
    clock_face.penup()
    clock_face.forward(20)
    clock_face.write(str(hour + 1), align="center", font=("Arial", 12, "bold"))

# Register custom clock hand shapes
turtle.register_shape("hour_hand", ((-4, -5), (4, -5), (2, 150), (-2, 150)))
turtle.register_shape("minute_hand", ((-2, -5), (2, -5), (1, 200), (-1, 200)))
turtle.register_shape("second_hand", ((-1, -5), (1, -5), (0.5, 220), (-0.5, 220)))

# Create clock hands
hands = []
for shape, color in [("hour_hand", "black"), ("minute_hand", "blue"), ("second_hand", "red")]:
    hand = turtle.Turtle()
    hand.shape(shape)
    hand.color(color)
    hand.speed(0)
    hands.append(hand)

# Digital time and date display
digital_time_display = turtle.Turtle()
digital_time_display.hideturtle()
digital_time_display.penup()
digital_time_display.goto(0, 250)

date_display = turtle.Turtle()
date_display.hideturtle()
date_display.penup()
date_display.goto(0, -250)

# Function to update the clock hands
def update_clock_hands():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second + now.microsecond / 1000000

    angles = [
        (hour + minute / 60) * 360 / 12,
        (minute + second / 60) * 360 / 60,
        second * 360 / 60
    ]

    for hand, angle in zip(hands, angles):
        hand.setheading(90 - angle)

# Function to update digital time and date
def update_digital_display():
    now = datetime.datetime.now()
    digital_time_display.clear()
    digital_time_display.write(now.strftime("%H:%M:%S"), align="center", font=("Arial", 24, "normal"))

    date_display.clear()
    date_display.write(now.strftime("%A, %B %d, %Y"), align="center", font=("Arial", 18, "normal"))

# Main update function
def update_clock():
    update_clock_hands()
    update_digital_display()
    screen.update()
    screen.ontimer(update_clock, 50)  # Smooth update every 50ms

# Start the clock
update_clock()

# Close the turtle graphics window on click
screen.exitonclick()
turtle.bye()
