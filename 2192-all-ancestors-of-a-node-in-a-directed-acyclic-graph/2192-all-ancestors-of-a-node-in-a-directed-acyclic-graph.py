class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestor = defaultdict(set)
        incoming = [0] * n
        graph = defaultdict(list)
        queue = deque()
        result = []
        
        for src, dst in edges:
            graph[src].append(dst)
            incoming[dst] += 1
            
        for node, degree in enumerate(incoming):
            if degree == 0:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            
            for child in graph[node]:
                ancestor[child].add(node)
                ancestor[child] |= ancestor[node]
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    queue.append(child)
                
        
        for node in range(n):
            ancestors = list(ancestor[node])
            ancestors.sort()
            result.append(ancestors)
            
        return result