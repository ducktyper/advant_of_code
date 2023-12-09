TXT = open("day07_input.txt").read().splitlines()

CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
CARDS.reverse()

hands = []
for line in TXT:
    hand, bid = line.split()

    sort_2 = 0
    for i in range(len(hand)):
        sort_2 += (CARDS.index(hand[i]) + 1) * 10 ** (4 - i * 2)

    group = {}
    j_count = 0
    for card in hand:
        if card == "J":
            j_count += 1
            continue
        if card not in group:
            group[card] = 0
        group[card] += 1
    counts = list(group.values())
    counts.sort()
    if len(counts) == 0:
        counts = [j_count]
    else:
        counts[-1] += j_count

    sort_1 = 0
    if counts == [5]:
        sort_1 = 7
    elif counts == [1, 4]:
        sort_1 = 6
    elif counts == [2, 3]:
        sort_1 = 5
    elif counts == [1, 1, 3]:
        sort_1 = 4
    elif counts == [1, 2, 2]:
        sort_1 = 3
    elif counts == [1, 1, 1, 2]:
        sort_1 = 2
    elif counts == [1, 1, 1, 1, 1]:
        sort_1 = 1

    hands.append([sort_1, sort_2, int(bid)])

hands.sort()

results = 0
for i in range(len(hands)):
    results += (i + 1) * hands[i][2]

print(results)
