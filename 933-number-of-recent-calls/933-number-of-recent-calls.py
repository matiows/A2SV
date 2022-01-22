class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        while self.queue and ( t - self.queue[0] > 3000):
            self.queue = self.queue[1:]
        self.queue.append(t)
        return len(self.queue)