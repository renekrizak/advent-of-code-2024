import os

class InputReader:
    def __init__(self, day: int):
        self.day = day
        self.file_path = f'solutions/day{self.day:02}.txt'
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f'Input file not found: {self.file_path}')
    
    def read_lines(self) -> list[str]:
        with open(self.file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    
    def read_text(self) -> str:
        with open(self.file_path, 'r') as file:
            return file.read().strip()
    
    def read_int(self) -> list[int]:
        return [int(line) for line in self.read_lines()] 