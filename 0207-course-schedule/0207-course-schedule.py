class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        coloring = [0] * numCourses
        courses = []
        
        for des, src in prerequisites:
            graph[src].append(des)
            
            
        def topDown(course):
            if coloring[course] == 1:
                return False
            
            if coloring[course] == 2:
                return True
            
            coloring[course] = 1
            answer = True
            for child in graph[course]:
                if child in graph:
                    answer = answer and topDown(child)
                
            coloring[course] = 2
            courses.append(course)
            return answer
        
        answer = True
        for course in graph:
            answer = answer and topDown(course)
            
        return answer