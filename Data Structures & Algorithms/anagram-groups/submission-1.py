class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        def checkAnagram(str1, str2):

            if len(str1) != len(str2):
                return False

            hsh_set1 = {}
            hsh_set2 = {}

            for i, chr in enumerate(str1):

                if chr not in hsh_set1:
                    hsh_set1[chr] = hsh_set1.get(chr, 0) + 1

                hsh_set1[chr] += 1

            for i, chr in enumerate(str2):

                if chr not in hsh_set2:
                    hsh_set2[chr] = hsh_set2.get(chr, 0) + 1

                hsh_set2[chr] += 1

            return hsh_set1 == hsh_set2

        hsh_set = set()

        for i in range(len(strs)):
            if strs[i] not in hsh_set:
                sblist = [strs[i]]
                for j in range(i+1, len(strs)):
                    # if strs[j] not in hsh_set:
                    if checkAnagram(strs[i], strs[j]):
                        sblist.append(strs[j])
                        hsh_set.add(strs[j])

            if sblist not in ans:
                ans.append(sblist)

        return ans 