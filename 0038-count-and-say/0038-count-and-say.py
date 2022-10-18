class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper(string):
            ans = []
            count = 1
            for idx in range(1,len(string)):
                if string[idx] == string[idx - 1]:
                    count += 1
                else:
                    ans.append(str(count) + string[idx - 1])
                    count = 1
            ans.append(str(count) + string[-1])
            return "".join(ans)
        
        def recur(num):
            
            if num == 1:
                return '1'
                
            string = recur(num-1)
            return helper(string)
            
        return recur(n)