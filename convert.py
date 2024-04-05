
def convert_maze2array(maze):
  # FIXME
  return [[int(i) for i in line.split("\t")] for line in maze.split("\n")]

maze1 = """\
1	1	1	1	1	1	1	1	1	1	1
2	0	0	0	0	0	0	0	0	0	1
1	0	1	0	1	1	1	0	1	1	1
1	0	1	0	0	0	0	0	0	0	1
1	0	1	1	1	0	1	1	1	0	1
1	0	0	0	1	0	1	0	0	0	1
1	0	1	0	0	0	0	0	1	0	3
1	1	1	1	1	1	1	1	1	1	1\
"""

maze2 = """\
1	1	1	1	1	1	1	1	1	1	1
2	0	1	0	0	0	1	0	0	0	1
1	0	0	0	1	0	1	0	1	1	1
1	1	0	1	0	0	0	0	0	0	1
1	0	0	1	0	1	0	1	0	1	1
1	0	0	0	1	1	1	1	0	0	1
1	0	1	0	0	0	0	0	1	0	3
1	1	1	1	1	1	1	1	1	1	1\
"""

maze3 = """\
1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1
2	0	1	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1
1	0	1	0	1	0	1	1	1	1	1	1	1	1	1	1	0	1	1	1	0	1
1	0	0	0	1	0	0	0	0	0	0	1	0	0	0	1	0	1	0	1	0	1
1	0	1	1	1	1	1	1	0	1	0	1	0	1	0	1	0	1	0	1	0	1
1	0	1	0	0	1	0	1	0	1	0	0	0	1	0	1	0	0	0	1	0	1
1	0	1	0	1	1	0	1	1	1	1	1	1	1	0	1	1	1	1	1	0	1
1	0	1	0	0	1	0	0	0	0	0	0	0	1	0	0	0	1	0	0	0	1
1	0	1	0	0	1	1	1	1	1	1	1	0	1	1	1	0	1	0	1	1	1
1	0	0	0	0	0	1	0	0	0	0	1	0	0	0	0	0	0	0	0	0	1
1	1	1	1	1	0	1	1	1	1	0	1	1	1	1	1	1	1	1	1	0	1
1	0	0	0	1	0	0	0	1	0	0	0	0	0	0	1	0	1	0	0	0	1
1	0	1	1	1	1	1	0	0	0	0	0	0	1	0	0	0	0	1	0	1	1
1	0	1	0	0	0	1	1	1	1	1	1	1	1	1	1	1	0	1	0	0	1
1	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	3
1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1\
"""

# maze_length
# お気持ち最適化

print(f"""
maze1_length = 11
maze1 = {convert_maze2array(maze1)}

maze2_length = 11
maze2 = {convert_maze2array(maze2)}

maze3_length = 22
maze3 = {convert_maze2array(maze3)}
""")
