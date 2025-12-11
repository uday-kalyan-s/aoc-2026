data = open("input.txt").read()

dial = 50
count = 0

for ln in data.splitlines():
    d = ln[0]
    val = int(ln[1:])
    if d == 'R':
        dial += val
    else:
        dial -= val
    dial = dial%100
    if dial == 0:
        count += 1

print(count)