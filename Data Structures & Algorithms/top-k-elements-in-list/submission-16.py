class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashSet =  [[] for _ in range(len(nums)+1)]
        freq = {}

        # print(nums)
        for i in nums:
            freq[i] = freq.get(i,0) + 1
            # print(freq)
        for key,val in freq.items():
            hashSet[val].append(key)
            # print(hashSet)
        
        res_nums = []

        for i in range(len(hashSet)-1,0,-1):
            if(hashSet[i] != []):
                for j in hashSet[i]:
                    res_nums += [j]
                    k -= 1
                    if(k == 0):
                        return res_nums

            

        #using just list
        
        # list_vals = {}
        # for i in nums:
        #     if i not in list_vals.keys():
        #         list_vals[i] = [i]  
        #     list_vals[i] += [i]
        
        # new_list = []
        # for key,values in list_vals.items():
        #     new_list += [values]
        
        # new_list.sort(key=len)
        # new_seq = [j for i in new_list for j in i]
        # new_order = []
        # for i in new_seq:
        #     if(i not in new_order):
        #         new_order += [i]
        # new_order = new_order[::-1]
        # new_order = new_order[:k]
        # print(new_order)
        
        # return new_order

        #hashmap method (wrong)
        
        # hashValues = [0 for i in range(10)]
        # u_nums = list(set(nums))
        # for i in nums:
        #     key = i%10
        #     hashValues[key] += 1 

        # print(hashValues)

        # k_vals = []
        # newHashVal = hashValues.copy()
        # while(newHashVal != [0]*10):
        #     max_v = max(newHashVal)
        #     i = newHashVal.index(max_v)
        #     k_vals += [i]
        #     newHashVal[i] = 0
        # print(k_vals[:k])

        # return k_vals[:k]


        # new_nums = nums.sort()
        # for
        # i = 0
        # vals = []
        # while(k==0):
        #     if(i > len(unique_nums)):
        #         break
        #     count_n = nums.count(unique_nums[i])
        #     if(count_n > 1):
        #         vals += [unique_nums[i]]
        #         k -= 1
        #     i += 1    
