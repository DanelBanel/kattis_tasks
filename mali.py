from dataclasses import dataclass
import sys

@dataclass
class MinMax:
    min: int
    max: int
def get_input():
    input_data = sys.stdin.read().split("\n")
    return input_data
# def find_max_comb(input_data: str) -> str:
a_min_max = MinMax(101, 0)
b_min_max = MinMax(101, 0)
output = []
num_lines = int(input())
for idx in range(num_lines):
    try:
        line = input()
    except EOFError:
        break
    a, b = map(int, line.split())
    # print(line)
    # print(f"a: {a}, b: {b}")
    a_min_max.min = min(a_min_max.min, a)
    a_min_max.max = max(a_min_max.max, a)
    b_min_max.min = min(b_min_max.min, b)
    b_min_max.max = max(b_min_max.max, b)
    max_comb = max(a_min_max.max + b_min_max.min, a_min_max.min + b_min_max.max)
    # output.append(str(max_comb))
    print(max_comb)


# if __name__ == "__main__":
#     assert find_max_comb(input_data_1) == """10
# 10
# 9"""
#     assert find_max_comb(input_data_2) == """2
# 3
# 4"""



"""
from dataclasses import dataclass

@dataclass
class MinMax:
    min: int
    max: int

a_min_max = MinMax(101, 0)
b_min_max = MinMax(101, 0)
output = []

input_data = input()
for idx, line in enumerate(input_data.split("\n")):
    if idx == 0:
        continue
    a, b = map(int, line.split())
    print(line)
    print(f"a: {a}, b: {b}")
    a_min_max.min = min(a_min_max.min, a)
    a_min_max.max = max(a_min_max.max, a)
    b_min_max.min = min(b_min_max.min, b)
    b_min_max.max = max(b_min_max.max, b)
    max_comb = max(a_min_max.max + b_min_max.min, a_min_max.min + b_min_max.max)
    output.append(str(max_comb))

print("\n".join(output))

"""