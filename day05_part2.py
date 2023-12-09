import datetime

GRID = open("day05_input.txt").read().splitlines()

# get seed_ranges
seeds_raw = [int(x) for x in GRID[0][7:].split(" ")]
seed_ranges = [] # [[1, 10], [100, 101]] # 1 to 10 and 100 to 101
for i in range(int(len(seeds_raw) / 2)):
    seed_ranges.append([seeds_raw[i * 2], seeds_raw[i * 2] + seeds_raw[i * 2 + 1] - 1])

# get all mappings
all_mappings = [] # [mappings]
mappings = [] # [[1, 10, 5]] # map 1 to 5 and 10 to 14
for line in GRID[2:]:
    if line == "":
        mappings.sort()
        all_mappings.append(mappings)
        mappings = []
    elif line[-1] != ":":
        mapping_raw = [int(x) for x in line.split(" ")]
        mappings.append([mapping_raw[1], mapping_raw[1] + mapping_raw[2] - 1, mapping_raw[0]])
if len(mappings) > 0:
    mappings.sort()
    all_mappings.append(mappings)
    mappings = []


# apply mappings
for mappings in all_mappings:
    new_seed_ranges = []
    for i in range(len(seed_ranges)):
        s_from, s_to = seed_ranges[i]
        converting = True

        for m_from, m_to, m_t in mappings:
            if s_from > m_to:
                continue

            if s_to < m_from:
                new_seed_ranges.append([s_from, s_to])
                converting = False
                break

            if s_from < m_from:
                new_seed_ranges.append([s_from, m_from - 1])
                s_from = m_from

            if s_to <= m_to:
                new_seed_ranges.append([
                    s_from + m_t - m_from,
                    s_to + m_t - m_from,
                ])
                converting = False
                break
            else:
                new_seed_ranges.append([
                    s_from + m_t - m_from,
                    m_to + m_t - m_from,
                ])
                s_from = m_to + 1

        if converting:
            new_seed_ranges.append([s_from, s_to])

    seed_ranges = new_seed_ranges

# print min
seed_ranges.sort()
print(seed_ranges[0][0])
