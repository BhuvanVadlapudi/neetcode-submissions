from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        cond = n//2 
        max_val = min(nums)
        unique_nums = list(set(nums))
        for i in unique_nums:
            count_n = nums.count(i)
            if(count_n > cond):
                max_value = max(max_val,i)
        return max_value
        