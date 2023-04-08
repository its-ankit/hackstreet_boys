import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text="Political analysis: By analyzing tweets from politicians, parties, or other public figures, you can gain insights into their positions and policies. This information can be used by journalists, activists, or researchers to study political trends or inform public opinion. Social media marketing: By accessing Twitter's APIs, you can create targeted advertising campaigns that reach specific demographics or interests. This can be useful for businesses that want to promote their products or services to a specific audience. In summary, a Twitter developer account can provide access to a wealth of data and services that can be used for a wide range of use cases. By leveraging these resources in a Hackathon, you can create innovative solutions that can have a positive impact on various industries and communities."
Ltext=text.lower()
cleaned_text=Ltext.translate(str.maketrans('','', string.punctuation))
token_words=word_tokenize(cleaned_text,"english")
final_words=[]
for word in token_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

def Sentiment_analyse(final_words):
    score=SentimentIntensityAnalyzer().polarity_scores(final_words)
    print(score)

Sentiment_analyse(final_words)

