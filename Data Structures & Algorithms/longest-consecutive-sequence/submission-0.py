class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        hsh_set = set(nums)

        max_len = 0

        for num in nums:
            if num - 1 not in hsh_set:
                seq_len = 0

                while (num + seq_len) in hsh_set:
                    seq_len += 1

                max_len = max(max_len, seq_len)

        return max_len