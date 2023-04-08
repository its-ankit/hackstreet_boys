# hackstreet_boys
platform to report frauds/scams posted on social media to the concerned authorities using automation

i) This website creates a platform to report the scams/frauds information gathered from social media platforms(Twitter) using Python.
    The Code is found in abcd.py file in home directory of the complaint filing. It uses Snscrapper library to scrap the data from twitter.

ii) We use sentiment analysis from NLP to get the degree of fraud/scam, so that the priorities would be set for the concerning problem.
      The Code is found in sentiment.py file in home directory of the complaint filing. It uses NLTK library of python to do the sentiment analysis.
      
iii) The home page, complaint page, contact page and priority page is designed using HTML and CSS and Django is used to connect it with the program.
     It takes the data as input from the program and present it dynamically on the screen.
     
iv) The contact me and complaint page takes input from the user and stores it in the database from the purpose of future use.
