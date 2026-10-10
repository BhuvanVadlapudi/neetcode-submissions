class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = []
        l,r = 0,0
        while(r < len(nums)):
            if(nums[r] not in new):
                new.append(nums[r])
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
            r += 1
        
        return len(new)