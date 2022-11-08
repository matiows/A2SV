class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        path = []
        result = []
        
        def backtrack(index, dots):
            if dots == 4:
                if index == len(s):
                    result.append(''.join(path[:-1]))
                    return
                return
                
            for i in range(index, min(index + 3, len(s))):
                if s[index] == '0' and i > index:
                    continue
                
                if int(s[index:i+1]) > 255:
                    continue
                    
                path.append(s[index:i+1])
                path.append('.')
                
                backtrack(i + 1, dots + 1)
                
                path.pop()
                path.pop()
                
        backtrack(0, 0)
        return result
        