class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        temp = self.stack.pop()
        self.stack.append(temp)
        return temp

    def getMin(self) -> int:
        _min = min(self.stack)
        return _min
        