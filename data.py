from itertools import count
import tweepy
import pandas as pd

# Twitter Credentials
consumer_key = 'riiUgzG0nHSkUGt5c521LgcnD'
consumer_key_secret = 'XkNvxIyc83Y2t1TS3TzELFmDR9ek5pHrpPUpU3W1K9oGuGBNGP'
access_token = '710798343623073792-tNUupkHcBd4WhfqaeKfDA9vhW19lAEC'
access_token_secret = '2mgo5ZEyVOTCGnYqbRzWYRSHBfmCIfZ8rvt5MNFbwrY6O'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABNDKgEAAAAAx7i7gCsEItSD4glnaw%2BCfuFh0Ok%3DIDQvFJ02SZ5G64z1Lzd4PwhROA8pHBij7MnWCPDK3kBGW82oaJ'

#  Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweetsPerQuery = 100
maxTweets = 1000

# random ints that should match with a user id, if not a match then skip
random_user_ids = [712023, 322099225, 227712905, 976796490, 765391580, 326676622, 705868308, 479987005, 848103961, 421817116]
random_users = []

# get each user
for id in random_user_ids:
    try:
        random_users.append(api.get_user(id))
        latest_tweet = api.user_timeline(id=api.get_user(id).id, count=220)

        # users must tweet in english and users must have ~ 100 - 200 tweets
        if len(latest_tweet) == 0 or len(latest_tweet) < 100 or latest_tweet[0].lang != "en":
            random_users = random_users[:-1]
            raise Exception


    except Exception:
        print("Invalid Id:", id)


print("Valid users:", len(random_users))

# next: loop through users, get n tweets (maybe 100 - 200), do same for followers and maybe followings if we want
for user in random_users:
    #print("user:", user.id, user.name)
    
    tweets = api.user_timeline(id=user.id, count=200)
    
    #print(tweets[2].text)


# build csv/json with pandas