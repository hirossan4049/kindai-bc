
def convert_maze2array(maze):
  # FIXME
  return [[int(i) for i in line.split("\t")] for line in maze.split("\n")]

maze1 = """\
1	1	1	1	1	1	1	1	1	1	1
0	0	1	0	0	0	1	0	0	0	1
1	0	1	0	1	0	1	0	1	0	1
1	0	0	0	1	0	0	0	1	0	1
1	1	1	0	1	0	1	1	1	0	1
1	0	0	0	0	0	0	0	0	0	1
1	0	1	1	1	0	1	1	1	0	1
1	0	0	0	0	0	0	0	0	0	1
1	0	1	1	1	0	1	1	1	0	1
1	0	0	0	1	0	0	0	0	0	0
1	1	1	1	1	1	1	1	1	1	1\
"""

maze2 = """\
1	1	1	1	1	1	1	1	1	1	1
2	0	0	0	0	0	0	0	0	0	1
1	0	1	0	1	1	1	0	1	1	1
1	0	1	0	0	0	0	0	0	0	1
1	0	1	1	1	0	1	1	1	0	1
1	0	0	0	1	0	1	0	0	0	1
1	0	1	0	0	0	0	0	1	0	3
1	1	1	1	1	1	1	1	1	1	1\
"""


print(f"""
# 11x11
maze1_length = 11
maze1 = {convert_maze2array(maze1)}

# 10x11
maze2_length = 10
maze2 = {convert_maze2array(maze2)}
""")
