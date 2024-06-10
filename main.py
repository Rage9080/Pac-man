import turtle
import time 
import random

#create screen
screen = turtle.Screen()
screen.title("Pac - man")
screen.bgcolor("black")
screen.setup (width=600, height=500)
screen.tracer(0)
#create pac-an
head = turtle.Turtle()
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"
#create ghost
ghost_list =[]

colors = ["yellow", "red", "blue", "orange"]
start_pos = [(100,0), (-100,0), (0,100), (0,-100)]


for color, position in zip(colors, start_pos):
    ghost = turtle.Turtle()
    ghost.shape("square")
    ghost.color(color)
    ghost.penup()
    ghost.goto(position)
    ghost_list.append(ghost)


def go_up():
  if head.direction != "down":
    head.direction = "up"


def go_down():
  if head.direction != "up":
    head.direction = "down"


def go_left():
  if head.direction != "right":
    head.direction = "left"


def go_right():
  if head.direction != "left":
    head.direction = "right"


def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  elif head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)
  elif head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)
  elif head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

maze_layout=[
  "wwwwwwwwwwwwwww"

  "w             w"

  "wwwwwwwwwwwwwww"
]


block_size = 40


def draw_maze (maze):
  valid_food_position = []
  maze_width = len(maze[0])
  maze_heigth = len(maze)

  block_size_width = screen.window_width() / maze_width
  block_size_height = screen.window_height() / maze_heigth

  block_size = min(block_size_width, block_size_height)


  wall = turtle.Turtle()
  wall.shape("square")
  wall.color("yellow")
  wall.penup()
  wall.speed(0) 


  start_x = -((maze_width / 2) * block_size)
  start_y = ((maze_heigth / 2) * block_size)


  for y in range(maze_heigth):
      for x in range(maze_width):
        character = maze [y][x]
        screen_x = start_x + (x  * block_size)
        screen_x = start_y - (y  * block_size)


        if character == "W":
          wall.goto(screen_x, screen_y)
          wall.shapesize(stretch_wid=block_size / 20, stretch_len = block_size / 20)
          wall.stamp()
        else:
          valid_food_position.append((screen_x, screen_x))
      return valid_food_position 
      
draw_maze(maze_layout)
  
          



while True:
  screen.update()
  move()
  time.sleep(0.1) 
  