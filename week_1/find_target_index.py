class Solution:
    def targetIndices(self, a: List[int], target: int) -> List[int]:
        target_index = []
        for i in range(len(a)):
            for j in range((len(a))-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
        for i in range(len(a)):
            if a[i] == target:
                target_index.append(i)
        return target_index