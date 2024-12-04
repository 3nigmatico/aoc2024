import sys
sys.path.append('../aoc_common')
from aoc_common import aoc_common

# Bruteforce for now. I might implement a better solution some other time.

def is_seq_valid(l: str, rem: int = -1):
    okp, okn = 0, 0
    nums = [int(x) for x in l.split(' ')]
    if rem > -1 and rem < len(nums):
        del nums[rem]
    for i in range(1, len(nums)):
        u,v = nums[i-1:i+1]
        if abs(u-v) < 1 or abs(u-v) > 3:
            okp = okn = 0
            break
        if u - v < 0:
            okn = 1
        elif u - v > 0:
            okn = -1
        if i == 1:
            okp = okn
        else:
            if okn != okp:
                okp = okn = 0
                break
    if (okp+okn) != 0 and okp == okn:
        return True
    return False

def parse_input(inp: str):
    count = 0
    for l in inp.split('\n'):
        if is_seq_valid(l):
            count += 1
        else:
            for i in range(0, len(l)):
                if is_seq_valid(l,i):
                    count += 1
                    break
    print(count)

if __name__ == "__main__":
    parse_input(aoc_common.get_puzzle(2024,2).strip())
