cont=som=0
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
frases = len(tweets)
print("Existem {} frases".format(frases))
def apaga(i):
    pont = ".,:;!@#?"
    for p in pont:
        i = i.replace(p, " ")
    return i
for i in tweets:
    q=apaga(i)
    for j in happy_words:
        if j in q:
           cont+=1
           print("happy, yass!")
    for t in sad_words:
        if t in q:
           som+=1
           print("its sad, :(")
print(cont, "num happy")
print(som, "num sad")