def fun(query):   
    import snscrape.modules.twitter as sntwitter
    import pandas as pd
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from string import punctuation
    punctuation = list(punctuation)
    nltk.download('stopwords')
    stopwords = stopwords.words('english')
    

    limit=100
    tweets=[]
    users=[]
    user_content=[]

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        # print(vars(tweet))
        # break
        if len(tweets)==limit:
            break
        else:
            tweets.append([tweet.user.username,tweet.content])
    for i in tweets:
        users.append(i[0])
        user_content.append(i[1])
    
    
    for i in range(len(tweets)):
        list_of_words=word_tokenize(user_content[i])

        l1=[]
        for i in range(len(list_of_words)):
            if list_of_words[i].lower() in stopwords or list_of_words[i] in "!@#$%^&*()_+-=][\|';:/?.,><`~":
                l1.append(i)

        x=0
        i=0
        for i in range(len(list_of_words)):
            if i not in l1:
                list_of_words[x] = list_of_words[i]
                x += 1
            i += 1
        while (len(list_of_words) > x):
            list_of_words.pop(x)
        
        return tweets

query="scam fraud misleading online"
print(fun(query))
# for i in dict:
#     print(i,dict[i])


