data = open("input.txt").read().splitlines()

nodes = []

dists = [[0]*len(data) for _ in data]

def get_area(a, b):
    p = 1
    for i in range(len(a)):
        p *= abs(a[i]-b[i])+1
    return p

dist_arr = []

for i, ln in enumerate(data):
    nd = list(map(int, ln.split(',')))
    for j, el in enumerate(nodes):
        dists[i][j] = dists[j][i] = get_area(nd, el)
        dist_arr.append((dists[i][j], i, j))
    nodes.append(nd)

dist_arr = sorted(dist_arr)

print(dist_arr[-1][0])