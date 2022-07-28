class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            print (output)
            output += [curr + [num] for curr in output]
        
        return output