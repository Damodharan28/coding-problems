class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        res = 0
        for word in words:
            for ch in word:
                if ch not in allowed_set:
                    break
            else:
                res += 1

        return res
