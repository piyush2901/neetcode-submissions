class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def get_freq(test_str):
            hsh_set = defaultdict()
            
            for char in test_str:
                if char in hsh_set:
                    hsh_set[char] += 1
                else:
                    hsh_set[char] = 1
            
            return hsh_set


        s_set = get_freq(s)
        t_set = get_freq(t)

        return s_set == t_set