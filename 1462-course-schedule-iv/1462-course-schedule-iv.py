class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        courses = defaultdict(set)
        answer = []
        
        for k in range(len(prerequisites)):
            i, j = prerequisites[k]
            graph[i].append(j)
            
        memo = {}
        def dfs(node):
            if node in memo:
                return memo[node]
            
            _set = set()
            _set.add(node)
            if node not in graph:
                return _set

            for course in graph[node]:
                _set |= dfs(course)
            
            memo[node] = _set
            return memo[node]
                
        for i in graph:
            for j in graph[i]:
                courses[i] |= dfs(j)
                
        for i, j in queries:
            answer.append(j in courses[i])
        return answer
            
        