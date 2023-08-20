class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placements = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftIsFree = i == 0 or flowerbed[i - 1] == 0
                rightIsFree = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if leftIsFree and rightIsFree:
                    #place a flower
                    flowerbed[i] = 1
                    placements += 1

                if placements >= n:
                    return True

        return placements >= n

        # TC: O(n)
        # SC: O(1)