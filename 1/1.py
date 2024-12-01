import sys
import re
import itertools
sys.path.append('../aoc_common')
from aoc_common import aoc_common

def parse_input(inp: str):
    u,v = zip(*(s.split() for s in list(map(lambda x: re.sub('\s+',' ',x), inp.split('\n')))))
    u,v = list(u),list(v)
    u.sort()
    v.sort()
    print(sum(list(map(lambda x,y: abs(int(y)-int(x)), u,v))))

if __name__ == "__main__":
    parse_input(aoc_common.get_puzzle(2024,1).strip())
