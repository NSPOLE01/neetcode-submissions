class Twitter:

    def __init__(self):
        self.mapFollow = {}
        self.listTweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.listTweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        count = 0
        for tweet in reversed(self.listTweets):
            user = tweet[0]
            postId = tweet[1]
            if userId == user or (user in self.mapFollow and userId in self.mapFollow[user]):
                count += 1
                tweets.append(postId)
            if count == 10:
                return tweets

        return tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.mapFollow:
            self.mapFollow[followeeId] = []
        self.mapFollow[followeeId].append(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.mapFollow[followeeId].remove(followerId)
        print(self.mapFollow[followeeId])
        
