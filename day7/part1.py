data = open("input.txt").read().splitlines()

beams = set([data[0].find('S')])

split_cnt = 0

for ln in data[1:]:
    for b in beams.copy():
        if ln[b] == '^':
            beams.remove(b)
            if b-1 >= 0:
                beams.add(b-1)
            if b+1 < len(data[0]):
                beams.add(b+1)
            split_cnt += 1

print(split_cnt)