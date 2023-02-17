class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        
        for des, src in prerequisites:
            graph[src].append(des)
            incoming[des] += 1
            
        queue = deque()
        answer = []

        for idx, degree in enumerate(incoming):
            if degree == 0:
                queue.append(idx)
                
        while queue:
            course = queue.popleft()
            answer.append(course)
            
            for child in graph[course]:
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    queue.append(child)
                    
        return len(answer) == numCourses       