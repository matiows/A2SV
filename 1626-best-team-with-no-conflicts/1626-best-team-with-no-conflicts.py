class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        team = list(zip(ages,scores))
        team.sort()
        n = len(ages)
        dp = [0]*n

        for i in range(n):
            curr = team[i][1]
            dp[i] = curr

            for j in range(i):
                if team[j][1] <= curr:
                    dp[i] = max(dp[i], dp[j]+curr)
            
        return max(dp)
