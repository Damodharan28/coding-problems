class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        size = len(strs[0])
        res = ""
        for i in range(size):
            common = ""
            for word in strs:
                if common == "" :             
                    common = word[i]
                elif common == word[i]:
                    common = word[i]
                else:
                    common = ""
                    return res
                
            res += common

        return res
