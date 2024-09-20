class Solution:
    def shortestPalindrome(self, s: str) -> str:
        cnt = self.kmp(s[::-1],s)
        return s[cnt:][::-1] + s
    def kmp(self,rev: str, actual: str)-> int:
        new_str = actual + '#' + rev
        pi = [0] * len(new_str)
        i = 1
        k = 0
        while i< len(new_str):
            if new_str[i] == new_str[k]:
                k+=1
                pi[i]=k
                i+=1
            else:
                if k>0:
                    k = pi[k-1]
                else:
                    pi[i] = 0
                    i+=1
        return pi[-1]

