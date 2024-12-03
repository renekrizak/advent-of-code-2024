
import argparse
import importlib

class SolutionRunner:
    def __init__(self, day: int):
        self.day = day
        from utils.InputReader import InputReader
        self.input_reader = InputReader(day)

    def run(self, part: int):
        if part == 1:
            result = self.part1()
            print(f'Day {self.day} - Part 1 ----> {result}')
        elif part == 2:
            result = self.part2()
            print(f'Day {self.day} - Part 2 ----> {result}')
        else:
            raise ValueError(f'Invalid part: {part}, must be 1 or 2')
        
    def part1(self):
        raise NotImplementedError('Implement part 1 before testing')
        
    def part2(self):
        raise NotImplementedError('Implenent part 2 before testing')
        
    @staticmethod
    def run_from_console():
        parser = argparse.ArgumentParser()
        parser.add_argument('day', type=int, help='Day of the challenge, e.g. 1 for day one')
        parser.add_argument('part', type=int, choices=[1,2], help='Part of the challenge, either 1 or 2')
        args = parser.parse_args()

        try:
            module = importlib.import_module(f'solutions.day{args.day:02}')
            solution_class = getattr(module, f'Day{args.day:02}')
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f'Solution for day {args.day} not found')

        solution = solution_class(day=args.day)
        solution.run(part=args.part)