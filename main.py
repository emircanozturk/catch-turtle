import turtle
from random import randint

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("#91C4F2")
text_font = "Bahnschrift", 25, "normal"
score = 0

score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    width = turtle.window_height()
    score_turtle.goto(x = 0 , y = width/2 - 40)
    score_turtle.write(f"Score: 0" , align = "center", font = text_font)

def make_turtle():
    t = turtle.Turtle()
    def create_turtle():
        t.hideturtle()
        t.penup()
        t.shape("turtle")
        t.shapesize(2)
        t.color("dark green")
        t.goto(x = randint(-350,350) , y = randint(-350,325))
        t.showturtle()

    def change_score(x , y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}",align = "center", font = text_font)

    def disappear():
        t.hideturtle()
        t.goto(x=randint(-350, 350), y=randint(-350, 325))
        t.showturtle()
        if time_left > 0:
            turtle.ontimer(disappear, t=500)
        else:
            t.hideturtle()
            t.home()
            t.write(f"GAME OVER AND YOUR SCORE IS {score}/21",align = "center", font = ("Bahnschrift", 35, "normal"))

    turtle.ontimer(disappear, t=500)
    create_turtle()
    t.onclick(change_score)


time_left = 20
timerturtle = turtle.Turtle()
def setup_timer_turtle():
    global time_left
    timerturtle.hideturtle()
    timerturtle.penup()
    width = turtle.window_height()
    timerturtle.goto(x=0, y=width / 2 - 75)
    timerturtle.write(f"Time: {time_left}", align="center", font=text_font)

    def decrease_time():
        global time_left
        time_left -= 1
        timerturtle.clear()
        timerturtle.write(f"Time: {time_left}", align="center", font=text_font)
        if time_left > -1:
            turtle.ontimer(decrease_time, t=1000)
        else:
            timerturtle.clear()
            timerturtle.write("GAME OVER", align="center", font=text_font)
    turtle.ontimer(decrease_time, t = 1000)

turtle.tracer(0)
setup_timer_turtle()
setup_score_turtle()
make_turtle()
turtle.tracer(1)
turtle.mainloop()
