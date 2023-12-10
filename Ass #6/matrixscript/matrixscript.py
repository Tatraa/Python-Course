import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ''

for i in range(len(matrix[0])):
    for row in matrix:
        s += row[i]

pattern = re.compile(r'(?<=[a-zA-Z0-9])(\W+)(?=[a-zA-Z0-9])')
sub = pattern.sub(' ', s)
print(sub)
