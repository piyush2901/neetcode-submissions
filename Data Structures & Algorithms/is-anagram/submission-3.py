class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hsh_set1 = defaultdict(int)
        hsh_set2 = defaultdict(int)

        for i in range(len(s)):
            hsh_set1[s[i]] += 1
            hsh_set2[t[i]] += 1

        return hsh_set1 == hsh_set2