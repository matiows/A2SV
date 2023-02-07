class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
    
        for i in instructions:
            if i == 'G':
                x += dx
                y += dy

            elif i == 'L':
                dx, dy = -dy, dx

            elif i == 'R':
                dx, dy = dy, -dx

        if (x, y) == (0, 0) or (dx, dy) != (0, 1):
            return True

        return False