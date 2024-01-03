class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        prev=0
        for row in bank:
            dev=row.count('1')
            if dev>0:
                ans+=dev*prev
                prev=dev
        return ans
["011001","000000","010100","001000"]
