import sys
import re
sys.path.append('../aoc_common')
from aoc_common import aoc_common

def parse_input(inp: str):
    sum_ = 0
    for match in re.findall(r"mul\([0-9]+\,[0-9]+\)", inp):
        u,v = re.search(r"mul\(([0-9]+)\,([0-9]+)\)", match).group(1,2)
        sum_ += int(u)*int(v)
    print(sum_)

if __name__ == "__main__":
    parse_input(aoc_common.get_puzzle(2024,3).strip())
