from regex import E
import tweepy
import json
import random

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


def append_to_dataset(new_user):                
    with open('dataset2.json', 'r+') as f:
        file_data = json.load(f)
        file_data['dataset2'].append(new_user)
        f.seek(0)
        json.dump(file_data, f, indent=4)


def get_followers(user):
    followers = []
    for f in api.followers(id=user)[:5]:
        followers.append(f.id)
    
    return followers

def get_followings(user):
    followings = []
    for f in api.friends(id=user)[:5]:
        followings.append(f.id)

    return followings 

def is_in_dataset(user):
    file = open('dataset2.json')
    users = json.load(file)['dataset2']

    in_dataset = get_user_ids(users)

    return user in in_dataset

# Python Flask, golang, category theory, dynamic programming, Machine Learning, numpy, IntelliJ, jupiter notebook
# Node.js, Javascript, Jquery, web development, software engineer, app development, python django

def get_initial_user_list():
    random_users = []

    complete_data = []

    # search for tweets by keyword, then get users
    search_tweets = tweepy.Cursor(api.search, q='App Development', lang='en').items(80)

    # get users from these tweets
    for tweet in search_tweets:
        try:
            if not is_in_dataset(tweet.user.id):
                tweets = api.user_timeline(id=tweet.user.id, count=61, include_rts=False)
                
                if len(tweets) >= 60:
                    random_users.append(tweet.user)

                    if len(random_users) > 50: 
                        break        
                    user = tweet.user
                    
                    # concatenate all tweets
                    corpus = " "
                    for t in tweets:
                        corpus += t.text + " "

                    # get follower ids
                    followers = get_followers(user.id)
                    
                    # get friend ids
                    followings = get_followings(user.id)
                
                    # create obj for json
                    data = {"user": user.id, "corpus": corpus, "followers": followers, "followings": followings}
                    complete_data.append(data)
                    print(len(complete_data))

        except Exception as e:
            print(E)

            for u in complete_data:
                append_to_dataset(u)
    
    # write to json file
    #json_file = open("dataset2.json", "a")
    #json_file.write(json.dumps(complete_data, indent=4))
    #json_file.close()


def get_user_ids(users):
    id_in_dataset = []

    for user in users:
        id_in_dataset.append(user['user'])
    
    return id_in_dataset
    

def add_followers_to_dataset():
    file = open('data.json')
    users = json.load(file)['dataset']

    in_dataset = get_user_ids(users)
    
    for user in users:
        followers = user['followers']
        for f in followers:
            if f not in in_dataset:
                try:
                    print(f)
                    tweets = api.user_timeline(id=f, count=60, include_rts=False)
                    corpus = ""
                    for t in tweets:
                        corpus += t.text + " "

                    next_followers = get_followers(f)

                    followings = get_followings(f)

                    new_data = {"user": f, "corpus": corpus, "followers": next_followers, "followings": followings}
                    
                    append_to_dataset(new_data)

                except Exception as e:
                    print(str(e))


def add_followings_to_dataset():
    file = open('data.json')
    users = json.load(file)['dataset']

    in_dataset = get_user_ids(users)
    
    for user in users:
        followings = user['followings']
        for f in followings:
            if f not in in_dataset:
                try:
                    print(f)
                    tweets = api.user_timeline(id=f, count=60, include_rts=False)
                    corpus = ""
                    for t in tweets:
                        corpus += t.text + " "

                    next_followers = get_followers(f)

                    next_followings = get_followings(f)

                    new_data = {"user": f, "corpus": corpus, "followers": next_followers, "followings": next_followings}
                    
                    append_to_dataset(new_data)

                except Exception as e:
                    print(str(e))


def add_some_random():
    file = open('data.json')
    users = json.load(file)['dataset']

    in_dataset = get_user_ids(users)

    indices = random.sample(range(100, len(users)), 10)
    print(indices)

    for i in indices:
        user = users[i]
        followers = user['followers']
        for f in followers:
            if f not in in_dataset:
                try:
                    print(f)
                    tweets = api.user_timeline(id=f, count=60, include_rts=False)
                    corpus = ""
                    for t in tweets:
                        corpus += t.text + " "

                    next_followers = get_followers(f)

                    next_followings = get_followings(f)

                    new_data = {"user": f, "corpus": corpus, "followers": next_followers, "followings": next_followings}
                    
                    append_to_dataset(new_data)

                except Exception as e:
                    print(str(e))


if __name__ == "__main__":
    get_initial_user_list()
    #add_followers_to_dataset()
    #add_followings_to_dataset()
    #add_some_random()
        


