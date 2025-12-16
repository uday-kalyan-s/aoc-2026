data = open("input.txt").read()

machines = []

def toggle(state, button):
    state = list(state)
    for i in button:
        state[i] = '.' if state[i] == '#' else '#'
    return ''.join(state)

def get_req_toggles(on_switches, buttons):
    cost = 0
    present_states = set(['.'*len(on_switches)])
    while True:
        if on_switches in present_states:
            return cost
        cost += 1
        new_states = set()
        for state in present_states:
            for button in buttons:
                new_states.add(toggle(state, button))
        present_states = new_states

sm = 0

for line in data.splitlines():
    els = line.split(' ')
    on_switches = els[0][1:-1]
    buttons = []
    for but in els[1:-1]:
        buttons.append(
            list(
                map(
                    int,
                    filter(
                        lambda x: x != '',
                        but[1:-1].split(',')
                    )
                )
            )
        )
    sm += get_req_toggles(on_switches, buttons)

print(sm)