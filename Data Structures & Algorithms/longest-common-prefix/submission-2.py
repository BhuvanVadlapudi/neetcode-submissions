class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # new_strs = sorted(strs,key=len)
        # prefix_check = ""
        # prefix=""
        # for j in range(len(new_strs[0])):
        #     prefix_check += strs[0][j]
        #     flag = 0
        #     for i in new_strs:
        #         if(i.startswith(prefix_check)):
        #             flag = 1
        #         else:
        #             flag = 0
        #             return prefix
        #     prefix = prefix_check
            
        # return prefix

        init_word = strs[0]

        for i in range(len(init_word)):
            for each_word in strs:
                if(i >= len(each_word) or each_word[i] != init_word[i]):
                    return init_word[:i]
        return init_word

