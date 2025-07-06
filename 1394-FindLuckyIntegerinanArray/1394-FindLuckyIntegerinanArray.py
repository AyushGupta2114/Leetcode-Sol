from collections import Counter

class Solution:
        freq = Counter(arr)
        lucky = [num for num, count in freq.items() if num == count]
        return max(lucky) if lucky else -1  # -1 is often used when no lucky number exists
from typing import List
import numpy as np

    def findLucky(self, arr: List[int]) -> int:
