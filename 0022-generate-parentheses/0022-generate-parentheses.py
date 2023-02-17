class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def dp(op_count, cl_count, path):
            if op_count == 0 and cl_count == 0:
                answer.append("".join(path))
                return
            
            if op_count > 0:
                dp(op_count - 1, cl_count, path + ["("])
        
            if op_count == 0 or op_count < cl_count:
                dp(op_count, cl_count - 1, path + [")"])
                
        dp(n, n, [])
        
        return answer
                
            