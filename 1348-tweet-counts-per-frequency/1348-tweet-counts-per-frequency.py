class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)
    
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        period = endTime - startTime
        if freq == 'minute':
            size = period // 60
            d = 60
        
        if freq == 'hour':
            size = period // 3600
            d = 3600
        
        if freq == 'day':
            size = period // 86400
            d = 86400
            
        res = [0] * (size + 1)
            
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                i = t - startTime
                res[i // d] += 1

        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)