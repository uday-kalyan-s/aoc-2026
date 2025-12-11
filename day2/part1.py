data = open("input.txt").read()

def check_symm(s):
    return s[0:(len(s)//2)] == s[(len(s)//2):]

id_sum = 0

for rng in data.split(','):
    l, r = rng.split('-')
    l = int(l)
    r = int(r)
    for i in range(l, r+1):
        if len(str(i))%2 != 0:
            continue
        if check_symm(str(i)):
            id_sum += i

print(id_sum)