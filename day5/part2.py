data = open('input.txt').read()

ranges_raw, ings_raw = data.split('\n\n')

ranges = [tuple(map(int, r.split('-'))) for r in ranges_raw.splitlines()]

# compures r2 - r1
def compute_disj(r1, r2):
    if r1[1] < r2[0] or r2[1] < r1[0]: # disjoint
        return [r2]
    if r1[0] <= r2[0] and r1[1] >= r2[1]: # r2 in r1, remove
        return []
    if r2[0] <= r1[0] and r2[1] >= r1[1]: # r1 in r2, split
        return [(r2[0], r1[0]-1), (r1[1]+1, r2[1])]
    if r2[0] <= r1[0]: # r2 before r1 after, intersect
        return [(r2[0], r1[0]-1)]
    if r1[0] <= r2[0]: # r1 before r2
        return [(r1[1]+1, r2[1])]
    print("fuckup hua")
    print(r1, r2)
    exit()

def form_range(r, jr_comb):
    if len(jr_comb) == 0:
        return [r]
    already_ins = jr_comb[0]
    diff = compute_disj(already_ins, r)
    trans_mut = []
    for e in diff:
        trans_mut += form_range(e, jr_comb[1:])
    return trans_mut

jr_comb = [ranges[0]]
for r in ranges[1:]:
    jr_comb += form_range(r, jr_comb.copy())

c = 0

for s, e in jr_comb:
    c += e-s+1

print(c)