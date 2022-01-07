class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls,cows = 0,0
        temp_secret,temp_guess = "",""
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                temp_secret+= secret[i]
                temp_guess+= guess[i]
        temp_guess = Counter(temp_guess)
        for x in temp_secret:
            if temp_guess[x] > 0:    
                cows+=1
                temp_guess[x]-=1
        result=str(bulls)+'A'+str(cows)+'B'
        return result