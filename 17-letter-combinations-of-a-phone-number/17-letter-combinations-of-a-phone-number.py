class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        dic={}
        dic[2] = ['a','b','c']
        dic[3] = ['d','e','f']
        dic[4] = ['g','h','i']
        dic[5] = ['j','k','l']
        dic[6] = ['m','n','o']
        dic[7] = ['p','q','r','s']
        dic[8] = ['t','u','v']
        dic[9] = ['w','x','y','z']
        
        result = dic[int(digits[0])]
        for i in range(1, len(digits)):
            temp = result
            result = []
            for num in temp:
                for digit in dic[int(digits[i])]:
                    result.append(num+digit)
        return result
                
                