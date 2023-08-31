from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].appendleft((self.time, tweetId))

    def getNewsFeed(self, userId):
        news_feed = []
        followees = self.users[userId] | {userId}
        for user in followees:
            news_feed.extend(self.tweets[user])
        news_feed.sort(reverse=True)
        return [tweetId for time, tweetId in news_feed[:10]]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId != followeeId:
            self.users[followerId].discard(followeeId)

# Example usage
commands = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
arguments = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

result = []
twitter = None

for i in range(len(commands)):
    command = commands[i]
    argument = arguments[i]

    if command == "Twitter":
        twitter = Twitter()
        result.append(None)
    elif command == "postTweet":
        twitter.postTweet(*argument)
        result.append(None)
    elif command == "getNewsFeed":
        result.append(twitter.getNewsFeed(*argument))
    elif command == "follow":
        twitter.follow(*argument)
        result.append(None)
    elif command == "unfollow":
        twitter.unfollow(*argument)
        result.append(None)

print(result)  # Output should match the expected output
