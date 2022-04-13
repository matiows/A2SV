class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0] * numCourses
        outgoing = defaultdict(set)
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            inDegrees[course] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)
        course = []
        while queue:
            course.append(queue.popleft())
            for neighbor in outgoing[course[-1]]:
                inDegrees[neighbor]-=1
                if inDegrees[neighbor]==0:
                    queue.append(neighbor)
        if len(course) == numCourses:
            return course
        else:
            return []
