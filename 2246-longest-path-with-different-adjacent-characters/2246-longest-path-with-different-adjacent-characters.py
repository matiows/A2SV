class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(set)
        
        for idx, value in enumerate(parent):
            if idx == 0:
                continue
                
            graph[idx].add(value)
            graph[value].add(idx)
        
        answer = [1]
        
        def findPath(node):
            if len(graph[node]) == 0:
                return [s[node]]
            
            longest = [[], 0]
            longer = [[],0]
            
            for child in graph[node]:
                graph[child].remove(node)
                
                path = findPath(child)
                
                if path[-1] != s[node]:
                    if len(path) >= longest[1]:
                        longer = longest
                        longest = [path, len(path)]
                        
                    elif len(path) > longer[1]:
                        longer = [path, len(path)]
            
            answer[0] = max(answer[0], longest[1] + longer[1] + 1)
            
            longest[0].append(s[node])
            
            return longest[0]
            
        findPath(0)
        return answer[0]