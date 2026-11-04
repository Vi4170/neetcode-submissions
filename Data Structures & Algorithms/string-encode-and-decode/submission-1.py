class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            res.append(s[left:right])
            left = right
        return res
