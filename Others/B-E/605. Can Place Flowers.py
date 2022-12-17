# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# Input: flowerbed = [0], n = 1
# Output: true

# Input: flowerbed = [1,0], n = 1
# Output: false
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1): #ignore the first and last added
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0

# Time = O(N)
# Space = O(N) is modification to flowerbed is consitered


# class Solution:
#     def isValidSpot(self, i, N, flowerbed):
#         if i == 0 and i < N - 1:
#             return flowerbed[i + 1] == 0
#         elif i == N - 1:
#             return flowerbed[i - 1] == 0
#         elif i < N -1 and i > 0:
#             return flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0 
#         else:
#             return True
            
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         N = len(flowerbed) 
            
#         for i in range(N):
#             if n == 0:
#                 return True
            
#             elif flowerbed[i] == 0 and self.isValidSpot(i, N, flowerbed):
#                 flowerbed[i] = 1
#                 n -= 1

#         return n == 0
    
# #  Space = O(1)
# #  Time = O(N)