import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions'))

from utils.SolutionRunner import SolutionRunner
if __name__ == '__main__':
    SolutionRunner.run_from_console()