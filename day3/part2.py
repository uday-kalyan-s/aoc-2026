import functools

data = open("input.txt").read()

rating = 0

def combine(dig, num):
    return int(dig+str(num))

for ln in data.splitlines():
    @functools.cache
    def get_dp(i, j):
        if j == 0 or i == len(ln):
            return 0
        return max(combine(ln[i], get_dp(i+1,j-1)), get_dp(i+1, j))
    rating += get_dp(0, 12)//10

print(rating)