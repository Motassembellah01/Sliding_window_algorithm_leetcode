class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        longest = 0
        maxf = 0
        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            maxf = max(count[char], maxf)
            while r - l + 1 - maxf - k > 0:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest