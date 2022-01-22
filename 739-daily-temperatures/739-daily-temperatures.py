class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                temp = stack.pop()
                result[temp[0]] = i - temp[0]    
                
            stack.append([i, temperatures[i]])
            
        return result