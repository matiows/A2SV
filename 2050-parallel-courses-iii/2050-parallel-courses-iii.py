class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        maximum = [0] * (n+1)
        graph = defaultdict(list)
        incoming = [0] * (n+1)
        queue = deque()
        answer = inf
        
        for src, dst in relations:
            graph[src].append(dst)
            incoming[dst] += 1
            
        for course, degree in enumerate(incoming[1:]):
            if degree == 0:
                queue.append(course + 1)
        
        while queue:
            check = 0
            for _ in range(len(queue)):
                course = queue.popleft()
                maximum[course] += time[course - 1]
                for sub in graph[course]:
                    maximum[sub] = max(maximum[sub], maximum[course])
                    incoming[sub] -= 1
                    if incoming[sub] == 0:
                        queue.append(sub)
            
        return max(maximum)
     