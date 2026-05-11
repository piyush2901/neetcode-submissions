class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hsh_set1 = defaultdict(int)
        hsh_set2 = defaultdict(int)

        for char in s:
            hsh_set1[char] += 1
        
        for char in t:
            hsh_set2[char] += 1

        return hsh_set1 == hsh_set2