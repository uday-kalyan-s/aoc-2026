data = open("input.txt").read().splitlines()

nodes = []

dists = [[0]*len(data) for _ in data]

def get_dist(a, b):
    return sum(
        [(a[i]-b[i])**2 for i in range(len(a))]
    )

dist_arr = []

for i, ln in enumerate(data):
    nd = list(map(int, ln.split(',')))
    for j, el in enumerate(nodes):
        dists[i][j] = dists[j][i] = get_dist(nd, el)
        dist_arr.append((dists[i][j], i, j))
    nodes.append(nd)

dist_arr = sorted(dist_arr)

clusters = []
clusters = [i for i in range(len(nodes))]

def union(n1, n2):
    clusters[get_cluster(n1)] = n2

def get_cluster(nd):
    if clusters[nd] != nd:
        return get_cluster(clusters[nd])
    return nd

def check_connected():
    for i in range(len(nodes)):
        if get_cluster(i) != get_cluster(0):
            return False
    return True

for i in range(len(dist_arr)):
    _, n1, n2 = dist_arr[i]
    if get_cluster(n1) == get_cluster(n2): # same cluster
        continue
    union(n1, n2)
    if check_connected():
        print(nodes[n1][0] * nodes[n2][0])
        break