class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0]*len(quiet)
        check = {}
        
        for rich, poor in richer:
            graph[rich].append(poor)
            incoming[poor] += 1
            
        queue = deque()
        for idx, degree in enumerate(incoming):
            check[idx] = (quiet[idx], idx)
            if degree == 0:
                queue.append(idx)
        
        while queue:
            person = queue.popleft()
            
            for people in graph[person]:
                if check[person][0] < check[people][0]:
                    check[people] = check[person]
                incoming[people] -= 1
                if incoming[people] == 0:
                    queue.append(people)
            
        for key, val in check.items():
            incoming[key] = val[1]
            
        return incoming
            