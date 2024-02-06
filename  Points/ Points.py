class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            d[''.join(sorted(i))].append(i)
        return d.values()                    

                    
        
["eat","tea","tan","ate","nat","bat"]
