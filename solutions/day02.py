from utils.SolutionRunner import SolutionRunner

class Day02(SolutionRunner):

    def is_safe(self, entry):
        inc_flag = True
        dec_flag = True

        for j in range(len(entry) - 1):
            diff = entry[j+1] - entry[j]
            if 1 <= diff <= 3:
                dec_flag = False
            elif -3 <= diff <= -1:
                inc_flag = False
            else:
                inc_flag = False
                dec_flag = False
                break
        return inc_flag or dec_flag

    def part1(self):
        data = self.input_reader.read_lines()
        data = [[int(num) for num in nums.split()] for nums in data]
        
        count = 0
        for entry in data:
            if self.is_safe(entry):
                count += 1
            
        return count
    

    def part2(self):
        data = self.input_reader.read_lines()
        data = [[int(num) for num in nums.split()] for nums in data]

        unsafe = []
        count = 0
        for entry in data:
            if self.is_safe(entry):
                count += 1
            else:
                unsafe.append(entry)
        
        for entry in unsafe:
            for i in range(len(entry)):
                modified = entry[:i] + entry[i + 1:]
                if self.is_safe(modified):
                    count += 1
                    break

        return count
