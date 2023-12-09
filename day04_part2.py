results = 0

# Card 1: 41 48 83 86 17                             | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 (83 86 17 48)               | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 (83 86 17 48) (61 32)       | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 (83 86 17 48) (61 32) (1)   | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 (83 86 17 48)               | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72                             | 74 77 10 23 35 67 36 11

GRID = open("day04_input.txt").read().splitlines()
number = [1 for x in range(len(GRID))]

results = 0
for i in range(len(GRID)):
  line = GRID[i]
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
  wins = 0
  for n in range(25):
      j = 42 + n * 3
      if int(line[j:j+2]) in wn:
          wins += 1

  for z in range(wins):
      # if len(number) - 1 >= i + 1 + z:
      number[i + 1 + z] += number[i]

  results += number[i]

print(results)
