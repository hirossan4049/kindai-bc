from m5stack import *
from m5ui import M5Rect, M5TextBox
from uiflow import *
import imu
import math
import random
# from mazes import maze2, maze2_length

# # 11x11
# maze1_length = 11
# maze1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# # 8x11
# maze2_length = 10
# maze2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# 10x11
maze2_length = 10
maze2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


DEBUG = True
WIDTH, HEIGHT = lcd.screensize()
MAZE_SIZE = 240 # 仮
BALL_SIZE = 10

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)
screen.set_screen_brightness(30)
imu0 = imu.IMU()

debug_text = M5TextBox(110, 0, str(WIDTH), lcd.FONT_Default, 0xff0000, rotate=0)

box_size = 30 # int(MAZE_SIZE / mazes.maze1_length)


maze_length = maze2_length
maze = maze2
def setup_maze(maze):
  for (row_i, row) in enumerate(maze):
    for (column_i, column) in enumerate(row):
      x = int(box_size * column_i)
      y = int(box_size * row_i)

      color = 0x000000
      if column == 0:
        color = 0x000000
      elif column == 1:
        color = 0xffffff
      else:
        color = 0x0000ff
      M5Rect(x, y, box_size, box_size, color)

setup_maze(maze)
dot_label = M5Rect(0,0, BALL_SIZE, BALL_SIZE, 0xff0000,)

# ビルドできてるかのデバッグ用
M5TextBox(0, 0, str(random.randint(0, 50)), lcd.FONT_Default, 0xff0000, rotate=0)

x = int(box_size / 2 - BALL_SIZE / 2)
y = int(box_size + box_size / 2 - BALL_SIZE / 2)

while True:
  old_x = x
  old_y = y
  x += int(round(imu0.ypr[2], 1))
  y += int(round(imu0.ypr[1], 1))

  # 外枠壁判定
  if x > (WIDTH - BALL_SIZE):
    x = WIDTH - BALL_SIZE
  elif x < 0:
    x = 0
  if y > (HEIGHT - BALL_SIZE):
    y = HEIGHT - BALL_SIZE
  elif y < 0:
    y = 0

  # 左上、右上、左下、右下の4点の座標
  points = [[x, y], [x + BALL_SIZE, y], [x, y + BALL_SIZE], [x + BALL_SIZE, y + BALL_SIZE]]

  for point in points:
    column_i = point[0] // box_size
    row_i = point[1] // box_size
    if (column_i > maze_length) or (row_i > maze_length):
      continue

    try:
      if maze[math.floor(row_i)][math.floor(column_i)] == 1:
        if (column_i + 1) * box_size < point[0]:
          x = old_x
        if (row_i + 1) * box_size < point[1]:
          y = old_y
        # x = old_x#int(box_size * column_i)
        # y = old_y#int(box_size * row_i)
    except:
        x = old_x# int(box_size * column_i)
        y = old_y# int(box_size * row_i)


  dot_label.setPosition(x, y)
  # screen.clean_screen()
  debug_text.setText(str(x) + " " + str(y))
  wait_ms(30)