class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            for i in range(len(output)):
                output += [output[i] + [num]]
        return output