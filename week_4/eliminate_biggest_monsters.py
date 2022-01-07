class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monster = []
        count_killed = 0
        for i in range(len(dist)):
            monster.append([dist[i],speed[i],dist[i]/speed[i]])
        monster.sort(key = lambda x : x[2])
        for value in monster:
            value[0] = value[0]-value[1]*count_killed
            if value[0] > 0:
                count_killed+=1
            else:
                break
        return count_killed