import sys
import re
sys.path.append('../aoc_common')
from aoc_common import aoc_common

# This doesn't work and I have no clue why. It does in every test input I gave it. So I'm
# calling it a day. Fuck it.

def parse_input(inp: str):
    sum_ = 0
    while re.search(r"don\'t\(\).*?do\(\)", inp):
        inp = re.sub(r"don\'t\(\).*?do\(\)", '', inp)
    if re.search(r"don\'t\(\).*$", inp):
        inp = re.sub(r"don\'t\(\).*$", '', inp)
    print(inp)
    for match in re.findall(r"mul\([0-9]+\,[0-9]+\)", inp):
        u,v = re.search(r"mul\(([0-9]+)\,([0-9]+)\)", match).group(1,2)
        sum_ += int(u)*int(v)
    print(sum_)

if __name__ == "__main__":
    parse_input(aoc_common.get_puzzle(2024,3).strip())
    #parse_input("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
