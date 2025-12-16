from collections import defaultdict

edges = defaultdict(set)
for line in open("input.txt").read().splitlines():
    s, n_edges = line.split(': ')
    for e in n_edges.split(' '):
        edges[s].add(e)

def toposort():
    ordering = []
    visited = set()
    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        if not n in edges:
            ordering.append(n)
            return
        for e in edges[n]:
            dfs(e)
        ordering.append(n)
    for n in edges.keys():
        dfs(n)
    return ordering

ordering = toposort()
# print(ordering)

def find_paths(start, end):
    paths = defaultdict(int)
    for node in ordering:
        if node == end:
            paths[node] = 1
            continue
        pc = 0
        if node in edges:
            for e in edges[node]:
                pc += paths[e]
        paths[node] = pc
    # print(paths[start], start, end)
    return paths[start]

print(
    find_paths('svr', 'dac') * find_paths('dac', 'fft') * find_paths('fft', 'out') + 
    find_paths('svr', 'fft') * find_paths('fft', 'dac') * find_paths('dac', 'out')
)