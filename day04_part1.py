results = 0

for line in open("day04_input.txt").read().splitlines():
  wn = {
      int(line[10:12]),
      int(line[13:15]),
      int(line[16:18]),
      int(line[19:21]),
      int(line[22:24]),
      int(line[25:27]),
      int(line[28:30]),
      int(line[31:33]),
      int(line[34:36]),
      int(line[37:39]),
  }
  score = 0
  for n in range(25):
      i = 42 + n * 3
      if int(line[i:i+2]) in wn:
          if score == 0:
              score = 1
          else:
              score *= 2

  results += score

print(results)
