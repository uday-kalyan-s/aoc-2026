data = open("input.txt").read().splitlines()

ans = 0

islast = False

while not islast:
    i = 1
    while i < len(data[0]) and data[-1][i] == ' ':
        i += 1
    if i == len(data[0]):
        islast = True
    else:
        i -= 1
    cons = []
    for ind, ln in enumerate(data[:-1]):
        cons.append(int(ln[:i]))
        if not islast:
            data[ind] = ln[i+1:]
    op = data[-1][:i].strip()
    if not islast:
        data[-1] = data[-1][i+1:]
    if op == '+':
        ans += sum(cons)
    else:
        a = 1
        for el in cons:
            a *= el
        ans += a

print(ans)