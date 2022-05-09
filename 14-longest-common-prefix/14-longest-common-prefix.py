class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for i in range(len(strs[0])):
            check = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != check:
                    check = ""
                    break
            if check != "":
                result.append(check)
            else:
                break
        answer = ''.join(str(e) for e in result)
        return answer
            
            