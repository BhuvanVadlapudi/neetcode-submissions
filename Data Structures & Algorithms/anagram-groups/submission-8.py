class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_strs= strs.copy()
        group_anagrams = []

        anagrams_dict = {}

        for word in strs:
            s_word = "".join(sorted(word))
            if(s_word not in anagrams_dict):
                anagrams_dict[s_word] = [word]
            else:
                anagrams_dict[s_word] += [word]
        
        return (list(anagrams_dict.values()))

        # for i in range(len(list_strs)):
        #     if list_strs[i] is None:
        #         continue
        #     root_word = list_strs[i]
        #     anagram_cluster = [root_word]
        #     sort_root_word = sorted(root_word)
        #     list_strs[i] = None
        #     for j in range(i+1,len(list_strs)):
        #         word = list_strs[j]
        #         if(word is not None):
        #             sort_word = sorted(word)
        #             if(sort_root_word == sort_word):
        #                 anagram_cluster += [list_strs[j]]
        #                 list_strs[j] = None
        #     anagram_cluster = sorted(anagram_cluster)
        #     if(anagram_cluster not in group_anagrams):
        #         group_anagrams += [anagram_cluster]
        # return group_anagrams

        # list_strs = strs.copy()





        # group_anagrams = []

        # for i in range(len(list_strs)):
        #     if list_strs[i] is None:
        #         continue

        #     root_word = list_strs[i]

        #     anagram_cluster = [root_word]

        #     list_strs[i] = None

        #     sort_root_word = sorted(root_word)

        #     for j in range(i + 1, len(list_strs)):
        #         word = list_strs[j]

        #         if word is not None:
        #             sort_word = sorted(word)

        #             if sort_root_word == sort_word:
        #                 anagram_cluster.append(word)

        #                 list_strs[j] = None

        #     group_anagrams.append(anagram_cluster)

        # return group_anagrams




    # def count_chars(unique_chars, word):
    #     chars_count = {}
    #     for i in unique_chars:
    #         c = word.count(i)
    #         chars_count[i] = c
    #     return chars_count

    # for i in range(len(list_strs)):
    #     root_word = list_strs[i]
    #     if root_word != None:
    #         anagram_list = [root_word]
    #         list_strs[i] = None
    #         if(root_word == ""):
    #             group_anagrams += [anagram_list]
    #             continue
    #         root_word_chars = list(set(root_word))
    #         root_word_chars_count = count_chars(root_word_chars, root_word)

    #     for j in range(i + 1, len(list_strs)):
    #         if list_strs[j] != None:
    #             word = list_strs[j]
    #             word_chars = list(set(word))
    #             word_chars_count = count_chars(word_chars, word)

    #             if root_word_chars_count == word_chars_count:
    #                 if word in anagram_list:
    #                     continue
    #                 anagram_list += [word]
    #                 list_strs[j] = None
    #     anagram_list = sorted(anagram_list)
    #     if anagram_list not in group_anagrams:
    #         group_anagrams += [anagram_list]
    # return group_anagrams
