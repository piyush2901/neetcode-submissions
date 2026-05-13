class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

      n = len(nums)
      
      pref_arr = [1] * n
      pref_arr[0] = 1
      
      suff_arr = [1] * n
      suff_arr[n-1] = 1


      for i in range(1, n):
        pref_arr[i] = pref_arr[i-1] * nums[i - 1]

      for i in range(n - 2, -1, -1):
        suff_arr[i] = suff_arr[i + 1] * nums[i + 1]

      print(suff_arr)
      print(pref_arr)

      res = [0]*n

      for i in range(n):
        res[i] = pref_arr[i] * suff_arr[i]

      return res