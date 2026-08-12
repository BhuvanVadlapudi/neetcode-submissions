class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cond = n//2 
        max_val = min(nums)
        for i in nums:
            count_n = nums.count(i)
            if(count_n > cond):
                max_value = max(max_val,i)
        return max_value
        