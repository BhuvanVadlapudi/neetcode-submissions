class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if(nums[j] == val):
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        print(nums)
        
        count_val = nums.count(val)
        k = len(nums) - count_val
        
        # print(nums_list)
        return k