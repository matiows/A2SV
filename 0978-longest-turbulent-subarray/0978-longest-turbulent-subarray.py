class Solution:
    def check(self, arr, index):
        if arr[index] > arr[index-1]:
            return 1
        elif arr[index] < arr[index-1]:
            return 2
        else:
            return 0
        
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        flag = 0
        left, right = 0, 1
        if len(arr) == 1:
            return 1
        
        if min(arr) == max(arr):
            return 1
        
        best = 2
        
        for right in range(1, len(arr)):
            # print(flag, left, right)
            if flag == 0:
                flag = self.check(arr, right)
                left = right - 1
                continue
                
            if arr[right] > arr[right - 1]:
                if flag == 2:
                    # print('yo')
                    best = max(best, right - left + 1)
                    flag = 1
                else:
                    # print('oy')
                    flag = self.check(arr, right)
                    left = right - 1
                
            elif arr[right] < arr[right - 1]:
                if flag == 1:
                    # print('go')
                    best = max(best, right - left + 1)
                    flag = 2
                else:
                    # print('og')
                    flag = self.check(arr,right)
                    left = right - 1
                
            else:
                # print('gg')
                flag = self.check(arr, right)
                left = right - 1
            
            # print(best)
                
        return best  