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
        cons.append(ln[:i])
        if not islast:
            data[ind] = ln[i+1:]
    op = data[-1][:i].strip()
    if not islast:
        data[-1] = data[-1][i+1:]
    prob_nums = []
    for i in reversed(range(0, len(cons[0]))):
        num = 0
        for ln in cons:
            if ln[i] != ' ':
                num = num*10 + int(ln[i])
        prob_nums.append(num)
    if op == '+':
        ans += sum(prob_nums)
    else:
        a = 1
        for el in prob_nums:
            a *= el
        ans += a

print(ans)