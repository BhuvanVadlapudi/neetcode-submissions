
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        count_zeros = nums.count(0)
        print(count_zeros)
        if(count_zeros > 1):
            return [0]*len(nums)
        elif(count_zeros == 1):
            zeroth_index = nums.index(0)
            val = 1
            for i in nums:
                if(i != 0):
                    val *= i
            res = [0]*len(nums)
            res[zeroth_index] = val
            return res
        else:
            total_product = 1
            res = [None]*len(nums)
            for i in nums:
                total_product *= i
            for j in range(len(nums)):
                res[j] = total_product//nums[j]
            return res

        #Brute-Force Approach
        # res = []
        # for i in range(len(nums)):
        #     val = 1
        #     for j in range(len(nums)):
        #         if(i != j):
        #             val *= nums[j]
        #     res += [val]
        # return res