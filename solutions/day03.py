from utils.SolutionRunner import SolutionRunner
import re


class Day03(SolutionRunner):

    def part1(self):

        data = self.input_reader.read_text()
        hits = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
        result = sum(int(hit[0]) * int(hit[1]) for hit in hits)
        return result
    
    def part2(self):
        data = self.input_reader.read_text()

        data = re.sub(r"don't\(\).*?(?:do\(\)|$)", "", data, flags=re.DOTALL)
        hits = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
        result = sum([int(hit[0])*int(hit[1]) for hit in hits])
        return result

