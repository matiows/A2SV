class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 11:
            return num
        
        if num > 10 ** 8:
            return 0

        original_num = list(str(num))
        new_num = original_num.copy()

        for i in range(len(original_num)):
            for j in range(i + 1, len(original_num)):
                
                original_num[i], original_num[j] = original_num[j], original_num[i]
                
                if new_num < original_num:
                    new_num = original_num.copy()
                
                original_num[i], original_num[j] = original_num[j], original_num[i]

        return int(''.join(new_num))        