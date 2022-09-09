#Isabella Souza Freitas

import numpy as np

#array definida

tweets = np.array(["Wow, what a great day today!! #sunshine",
"I feel sad about the things going on around us. #covid19",
"I'm really excited to learn Python with @JovianML #zerotopandas",
"This is a really nice song. #linkinpark",
"The python programming language is useful for data science",
"Why do bad things happen to me?",
"Apple announces the release of the new iPhone 12. Fans are excited.",
"Spent my day with family!! #happy",
"Check out my blog post on common string operations in Python. #zerotopandas",
'Freecodecamp has great coding tutorials. #skillup'])

#output do nuemro de tweets existentes

print( "foram analizados ",len(tweets), "tweets")

#analise dos tweets felizes ou triste

happy_tweets = np.empty(10)
sad_tweets = np.empty(10)
hword = (['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best'])
sword = (['sad', 'bad', 'tragic', 'unhappy', 'worst'])
cont1 = 0 
for phrase in tweets:
    for word in  hword:
        if word in phrase:
            np.append(happy_tweets,phrase)
            cont1 +=1 
cont2 = 0      
for phrase in tweets:
    for word in sword:
        if word in phrase:
             np.append(sad_tweets,phrase)
             cont2 +=1

#numero de tweets felizes
print(cont1)

#numero de tweets 
print(cont2)



        


        
