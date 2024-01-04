class Solution:
    def minOperations(self, nums: List[int]) -> int:
       ·ans=0
········a=Counter(nums)
········print(a)
········if(1·in·a.values()):
············return·-1
········for·i,j·in·a·.items():
············if(j%3==0):
················ans+=j//3
············else:
················ans+=j//3+1
········return·ans
        
        
[2,3,3,2,2,4,2,3,4]
