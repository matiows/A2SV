class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def helper(index):
            if arr[index] == 0:
                return True
            
            forward = index + arr[index]
            backward = index - arr[index]
            
            if forward not in visited and forward < len(arr):
                visited.add(forward)
                if helper(index + arr[index]):
                    return True
                
            if backward not in visited and backward >= 0:
                visited.add(backward)
                if helper(index - arr[index]):
                    return True
                
            return False
        
        return helper(start)
        