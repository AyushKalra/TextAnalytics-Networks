import tweepy
import json
import random

# Twitter Credentials
consumer_key = 'riiUgzG0nHSkUGt5c521LgcnD'
consumer_key_secret = 'XkNvxIyc83Y2t1TS3TzELFmDR9ek5pHrpPUpU3W1K9oGuGBNGP'
access_token = '710798343623073792-tNUupkHcBd4WhfqaeKfDA9vhW19lAEC'
access_token_secret = '2mgo5ZEyVOTCGnYqbRzWYRSHBfmCIfZ8rvt5MNFbwrY6O'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABNDKgEAAAAAx7i7gCsEItSD4glnaw%2BCfuFh0Ok%3DIDQvFJ02SZ5G64z1Lzd4PwhROA8pHBij7MnWCPDK3kBGW82oaJ'

#  Tweepy Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def append_to_dataset(new_user):
    """
    Appends the new user JSON object to the dataset.
    """                
    with open('dataset1.json', 'r+') as f:
        file_data = json.load(f)
        file_data['dataset1'].append(new_user)
        f.seek(0)
        json.dump(file_data, f, indent=4)

def get_user_ids(users):
    """
    Gets a list of all user ids currently in dataset
    """    
    return [u['user'] for u in users]

def get_followers(user, n):
    """
    Gets the top n followers of user.
    """
    return [f.id for f in api.followers(id=user)[:n]]

def get_followings(user, n):
    """
    Gets the top n followings of user.
    """
    return [f.id for f in api.friends(id=user)[:n]]

def is_in_dataset(user):
    """
    Checks to see if the user already exists in the dataset.
    """
    file = open('dataset1.json')
    users = json.load(file)['dataset1']

    in_dataset = get_user_ids(users)

    return user in in_dataset


def get_initial_user_list():
    """
    Obtains a list of random tweets using Tweepy given a query string.
    Gets the users from each of these tweets.
    Generates corpus, followers list, followings list for each users.
    Creates JSON object of user as entry for dataset.
    Sends JSON to appending function
    """
    random_users = []

    complete_data = []

    # search for tweets by query
    search_tweets = tweepy.Cursor(api.search, q='App Development', lang='en').items(80)

    # get users from these tweets
    for tweet in search_tweets:
        try:
            if not is_in_dataset(tweet.user.id):
                tweets = api.user_timeline(id=tweet.user.id, count=61, include_rts=False)
                
                # if user has enough tweets
                if len(tweets) >= 60:
                    random_users.append(tweet.user)

                    if len(random_users) > 2: 
                        break       

                    user = tweet.user
                    
                    # concatenate all tweets
                    corpus = " "
                    for t in tweets:
                        corpus += t.text + " "

                    # get follower ids
                    followers = get_followers(user.id, 10)
                    
                    # get followings ids
                    followings = get_followings(user.id, 10)
                
                    # create json object
                    data = {"user": user.id, "corpus": corpus, "followers": followers, "followings": followings}
                    complete_data.append(data)
                    
                    print("Number of users collected: ", len(complete_data))

        except Exception as e:
            print(str(e))

        # append to dataset
        for u in complete_data:
            append_to_dataset(u)


def add_followers_to_dataset1():
    """
    Gets list of current users in dataset1, iterates through followers, appends them to dataset
    """
    file = open('dataset1.json')
    users = json.load(file)['dataset1']

    # get current users in dataset1
    in_dataset = get_user_ids(users)
    
    for user in users:
        followers = user['followers']
        for f in followers:
            # if follower not in dataset1
            if f not in in_dataset:
                try:
                    tweets = api.user_timeline(id=f, count=60, include_rts=False)

                    # generate corpus
                    corpus = ""
                    for t in tweets:
                        corpus += t.text + " "
                    
                    # get followers
                    next_followers = get_followers(f, 5)

                    # get followings
                    followings = get_followings(f, 5)

                    # create user json object
                    new_data = {"user": f, "corpus": corpus, "followers": next_followers, "followings": followings}
                    append_to_dataset(new_data)

                except Exception as e:
                    print(str(e))


def add_followings_to_dataset1():
    """
    Gets list of current users in dataset1, iterates through followers, appends them to dataset
    """
    file = open('dataset1.json')
    users = json.load(file)['dataset1']

    # get current users in dataset1
    in_dataset = get_user_ids(users)
    
    for user in users:
        followings = user['followings']
        for f in followings:
            # if following not in dataset1
            if f not in in_dataset:
                try:
                    tweets = api.user_timeline(id=f, count=60, include_rts=False)

                    # generate corpus
                    corpus = ""
                    for t in tweets:
                        corpus += t.text + " "

                    # get followers
                    next_followers = get_followers(f, 5)

                    # get followings
                    next_followings = get_followings(f, 5)

                    # create user json object
                    new_data = {"user": f, "corpus": corpus, "followers": next_followers, "followings": next_followings}
                    append_to_dataset(new_data)

                except Exception as e:
                    print(str(e))


def add_some_random_users():
    """
    Generates list of random indices.
    Iterates through list, adds followers/followings to dataset1
    """
    file = open('dataset1.json')
    users = json.load(file)['dataset1']

    # get current users in dataset1
    in_dataset = get_user_ids(users)

    # get indices
    indices = random.sample(range(100, len(users)), 10)

    for i in indices:
        user = users[i]
        followers = user['followers']
        # if not in dataset1
        for f in followers:
            if f not in in_dataset:
                try:
                    tweets = api.user_timeline(id=f, count=60, include_rts=False)
                    
                    # generate corpus
                    corpus = ""
                    for t in tweets:
                        corpus += t.text + " "

                    # get followers
                    next_followers = get_followers(f, 8)

                    # get followings
                    next_followings = get_followings(f, 8)

                    # create user json object
                    new_data = {"user": f, "corpus": corpus, "followers": next_followers, "followings": next_followings}
                    append_to_dataset(new_data)

                except Exception as e:
                    print(str(e))


if __name__ == "__main__":
    """
    Code used for creating two datasets:
        dataset1.json --> Linked users
        dataset2.json --> unlinked users
    
    Replace name of dataset with the one you would like to add to in functions:
        is_in_dataset()
        add_followers_to_dataset1()
        add_followings_to_dataset1()
        add_some_random_users()
    
    Uncomment functions below that you would like to run
    """
    get_initial_user_list()
    #add_followers_to_dataset1()
    #add_followings_to_dataset1()
    #add_some_random_users()
        


