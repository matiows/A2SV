class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def allPossible(stack, index):
            if index == len(s): 
                result.append(''.join(stack))
                return
            
            for ch in set([s[index].lower(), s[index].upper()]):
                stack.append(ch)
                allPossible(stack, index + 1)
                stack.pop()

        allPossible([], 0)
        return result