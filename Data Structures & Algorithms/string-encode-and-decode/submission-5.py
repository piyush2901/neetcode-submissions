class Solution:

    def encode(self, strs: List[str]) -> str:

        encod_s = ""

        for s in strs:
            str_len = len(s)
            encod_s += str(str_len)
            encod_s += "#"
            encod_s += s

        return encod_s

    def decode(self, s: str) -> List[str]:
        
        print(s)

        ans = []

        left = 0

        while left < len(s):
            
            right = left


            while s[right] != '#':

                right += 1
            
            str_len = int(s[left : right])

            ans.append(s[right + 1 : right + str_len + 1])

            left = right + str_len + 1

        return ans
