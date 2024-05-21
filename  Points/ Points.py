class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        
        def backtrack(start, path):
        print(result)
        return result
        
[
