class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [-1] * 255
        n = len(s)
        l=r=maxl=0
        while r<n:
            if hash[ord(s[r])] != -1:
                if hash[ord(s[r])]>=l:
                    l = hash[ord(s[r])]+1
            leng = r - l + 1
            maxl = max(leng, maxl)
            hash[ord(s[r])] = r
            r+=1
        return maxl
