class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        sm = 1
        while(True):
            if(sm not in nums):
                return sm
                break
            sm += 1

        # a = sorted(nums)
        # pn = {}
        # for i in range(len(nums)):
        #     if(nums[i] > 0):
        #         pn[i] = i
        # print(pn)
        # size = 0
        # for i in range(len(a)):
        #     if(a[i] > 0):
        #         size = len(a) - i
        #         break
    
        # newa = [i for i in range(1,size+1)]
        # for i in newa:
        #     if(pn.get(i) is None):
        #         return i
        # return 1


        # a = sorted(nums)
        # pn = []
        # for i in range(len(nums)):
        #     if(nums[i] > 0):
        #         pn = a[i:]
        #         break
        # newa = [i  for i in range(pn[0],pn[0]+len(pn))]
        # for i in range(len(pn)):
        #     if(pn[i] != newa[i]):
        #         return newa[i]
