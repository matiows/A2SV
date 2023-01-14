class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if x == parent[x]:
                return x
            
            return find(parent[x])
        
        def union(x, y):
            px = find(x)
            py = find(y)
            
            px, py = min(px, py), max(px, py)
            parent[py] = px
            
        parent = {}
        answer = []
        
        for i in range(26):
            char = chr(i + 97)
            parent[char] = char
            
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
        for ch in baseStr:
            answer.append(find(ch))
            
        return ''.join(answer)
        