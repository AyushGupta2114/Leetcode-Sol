                # Update the maximum distance if needed
                max1 = max(max1, appearances[char]["last"] - appearances[char]["first"])
            else:
                # If the character is already in the dictionary, update its last appearance
                appearances[char]["last"] = i
                # If the character is not in the dictionary, store its first appearance
                appearances[char] = {"first": i, "last": i}

# Dictionary to store the first and last appearance of each character
        appearances = {}

# Variable to store the maximum distance
        max1 = -1

        for i, char in enumerate(s):
            if char not in appearances:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

class Solution:
"aa"
