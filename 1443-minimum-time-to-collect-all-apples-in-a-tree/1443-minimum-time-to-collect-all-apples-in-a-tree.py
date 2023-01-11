class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        tree = defaultdict(set)
        
        for e1, e2 in edges:
            tree[e1].add(e2)
            tree[e2].add(e1)
        
        def collectApple(node):
            if len(tree[node]) == 0:
                return int(hasApple[node]) * 2
            
            value = 0
            for child in tree[node]:
                tree[child].remove(node)
                value += collectApple(child)
              
            if (value > 0 or hasApple[node]) and node != 0:
                value += 2
            
            return value
                
        return collectApple(0)