class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for str1 in strs:
            meta_data = str(len(str1)) + "#" + str1
            encoded_str += meta_data

        return encoded_str

    def decode(self, s: str) -> List[str]:

        ans = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            str_len = int(s[i:j])
            i = j + 1
            j = i + str_len

            ans.append(s[i:j])
            i = j

        return ans
