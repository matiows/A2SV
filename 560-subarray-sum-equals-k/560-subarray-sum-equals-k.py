class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefixsum = 0
        d = {0:1}

        for num in nums:
            prefixsum += num
            if prefixsum - k in d:
                ans += d[prefixsum - k]

            if prefixsum not in d:
                d[prefixsum] = 1
            else:
                d[prefixsum] += 1

        return ans