class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        right = len(nums) - 1
        right_product = [nums[right]]        
        
        while(right > 1):
            right -= 1
            right_product.append(right_product[-1] * nums[right])
        
        left_product = 1
        result = []
        
        for i in range(len(nums)):
            if i == 0:
                result.append(right_product.pop())
            
            elif i == len(nums)-1:
                result.append(left_product)
            
            else:
                temp = left_product * right_product.pop()
                result.append(temp)
                
            left_product *= nums[i]
            
        return result