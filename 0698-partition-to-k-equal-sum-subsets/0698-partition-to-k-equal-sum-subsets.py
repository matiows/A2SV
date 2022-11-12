class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        target = total // k
        visited = 0
        visited |= (1 << 0)
        nums.sort(reverse = True)
        
        memo = {}
        def backtrack(index, count, subset_sum, visited):
            if count == 0:
                return True

            if subset_sum == target:
                return backtrack(0, count - 1, 0, visited)
            
            # if not visited & (1 << index) and (index, subset_sum) in memo:
            #     print('yy')
            #     return memo[(index, subset_sum)]

            result = False
            i = index + 1
            while not result and i < len(nums):
                if not visited & (1 << i) and (nums[i] + subset_sum) <= target:
                    visited |= (1 << i)
                    result |= backtrack(i, count, subset_sum + nums[i], visited)
                    visited &= ~(1 << i)
                i += 1

            # memo[(index, subset_sum)] = result
            return result
        
        return backtrack(0, k, nums[0], visited)
