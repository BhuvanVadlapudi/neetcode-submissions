class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = []
        for i in nums:
            prev = i-1
            if(prev not in numSet):
                seq = [i]
                while(i+1 in numSet):
                    i += 1
                    seq += [i]   
                print(seq)
                if(len(seq) > len(res)):
                    res = seq
        return len(res)

        #Brute-Force Approach

        # nums.sort()
        # # print(nums)
        # res = []
        # for i in range(len(nums)):
        #     seq = [nums[i]]
        #     for j in range(i+1,len(nums)):
        #         if(abs(seq[-1] - nums[j]) > 1):
        #             break
        #         if(abs(seq[-1] - nums[j]) == 1):
        #             seq.append(nums[j])
        #     # print(seq)
        #     if(len(seq) > len(res)):
        #         res = seq
        # return len(res)