            if column_values != expected_set:
                return False
        expected_set = set(range(1, len(matrix) + 1))
        for col in range(len(matrix[0])):
            column_values = set(matrix[row][col] for row in range(len(matrix)))
                return False

        # Check columns
            row_values = sorted(matrix[i])
            if row_values != list(range(1, len(matrix) + 1)):
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Check rows
        for i in range(len(matrix)):
class Solution:

from typing import List
# please check carefully
[
