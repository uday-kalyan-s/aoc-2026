data = open("input.txt").read()

def check_symm(s):
    for i in range(1, len(s)//2+1):
        if len(s)%i == 0:
            first = s[0:i]
            isvalid = True
            for j in range(1, len(s)//i):
                part = s[j*i:(j+1)*i]
                if part != first:
                    isvalid = False
                    break
            if isvalid:
                return True
    return False

id_sum = 0

for rng in data.split(','):
    l, r = rng.split('-')
    l = int(l)
    r = int(r)
    for i in range(l, r+1):
        if check_symm(str(i)):
            id_sum += i

print(id_sum)