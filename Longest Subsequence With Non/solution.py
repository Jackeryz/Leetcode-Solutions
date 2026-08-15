class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        t = nz = 0
        for n in nums:
            nz |= n > 0
            t ^= n
        return nz * (len(nums) - (not t))
