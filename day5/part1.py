data = open('input.txt').read()

ranges_raw, ings_raw = data.split('\n\n')

ranges = [tuple(map(int, r.split('-'))) for r in ranges_raw.splitlines()]
ings = list(map(int, ings_raw.splitlines()))

fresh = 0

for i in ings:
    for s, e in ranges:
        if s <= i <= e:
            fresh += 1
            break

print(fresh)