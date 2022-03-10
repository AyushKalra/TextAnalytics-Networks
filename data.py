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
random_user_ids = [180463340, 322099225, 322429759, 642942976, 893481877, 680302528, 379330167, 439322888, 507686370, 645127599, 363438343]
random_users = []

# get each user
for id in random_user_ids:
    try:
        random_users.append(api.get_user(id))
    except Exception:
        pass


print(len(random_users))

# next: loop through users, get n tweets (maybe 100 - 200), do same for followers and maybe followings if we want
# build csv/json with pandas