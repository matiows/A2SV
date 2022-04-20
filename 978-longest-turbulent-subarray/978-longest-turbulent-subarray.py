class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        self.count = 0
        self.result = self.count
        
        def comp(i, g):
            
            self.result = max(self.result, self.count)
            
            if i+1 >= len(arr):
                return self.result
            
            if arr[i] < arr[i+1]:
                if g: 
                    self.count += 1
                else:
                    self.count = 1
                return comp(i+1, False)
                
            if arr[i] > arr[i+1]:
                if not g:
                    self.count += 1
                else:
                    self.count = 1
                return comp(i+1, True)
            
            else:
                self.count = 0
                return comp(i+1, arr[i] > arr[i+1])
            
        return comp(0, arr[0] > arr[1]) + 1
