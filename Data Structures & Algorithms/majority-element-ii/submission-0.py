class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        numsMap = {}
        n = len(nums)
        for i in nums:
            if(numsMap.get(i) == None):
                numsMap[i] = 1
            else:
                numsMap[i] += 1
        for i in numsMap:
            print(i,": ",numsMap[i])
            if(numsMap[i] > n/3):
                res += [i]
        return res