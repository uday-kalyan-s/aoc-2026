import functools

data = open("sample.txt").read().splitlines()

beam_loc = data[0].find('S')

@functools.cache
def split_cnt(level, beam_loc):
    if level == len(data)-1:
        return 1
    if data[level][beam_loc] == '^':
        cnt = 0
        if beam_loc > 0:
            cnt += split_cnt(level+1, beam_loc-1)
        if beam_loc < len(data[0]):
            cnt += split_cnt(level+1, beam_loc+1)
        return cnt
    else:
        return split_cnt(level+1, beam_loc)
    
print(split_cnt(0, beam_loc))