import os.path
import sys
import requests

class aoc_common:
    def get_puzzle(year: int, day: int)->str:
        try:
            if not os.path.isfile('../session'):
                raise Exception("You need to create a file named 'session' in the top directory (aoc2024). Log in to Advent of code from your browser, then get the session token and paste it into that file. Then try again!")
                sys.exit(-1)
            session = ""
            with open('../session', 'r') as sf:
                session = sf.read().strip()
            s = requests.Session()
            r = s.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={'session': session})
            return r.text
        except Exception as e:
            raise e
