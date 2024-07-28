class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s) - 1
        list = [0] * len(s)
        for item in range(len(s)):
            list[item] = s[item]
        for item in range(len(s)):
            s[item] = list[size]
            size = size - 1