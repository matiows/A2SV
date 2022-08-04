class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def recursiveFind(x, candis):
            for i in range(x, len(candidates)):
                nums = candis.copy()
                if sum(nums) + candidates[i] == target:
                    nums.append(candidates[i])
                    result.append(nums)
                    return
                elif sum(nums) + candidates[i] < target:
                    nums.append(candidates[i])
                    recursiveFind(i, nums)
                else:
                    return

        recursiveFind(0,[])
        return result       
        