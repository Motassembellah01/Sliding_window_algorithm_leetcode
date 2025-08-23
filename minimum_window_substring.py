class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        
        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        fullfilled = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                fullfilled += 1
            
            while fullfilled == need:
                windowSize = r - l + 1
                if windowSize < resLen:
                    resLen = windowSize
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    fullfilled -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res != [-1, -1] else ""