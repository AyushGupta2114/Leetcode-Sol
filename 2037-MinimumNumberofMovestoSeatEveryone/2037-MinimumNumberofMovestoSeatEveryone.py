class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        k=0
        for i in range(0,len(seats)) :
        seats.sort()
        students.sort()
            k+=abs(seats[i]-students[i])
        return k 
        
[
