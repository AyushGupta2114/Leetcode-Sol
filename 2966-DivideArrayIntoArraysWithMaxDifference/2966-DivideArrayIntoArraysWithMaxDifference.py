        a=[]
        for i in range(0,len(nums),3):
            if(nums[i+2]-nums[i]>k) or (nums[i+1]-nums[i]>k):
                return []
            else:
                a.append(nums[i:i+3])
        nums.sort()
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
class Solution:

        return a
