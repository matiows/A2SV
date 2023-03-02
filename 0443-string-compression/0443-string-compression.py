class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        w = 0
        c = 0
        
        for r in range(len(chars)+1):
            if r != len(chars) and chars[l] == chars[r]:
                c += 1
                
            else:
                
                chars[w] = chars[l]
                w += 1
                if c > 1:
                    t = list(map(str, str(c)))
                    chars[w:w+len(t)] = t
                    w += len(t)
                
                l = r
                c = 1
        
        p = len(chars) - w
        
        while p:
            chars.pop()
            p -= 1