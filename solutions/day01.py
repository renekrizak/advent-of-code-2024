from utils.SolutionRunner import SolutionRunner
from collections import Counter

class Day01(SolutionRunner):
    def part1(self):
        data = self.input_reader.read_lines()
        left_list = []
        right_list = []

        for line in data:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

        left_list = sorted(left_list)
        right_list = sorted(right_list)

        dist = 0
        for i in range(len(left_list)):
            dist += abs(left_list[i] - right_list[i])
        return dist

    def part2(self):
        data = self.input_reader.read_lines()
        left_list = []
        right_list = []

        for line in data:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

        right_counts = Counter(right_list)

        similarity_score = 0
        for num in left_list:
            similarity_score += num * right_counts.get(num, 0)
        return similarity_score