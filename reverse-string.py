class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s) - 1
        list = [0] * len(s)
        i = 0
        for item in range(len(s)):
            list[i] = s[i]
            i = i + 1
        i = 0
        for item in range(len(s)):
            s[i] = list[size]
            i = i + 1
            size = size - 1