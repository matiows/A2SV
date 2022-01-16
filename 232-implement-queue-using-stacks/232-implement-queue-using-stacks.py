class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:     
        self.stack1.append(x)
    def pop(self) -> int:
        value = 0
        for i in range(len(self.stack1)):
            value = self.stack1.pop()
            self.stack2.append(value)
        self.stack2.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return value
    def peek(self) -> int:
        value = 0
        for i in range(len(self.stack1)):
            value = self.stack1.pop()
            self.stack2.append(value)
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return value
    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False