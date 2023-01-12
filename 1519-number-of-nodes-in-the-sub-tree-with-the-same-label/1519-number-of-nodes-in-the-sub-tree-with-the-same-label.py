class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [1] * n
        graph = defaultdict(set)
        
        for source, destination in edges:
            graph [source].add(destination)
            graph [destination].add(source)
        
        def findLabel(node):
            if len(graph[node]) == 0:
                return {labels[node]: 1}
            
            result = defaultdict(int)
            
            for child in graph[node]:
                graph[child].remove(node)
                
                letter = findLabel(child)
                
                for key, value in letter.items():
                    result[key] += value
            result[labels[node]] += 1
            answer[node] = result[labels[node]]
            
            return result
                    
        findLabel(0)
        return answer
            