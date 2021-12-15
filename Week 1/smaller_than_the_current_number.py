class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        count = [0]*length
        for i in range (0 , length):
            for j in range (0 , length):
                if nums[j] < nums[i] and j!=i:
                    count[i]+=1
        return count