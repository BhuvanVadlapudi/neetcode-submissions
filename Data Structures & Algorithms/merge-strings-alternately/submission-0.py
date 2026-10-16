class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = len(word1) - 1
        p2 = len(word2) - 1

        res = ""

        f1 , f2 = True, True
        while(f1 or f2):
            if(p1 >= 0):
                res += word1[len(word1) - 1 - p1]
                p1 -= 1
            else :
                f1 = False

            if(p2 >= 0):
                res += word2[len(word2) - 1 - p2]
                p2 -= 1
            else:
                f2 = False
        return res