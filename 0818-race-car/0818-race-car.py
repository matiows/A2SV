class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        visited = set()
        visited.add((0,  1))
        moves  = 0
        
        while q:
            n = len(q)
            
            for _ in range(n):
                pos, speed = q.popleft()
                
                if pos == target:
                    return moves
                
                if (pos+speed, speed*2) not in visited:
                    visited.add((pos+speed, speed*2))
                    q.append((pos+speed, speed*2))
                
                
                if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    if (pos, speed) not in visited:
                        visited.add((pos,  speed))
                        q.append((pos,  speed))
            
            moves += 1
        
        return -1