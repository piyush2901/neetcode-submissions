class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                seq_len = 1

                while (num + seq_len) in numSet:
                    seq_len += 1

                longest = max(seq_len, longest)

        
        return longest