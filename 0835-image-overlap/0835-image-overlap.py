class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        image1 = []
        image2 = []
        
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    image1.append((i,j))
                if img2[i][j] == 1:
                    image2.append((i,j))
        
        dictionary = {}
        ans = 0
        
        for img1x, img1y in image1:
            for img2x, img2y in image2:
                check = (img2x - img1x, img2y - img1y)
                
                if check in dictionary:
                    dictionary[check] += 1
                
                else:
                    dictionary[check] = 1
                
                ans = max(ans, dictionary[check])
        
        return ans