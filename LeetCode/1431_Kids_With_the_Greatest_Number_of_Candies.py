class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #find kid with the most candy
        max_candies_held = max(candies)
        res = []

        #build the result array by iterating over the kids and comparing thier candies + extra to the kid with max_candies 
        for kid_candies in candies:
            if kid_candies + extraCandies >= max_candies_held:
                res.append(True)
            else:
                res.append(False)

        return res

# TC: O(n)
# SC: O(n)