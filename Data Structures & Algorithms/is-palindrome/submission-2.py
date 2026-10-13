class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s:
            if(((ord(i) in range(65,91)) or ord(i) in range(97,123)) or ord(i) in range(48,58)):
                ns += i.lower()
        print(ns)
        if(ns == ns[::-1]):
            return True
        return False