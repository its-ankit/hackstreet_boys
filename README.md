# hackstreet_boys
platform to report frauds/scams posted on social media to the concerned authorities using automation


> Problem Statement:

With the rising use of the internet, more and more people are using social media nowadays. People post various kinds of things related to their day-to-day activities. One major type of post that is seen frequently on social media is posts related to complaints about the products and services used by people. It is very confusing and difficult for people to register their complaints on specific portals so they find it easier to share their problems on social media. Some of the problems that people face for registering their complaints are as follows-
Different types of complaints have to be filed on different government websites which is difficult for the user to find.

Even after finding the correct website, it is difficult and tiring for people to fill out the long and complex forms.

In many cases, people land on fraudulent websites and end up getting scammed and lose their money or important data and credentials.

To solve this problem we are creating an automated platform that will take the data from the complaining posts from different social media and ask the respective user for permission to post it on the respective government websites. The platform also includes a web application that will show the complaints of the different users.



Solution:

The main objective of this automated platform is to collect the posts related to some kind of complaint from different social media platforms through web scraping only after taking permission from the user, then this data is used to file a complaint to the specific government/ e-commerce portals. A web application is also created which stores all the different complaints of the users.

Collecting the data of scams/frauds from social media - For this, we will use a web-scraping technique and an automation tool. Firstly, we login into a platform (say Facebook) and track the posts using an automation tool (Selenium in python). Secondly, we collect data through different posts (50 posts at a time) using the web-scraping technique (using the auto-scraper library of python).

Processing the data and finding the posts expressing scams/frauds faced by the consumer- For this, we use the Sentiment Analysis of Natural Language Processing Concept(of Machine Learning) to find the negative experiences of scams/frauds faced by them. 

Figuring out the necessary details of the consumers from the posts to contact them- Using the web-scraping techniques and the HTML format of different pages (social media pages) we try finding the name and contact information of the consumer. In addition to that, we connect with them on the same social media platform or contact them via mail (if available on their profile). 

Processing the data in a proper format of the complaint to be reported - After collecting the data, we format it into a JSON format having information (such as name, goods/service purchased, date of purchase, issue/problem, evidence, etc) using python programming. 

Identifying the respective platform where the scam/issue has to be reported- For this we will keep some pre-processed data. We will keep a dictionary of key-value pairs. Example- 
Consumer Forum : [ “a deficiency of services”,” unfair trade practices”, “manufacturing defects in the product”,  “medical negligence”]
Cyber Crime: National Cyber Crime Reporting Portal
We will use the Classification Algorithm of Machine Learning to classify the processed consumer issue into any of the categories matching the government schemes/ concerned authorities available on our platform.

Taking approval from the consumer whether he/she wants his complaint to be reported or not - After processing the information into a proper format, we will present it to the consumer using an automated email generator or via texting them on the platform where they posted their instance. (This step can be automated as well).

Filing the complaint to the concerned platform/service available- After getting the approval from the consumer, we will use the information collected from step 5 and file the issue on behalf of the consumer with the automation tool Selenium. This will help the consumer receive notifications from the platform where the complaint has been filed.

Inform the consumer/person about the filing and provide the details to track the interaction.





Working:-

i) This website creates a platform to report the scams/frauds information gathered from social media platforms(Twitter) using Python.
    The Code is found in abcd.py file in home directory of the complaint filing. It uses Snscrapper library to scrap the data from twitter.

ii) We use sentiment analysis from NLP to get the degree of fraud/scam, so that the priorities would be set for the concerning problem.
      The Code is found in sentiment.py file in home directory of the complaint filing. It uses NLTK library of python to do the sentiment analysis.
      
iii) The home page, complaint page, contact page and priority page is designed using HTML and CSS and Django is used to connect it with the program.
     It takes the data as input from the program and present it dynamically on the screen.
     
iv) The contact me and complaint page takes input from the user and stores it in the database from the purpose of future use.



