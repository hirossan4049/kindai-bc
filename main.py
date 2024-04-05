from m5stack import *
from m5ui import M5Rect, M5TextBox
import m5stack_ui
from uiflow import *
import imu
import random

# MARK: ./mazes.py
# importのバグが頻繁に発生するのでファイル理由していない
maze1_length = 11
maze1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maze2_length = 11
maze2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maze3_length = 22
maze3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

DEBUG = False
WIDTH, HEIGHT = lcd.screensize()
MAZE_SIZE = WIDTH # 仮
BALL_SIZE = 6

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xffffff)
# screen.set_screen_brightness(30)
imu0 = imu.IMU()

if DEBUG:
  debug_text = M5TextBox(110, 0, str(WIDTH), lcd.FONT_Default, 0xff0000, rotate=0)

def setup_maze(maze, box_size):
  screen.clean_screen()
  screen.set_screen_bg_color(0x000000)

  for (row_i, row) in enumerate(maze):
    for (column_i, column) in enumerate(row):
      x = int(box_size * column_i)
      y = int(box_size * row_i)

      color = 0x000000
      if column == 0: # 通路
        color = 0x000000
      elif column == 1: # 壁
        color = 0xffffff
      elif column == 2: # スタート
        color = 0x000000
      elif column == 3: # ゴール
        color = 0x0000ff
      else:
        color = 0x0000ff
      M5Rect(x, y, box_size, box_size, color)

def game_loop(maze, maze_length, box_size):
  dot_label = M5Rect(0,0, BALL_SIZE, BALL_SIZE, 0xff0000,)

  # ビルドできてるかのデバッグ用
  if DEBUG:
    M5TextBox(0, 0, str(random.randint(0, 50)), lcd.FONT_Default, 0xff0000, rotate=0)

  x = int(box_size / 2 - BALL_SIZE / 2)
  y = int(box_size + box_size / 2 - BALL_SIZE / 2)

  while True:
    old_x = x
    old_y = y
    new_x = int(round(imu0.ypr[2], -1))
    new_y = int(round(imu0.ypr[1], -1))

    # 勢い余らせてブロック貫通してしまうのを防ぐ
    if abs(new_x) > box_size * 2:
      new_x = -box_size if new_x < 0 else box_size
    if abs(new_y) > box_size * 2:
      new_y = -box_size if new_y < 0 else box_size

    x += new_x #int(round(imu0.ypr[2], -1))
    y += new_y #int(round(imu0.ypr[1], -1))

    # 外枠壁判定
    if x > (WIDTH - BALL_SIZE):
      x = WIDTH - BALL_SIZE
    elif x < 0:
      x = 0
    if y > (HEIGHT - BALL_SIZE):
      y = HEIGHT - BALL_SIZE
    elif y < 0:
      y = 0

    # tupple
    points = [[x, y], [x + BALL_SIZE, y], [x, y + BALL_SIZE], [x + BALL_SIZE, y + BALL_SIZE]]
    goal = False

    for point in points:
      column_i = point[0] // box_size
      row_i = point[1] // box_size
      if (column_i > maze_length) or (row_i > maze_length):
        continue

      try:
        column = maze[row_i][column_i]
        if column == 1:
          x = old_x
          y = old_y
        elif column == 3:
          goal = True
      except:
          x = old_x
          y = old_y

    dot_label.setPosition(x, y)
    screen.clean_screen()
    # debug_text.setText(str(x) + " " + str(y)),
    wait_ms(40)

    if goal:
      power.setVibrationEnable(True)
      wait(0.2)
      power.setVibrationEnable(False)
      screen.clean_screen()
      break

stages = [(maze1, maze1_length),
          (maze2, maze2_length),
          (maze3, maze3_length)]

def ended_game():
  screen.clean_screen()
  screen.set_screen_bg_color(0xffffff)
  M5TextBox(95, 21, "CLEAR!", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

  clearBtn = m5stack_ui.M5Btn(text='CLOSE',
                             x=20, y=167, w=280, h=48, 
                             bg_c=0xffffff, text_c=0x000000,
                             font=m5stack_ui.FONT_MONT_14, parent=None)
  clearBtn.pressed(start_screen)

def start():
  screen.clean_screen()
  screen.set_screen_bg_color(0xffffff)
  power.setVibrationEnable(True)
  wait(0.2)
  power.setVibrationEnable(False)

  for (maze, maze_length) in stages:
    box_size = int(MAZE_SIZE / maze_length)

    setup_maze(maze, box_size)
    game_loop(maze, maze_length, box_size)
  ended_game()


def start_screen():
  M5TextBox(40, 40, "MAZE GAME", lcd.FONT_DejaVu40, 0x000000, rotate=0)

  startBtn = m5stack_ui.M5Btn(text='START',
                              x=20, y=167, w=280, h=48, 
                              bg_c=0xffffff, text_c=0x000000,
                              font=m5stack_ui.FONT_MONT_14, parent=None)
  startBtn.pressed(start)

start_screen()