class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                result[temp] = i - temp    
                
            stack.append(i)
            
        return result