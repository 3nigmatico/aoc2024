import sys
sys.path.append('../aoc_common')
from aoc_common import aoc_common

def parse_input(inp: str):
    count = 0
    for l in inp.split('\n'):
        okp, okn = 0, 0
        nums = [int(x) for x in l.split(' ')]
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
            count += 1
    print(count)

if __name__ == "__main__":
    parse_input(aoc_common.get_puzzle(2024,2).strip())
