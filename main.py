from m5stack import *
from m5ui import M5Rect, M5TextBox
# from m5stack_ui import * # M5Labelとかはこっち
from uiflow import *
import time
import imu
import math
import random

DEBUG = True
WIDTH, HEIGHT = lcd.screensize()

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

imu0 = imu.IMU()

# ビルドできてるかのデバッグ用
# M5Label(str(random.randint(0,50)), x=0, y=0, color=0xff0000, font=lcd.FONT_Default, parent=None)
M5TextBox(0, 0, str(random.randint(0,50)), lcd.FONT_Default, 0xff0000, rotate=0)
debug_text = M5TextBox(110, 0, str(WIDTH), lcd.FONT_Default, 0xff0000, rotate=0)


# rect0 = M5Rect(75, 75, 30, 80, 0x33cc00, 0x33cc00)

dot_label = M5Rect(30, 30, 30, 30, 0x33cc00, 0x33cc00) # M5Label(".", x=100, y=100, color=0xff0000, font=FONT_UNICODE_24, parent=None)

x = 0
y = 0
while True:

  x += int(round(imu0.ypr[2], -1))
  y += int(round(imu0.ypr[1], -1))

  if x > (WIDTH - 30):
    x = WIDTH - 30
  elif x < 0:
    x = 0
  if y > (HEIGHT - 30):
    y = HEIGHT - 30
  elif y < 0:
    y = 0

  # x = int(round(imu0.ypr[2] * 3 + WIDTH / 2 - 15, -1))
  # y = int(round(imu0.ypr[1] * 3 + HEIGHT / 2 - 15, -1))
  # dot_label.set_align(ALIGN_CENTER, x, y)
  dot_label.setPosition(x, y)
  screen.clean_screen()
  debug_text.setText(str(x) + " " + str(y))
  wait_ms(20) # 20fps
