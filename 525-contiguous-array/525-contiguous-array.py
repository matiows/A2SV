class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = {}
        hashMap[0] = -1
        _max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in hashMap:
                _max = max(_max, i - hashMap[count])
            else:
                hashMap[count] = i 
        
        return _max