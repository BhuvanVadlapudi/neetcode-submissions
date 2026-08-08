class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        unique_chars = list(set(s))
        char_lengths = {

        }
        for i in unique_chars:
            count_s = s.count(i)
            count_t = t.count(i)
            if(count_s != count_t):
                return False
        return True

