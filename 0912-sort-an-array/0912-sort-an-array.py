class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(l, m, r):
            
            sorted_list = []
            p1 = l
            p2 = m+1
            while p1 <= m or p2 <= r:
                if p2 > r or (p1 <= m and nums[p1] < nums[p2]):
                    sorted_list.append(nums[p1])
                    p1 += 1
                    
                else:
                    sorted_list.append(nums[p2])
                    p2 += 1
                    
            for i in range(l, r + 1):
                nums[i] = sorted_list[i - l]
            # print('m',l,m,r,nums,sorted_list)         
        
        def helper(l,r):
            # print(l,r)
            if l >= r:
                return
            
            m = (l + r)//2
            helper(l, m)
            helper(m+1, r)
            merge(l, m, r)
            
        helper(0, len(nums)-1)
        return nums