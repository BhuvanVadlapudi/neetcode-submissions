class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[k] = nums[i]
                k += 1


        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-1-i):
        #         if(nums[j] == val):
        #             temp = nums[j+1]
        #             nums[j+1] = nums[j]
        #             nums[j] = temp
        # print(nums)
        
        # count_val = nums.count(val)
        # k = len(nums) - count_val
        
        # print(nums_list)
        return k