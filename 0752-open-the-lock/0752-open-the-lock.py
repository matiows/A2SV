class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set(deadends)
        start = '0000'
        if start in visited:
            return -1
        
        queue = collections.deque([start])

        visited.add(start)
        counter = 0
        
        while queue:
            N = len(queue)
            for _ in range(N):
                curr = queue.popleft()

                if curr == target:
                    return counter

                for i in range(4):
                    add = curr[:i] + str((int(curr[i]) - 1) %10) + curr[i+1:]
                    sub = curr[:i] + str((int(curr[i]) + 1) %10) + curr[i+1:]

                    if add not in visited:
                        queue.append(add)
                        visited.add(add)
                    if sub not in visited:
                        queue.append(sub)
                        visited.add(sub)
            counter += 1

        return -1    