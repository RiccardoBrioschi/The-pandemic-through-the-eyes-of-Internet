" Some helper functions"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from empath import Empath
lexicon = Empath()

import re


# Task 1 functions 

def create_dataframe(name_country, language, period_of_interest, time_window, prob, skip_day=1, subsample=None):
    
    """
    Function which creates dataframe retrieving tweets using Twitter API
    
    Arguments:
        name_country: name of country from which we are retrieving tweets
        language: languages spoken in analyised country
        period_of_interest: dates from which we are retrieving tweets
        time_window: list of hours from which we are retrieving tweets 
        prob: list of weights assigned to each hour in time_window
        skip_day: step used when iterating over period of interest
        subsample: index of sample of data retrieved
    """
    
    # Initialize the stemmer
    stemmer = PorterStemmer()
    lexicon = Empath()
    # Defining a list of topics based on Coronawiki Dataset
    topics = []
    # Defining support structure
    new_data = []
    output_path = './output/'+name_country
    if subsample != None:
        output_path+= subsample
    output_path+='_tweets.pkl'
    
    # Importing Twitter API keys
    with open('./Data/BearerTokens.json', 'r') as f:
        bearer_tokens = json.load(f)

    bearer_token_balsa = bearer_tokens['gojko']
    # We initialize tweepy 
    client = tweepy.Client(bearer_token=bearer_token_balsa, wait_on_rate_limit=True)
    
    for idx in range(0,len(period_of_interest[name_country]), skip_day):
        # We randomly choose the time of the day to retrieve tweets
        random_hour = np.random.choice(hours,p = weights)
        date = period_of_interest[name_country][idx]
        
        # We define start and end time to retrieve (then passed as inputs for twitter.API)
        start_time = datetime(date.year,date.month,date.day,random_hour)
        end_time = datetime(date.year,date.month,date.day,random_hour+3)
        
        # We define a proper query to get tweets from the country we're interested in
        query = " place_country:{} lang:{} -is:retweet -has:links -has:media -has:images \
                                    -has:video_link -has:mentions".format(name_country,language)
        
        while True:
            tweets = client.search_all_tweets( query, max_results = 30, 
                                         start_time = start_time, end_time = end_time,
                                              tweet_fields  = ['text','context_annotations','id'])
            if tweets.data != None:
                break
            random_hour = np.random.choice(hours,p = weights)
            date = period_of_interest[name_country][idx]
            start_time = datetime(date.year,date.month,date.day,random_hour)
            end_time = datetime(date.year,date.month,date.day,random_hour+3)
        
        # We perform basic preprocessing operations on the text (translation and removal of punctuations)
        for tweet in tweets.data:
            if language != 'en':
                text = ts.google(tweet.text)
            else:
                text = tweet.text
            # We remove punctuation
            text = ("".join([ch for ch in text if ch not in string.punctuation])).lower()
            # We remove numbers
            text = re.sub("\d+", "",text).strip()
            # We compute sentiment analysis on the given text
            text_sentiment = TextBlob(text).sentiment
            text_polarity, text_subjectivity = text_sentiment.polarity, text_sentiment.subjectivity
            # We tokenize the tweet to make the work easier
            tokenized_stemmed_version = nltk.word_tokenize(text)
            tokenized_stemmed_version = [stemmer.stem(word) for word in tokenized_stemmed_version]
            # Saving new datapoint in new_data list
            if len(text) > 0:
                new_data.append([date,tweet.id, language,text,tokenized_stemmed_version,
                                 tweet.context_annotations,text_polarity,text_subjectivity])
            
        # We create the dataframe
        df = pd.DataFrame(new_data, columns = ['date','id','language','tweet','tokenized_tweet_list',
                                               'context_from_Twitter','polarity','subjectivity'])
        df.to_pickle(output_path)
        
        
def get_dataframe(name_country):
    """
    Function which reads dataframe from pickle format
    
    Arguments:
        name_country: name of country from which we are retrieving tweets
    Returns:
        df: dataframe object
    """
        
    get_path = './output/'+name_country+'_tweets.pkl'
    return pd.read_pickle(get_path)
    
# Task 2 functions

def remove_emojis(data):
    """
    Function which removing emojis from tweet's text
    
    Arguments:
        data : tweet text
    
    Returns:
        text: text without emojis
    """
    
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)
    

def update_influental_people_dataframe(client, country_code, lang, users, dates, influential_people_tweets):
    """
    Function which retrieving new tweets using Twitter API
    
    Arguments:
        client : Twitter API v2 Client
        country_code: country from which we are retrieving tweets
        lang: languge of tweets we are retrieving
        users: list of users which tweets we want to retrieve
        dates: list of dates for which we want to retrieve tweets
        influential_people_tweets: dataframe which will contain new tweets
    
    Returns:
        influential_people_tweets: dataframe containing tweets which 
        satisfying conditions sent as parameters of function
    """
        
    start_time = dates[country_code][0]
    end_time = dates[country_code][-1] 
    
    influential_people_tweets = pd.read_csv('influential_people_tweets.csv', delimiter=',')
    
    for user in users:
        # We define a proper query to get tweets from the country we're interested in
        query = "from:{} -is:retweet".format(user.data.id)
                
        tweets = client.search_all_tweets(query, max_results=100, 
                                      start_time=start_time, end_time=end_time,
                                      tweet_fields=['id','text','context_annotations','created_at'])
        
        if(tweets.data == None): continue
        
        for tweet in tweets.data: 
            tweet_en = tweet.text
            
            #translating tweet to english
            if lang != 'en':
                try:
                    tweet_en = ts.google(tweet.text)
                except:
                    tweet_en = None
                    
            if tweet_en != None:
                # removing punctuation
                tweet_en = ("".join([ch for ch in tweet_en if ch not in '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~'])).lower()
                tweet_en.strip()
                # removing numbers
                tweet_en = re.sub("\d+", "", tweet_en).strip()
                
                # merging hashtag sign with next word 
                if('# ' in tweet_en):
                    tweet_en.replace('# ', '#')

                # removing emojis
                tweet_en = remove_emojis(tweet_en)

                # removing username tags and http links
                if('http' in tweet_en) or ('@' in tweet_en):
                    tweet_en = " ".join(filter(lambda word: (not word.startswith('http')) and (not word.startswith('@')),
                                               tweet_en.split()))

            new_tweet = pd.DataFrame([{'id': tweet.id, 'country_code': country_code, 'lang': lang, 'user': user,
                                       'tweet_text_orginal': tweet.text, 'tweet_text_en': tweet_en, 
                                       'tweet_date': tweet.created_at,
                                       'context_annotations': tweet.context_annotations }])
            
            influential_people_tweets = pd.concat([influential_people_tweets, new_tweet], axis=0, ignore_index=True)
        
    
    return influential_people_tweets



def getTweets(country, lang, users, periods):
    # retrieving tweets (delete the dot from line below to execute)
    influential_people_tweets = pd.read_csv('./output/influential_people_tweets.csv', delimiter=',')
    influential_people_tweets_update = pd.DataFrame(columns=['id','country_code', 
                                                             'lang', 'user',
                                                             'tweet_text_orginal', 'tweet_text_en', 
                                                             'tweet_date', 'context_annotations'])

    influential_people_tweets_update = update_influental_people_dataframe(client, country, lang, 
                                                                          users,  periods, 
                                                                          influential_people_tweets_update)

    # concat new tweets with pervious one
    influential_people_tweets = pd.concat([influential_people_tweets, influential_people_tweets_update], ignore_index=True)
    influential_people_tweets.to_csv('influential_people_tweets.csv')
    
    
