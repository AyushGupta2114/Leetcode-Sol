#             a=365
#         m=1
#         days=0
#         if a==366:
#             a=366
#         elif (year % 4 ==0) and (year % 100 != 0):
#             a=366
#         else:
#         if (year % 400 == 0) and (year % 100 == 0):
class Solution:
#     def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#         a=0
# class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A") 
3
