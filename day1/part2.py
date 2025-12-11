data = open("input.txt").read()

dial = 50
count = 0

for ln in data.splitlines():
    d = ln[0]
    val = int(ln[1:])
    atzero = False
    if dial == 0:
        atzero = True
    if d == 'R':
        dial += val
        count += dial//100
    else:
        dial -= val
        if atzero:
            count += abs(val//100)
        else:
            count += abs(dial//100)
            if dial%100 == 0:
                count += 1
    dial = dial%100
    print(count, dial)

print(count)