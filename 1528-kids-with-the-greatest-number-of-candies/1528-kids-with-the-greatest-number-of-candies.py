class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        resArr = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            resArr.append(candies[i] + extraCandies >=  maxCandies)
        return resArr