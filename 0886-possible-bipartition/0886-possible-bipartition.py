class Solution:
    def possibleBipartition(self, n: int, dis: List[List[int]]) -> bool:
        
        G = defaultdict(set)
        for i,j in dis : G[i].add(j), G[j].add(i)
        
        seen = dict()

        for k in range(1,n+1):
            if k not in seen:
                Q = deque([(k,True)])
                while Q:
                    i, g = Q.popleft()
                    seen[i] = g
                    for j in G[i]:
                        if j in seen:
                            if seen[j] == g : return False
                        else:
                            seen[j] = not g
                            Q.append((j, not g))
        
        return True