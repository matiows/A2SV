class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        point1 = 0
        point2 = 0
        nums = []
        
        while (point1 + point2 < (len(nums1) + len(nums2)+1) / 2):
            if point1 == len(nums1):
                nums.append(nums2[point2])
                point2 += 1
                continue
            
            if point2 == len(nums2):
                nums.append(nums1[point1])
                point1 += 1
                continue
                
            if nums1[point1] < nums2[point2]:
                nums.append(nums1[point1])
                point1 += 1
            
            else:
                nums.append(nums2[point2])
                point2 += 1
                
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (nums[-1] + nums[-2]) / 2
        
        else:
            return nums[-1]