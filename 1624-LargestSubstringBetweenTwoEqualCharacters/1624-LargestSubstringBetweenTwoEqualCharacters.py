                # Update the maximum distance if needed
                max1 = max(max1, appearances[char]["last"] - appearances[char]["first"])
            else:
                # If the character is already in the dictionary, update its last appearance
                appearances[char]["last"] = i
                appearances[char] = {"first": i, "last": i}
                # If the character is not in the dictionary, store its first appearance
            if char not in appearances:
        max1 = -1

        for i, char in enumerate(s):

# Variable to store the maximum distance
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

# Dictionary to store the first and last appearance of each character
        appearances = {}

class Solution:
"aa"
