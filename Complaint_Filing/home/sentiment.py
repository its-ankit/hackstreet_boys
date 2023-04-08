import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
dfs = ["I am extremely disappointed with the service I received. The product was not as advertised and customer support was unresponsive. I have wasted both time and money, and I expect a full refund to rectify this situation.", "The condition of the rented property was unacceptable. There were several maintenance issues that were not addressed, including broken appliances and pest infestation. This has caused great inconvenience and I demand immediate action to resolve these problems"]
def fun(dfs):
    sid = SentimentIntensityAnalyzer()"
    for data in dfs:
        val=0
        ss = sid.polarity_scores(data)
        print(data)
        val=ss["compound"]
        print(val)
        return val