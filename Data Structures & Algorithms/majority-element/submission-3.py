from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashDict = defaultdict(int)
        n = len(nums)
        cond = n//2

        for i in nums:
            hashDict[i] += 1
        
        max_count = max(hashDict.values())
        for key,value in hashDict.items() :
            if(value == max_count):
                return key

        # n = len(nums)
        # cond = n//2 
        # max_val = min(nums)
        # unique_nums = list(set(nums))
        # for i in unique_nums:
        #     count_n = nums.count(i)
        #     if(count_n > cond):
        #         max_value = max(max_val,i)
        # return max_value
        