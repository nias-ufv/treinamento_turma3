tweets = [
"Wow, what a great day today!! #sunshine",
"I feel sad about the things going on around us. #covid19",
"I'm really excited to learn Python with @JovianML #zerotopandas",
"This is a really nice song. #linkinpark",
"The python programming language is useful for data science",
"Why do bad things happen to me?",
"Apple announces the release of the new iPhone 12. Fans are excited.",
"Spent my day with family!! #happy",
"Check out my blog post on common string operations in Python. #zerotopandas",
"Freecodecamp has great coding tutorials. #skillup"
]
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

sad = 0
happy = 0

def ignore(sc):
    specialCharacters = ",.;;@#!?"
    for c in specialCharacters:
        sc = sc.replace(c," ")
    return sc



for c in tweets:
    nl = ignore(c)
    for i in sad_words:
        if i in nl :
            sad = sad+1
            print(nl+"\n-sad-")
    for j in happy_words:
        if j in nl :
            happy = happy+1
            print(nl+"\n-happy-") 
print("Tweets tristes: "+str(sad)) 
print("Tweets felizes: "+str(happy)) 
print("Tweets com palavra chave: "+str(sad+happy))
print("Tweets totais: " +str(len(tweets)))     
  
