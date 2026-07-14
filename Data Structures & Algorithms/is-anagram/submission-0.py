class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        ch_count = {}

        for ch in s:
            ch_count[ch] = ch_count.get(ch, 0) + 1

        for ch in t:
            if ch not in ch_count:
                return False

            ch_count[ch] -= 1

            if ch_count[ch] < 0:
                return False
        
        return True