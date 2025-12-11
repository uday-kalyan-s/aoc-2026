data = open("input.txt").read()

rating = 0

for ln in data.splitlines():
    maxes = [0] * len(ln)
    maxes[len(ln)-1] = ln[-1]
    for i in reversed(range(len(ln)-1)):
        maxes[i] = max(ln[i+1], maxes[i+1])
    largest_num = 0
    for i in range(len(ln)-1):
        largest_num = max(largest_num, int(ln[i]+maxes[i]))
    rating += largest_num

print(rating)