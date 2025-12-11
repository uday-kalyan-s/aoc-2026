data = open("input.txt").read()

parsed = [list(ln) for ln in data.splitlines()]

liftable = 0

for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if parsed[i][j] != '@':
            continue
        neibs = 0
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if di == 0 and dj == 0:
                    continue
                if not (0 <= di + i < len(parsed)):
                    continue
                if not (0 <= dj+ j < len(parsed[0])):
                    continue
                if parsed[i+di][j+dj] == '@':
                    neibs += 1
        if neibs < 4:
            liftable += 1

print(liftable)