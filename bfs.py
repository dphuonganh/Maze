import collections

map = ['####################',
'#                  #',
'#                  #',
'#                  #',
'#    !              #',
'#         o o   o  #',
'#                  #',
'#    A             #',
'#                  #',
'####################']

def get_ia(map, IA):
  phuonganh = []
  for current_y in range(len(map)):
      for current_x in range(len(map[current_y])):
          if map[current_y][current_x] == IA:
              phuonganh.append((current_x, current_y))
  return phuonganh


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



if __name__ == "__main__":
    # dongtien = get_ia(map, "o")
    # print(dongtien)
    # chamthan = get_ia(map, "!")
    # print(chamthan)
    # print(get_ia(map, "A"))
  ia = [(7,5)]
  print(bfs(map, ia))
