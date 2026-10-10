class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
        while(i < n//2):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp
            i += 1
        