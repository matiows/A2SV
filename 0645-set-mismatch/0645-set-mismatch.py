class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = [0,0]
        for x in range(len(count)+1):
            if count[x+1] == 2:    
                result[0] = x+1
            elif count[x+1] == 0:
                result[1] = x+1
        return result