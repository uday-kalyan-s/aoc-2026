from collections import defaultdict

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

# print(dist_arr)

clusters = []
clusters = [i for i in range(len(nodes))]

def union(n1, n2):
    clusters[get_cluster(n1)] = n2

def get_cluster(nd):
    if clusters[nd] != nd:
        return get_cluster(clusters[nd])
    return nd

CONN_NUM = 1000

for i in range(CONN_NUM):
    _, n1, n2 = dist_arr[i]
    if get_cluster(n1) == get_cluster(n2): # same cluster
        continue
    union(n1, n2)

cluster_dict = defaultdict(int)

for i in range(len(nodes)):
    cluster_dict[get_cluster(i)] += 1

lst = sorted(cluster_dict.items(), key=lambda x: x[1], reverse=True)
top3 = map(lambda x: x[1], lst[:3])

p = 1
for i in top3:
    p *= i

print(p)