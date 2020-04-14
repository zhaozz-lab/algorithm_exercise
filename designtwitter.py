class User(object):
    def __init__(self,userId):
        self.userId = userId
        self.tweets = set()
        self.following = set()

class Tweet(object):
    """docstring for Tweet"""
    def __init__(self, tweetId,userId,ts):
        self.tweetId = tweetId
        self.userId = userId
        self.ts = ts
    def __cmp__(self,other):
        return cmp(other.ts,self.ts)


class Twitter(object):
    """docstring for Twitter"""
    def __init__(self):
        self.ts = 0
        self.userMap = dict()
    
    def postTweet(self,userId,tweetId):
        if userId not in self.userMap:
            self.userMap[userId] = User(userId)
        tweet = Tweet(tweetId,userId,self.ts)
        self.userMap[userId].tweets.add(tweet)
        self.ts += 1

    def getNewsFeed(self,userId):
        res = list()
        que = []
        if userId not in self.userMap:
            return res
        mainUser = self.userMap[userId]

        for t in mainUser.tweets:
            heapq.heappush(que,t)

        for u in mainUser.following:
            for t in u.tweets:
                heapq.heappush(que,t) 
        n = 0
        while que and n < 10:
            res.append(heapq.heappop(que).tweetId)
            n += 1
        return res

        def follow(self,followerId,followerId):
            if followeeId not in self.userMap:
                self.userMap[followeeId] = User(followerId)
            if followerId not in self.userMap:
                self.userMap[followerId] = User(followerId)
            if followerId == followeeId:
                return

            followee = self.userMap[followeeId]
            self.userMap[followerId].following.add(followee)

        def unfollow(self,followerId,followeeId):
            if followerId == followeeId or followerId not in self.userMap or followeeId not in self.userMap:
                return
            followee = self.userMap 
            
        
        