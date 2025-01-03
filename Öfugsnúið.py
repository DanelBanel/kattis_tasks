import sys
from typing import List


input_len = int(input())
# print(input_len)

input_data: List[int] = sys.stdin.read().split("\n")
# for idx in range(input_len):
#     print(input())
#     input_data.append(int(input()))

# print(sorted(input_data, reverse=True))
for test in input_data[::-1]:
    print(test)