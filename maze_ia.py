#!/usr/bin/env python3
# ./vm-Linux ./maze_ia.py -d
import sys
import collections

def get():
    i = 0
    y = sys.stdin.readline()
    maze = ''
    while '#' in y:
        maze = maze + list(y)
        y = sys.stdin.readline()
    return maze.split('\n')[0:-1]


def get_ia(map):
  vitri_ia = []
  for current_y in range(len(map)):
      for current_x in range(len(map[current_y])):
          if map[current_y][current_x] == "A":
              vitri_ia.append((current_y, current_x))
  return vitri_ia


def bfs(map, IA):
  start = IA[0]
  double = collections.deque([[start]])
  note_street = list(start)
  while double:
    path = double.popleft()
    (y, x) = path[-1]
    if map[y][x] == "!":
      return path
    if map[y][x] == "o":
      return path
    for x1, y1 in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
      if map[y1][x1] != "#" and [y1, x1] not in note_street:
        double.append(path + [[y1, x1]])
        note_street.append([y1, x1])
  return path


# di chuyen
def move(path): # (0,1) (1,0), (-1,1), (-1,0)
    if path[1][0] - path[0][0] == 1:
        return "MOVE DOWN\n\n"
    elif path[1][0] - path[0][0] == -1:
        return "MOVE UP\n\n"
    elif path[1][1] - path[0][1] == -1:
        return "MOVE LEFT\n\n"
    elif path[1][1] - path[0][1] == 1:
        return "MOVE RIGHT\n\n"
    else:
        return None


if __name__ == '__main__': # creat character
    while True:
        x = sys.stdin.readline()
        # maze = []
        if "HELLO" in x:
            sys.stdout.write("I AM ANH\n\n")
        if "YOU" in x:
            sys.stdout.write("OK\n\n")
        if "MAZE" in x:
            maze = []
            while len(x) > 0:
                x = sys.stdin.readline().rstrip("\n")
                maze.append(x)
            vitri_ia = get_ia(maze)
            path = bfs(maze, vitri_ia)
            x = move(path)
            sys.stdout.write(x)
