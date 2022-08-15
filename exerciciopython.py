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
cont = len(tweets)
print('Existem %d tweets nesse banco de dados'%cont)

def plfeliz(feliz,string):
    return set(feliz).intersection(string.split())

is_happy = False

def pltrist(triste,stringt):
    return set(triste).intersection(stringt.split())
tfeliz = 0
ttrist = 0

for x in tweets:
    string = ('%s'%x).replace("#","")
    string2 = ('%s'%string).replace(".","")
    #print(x)
    #print(string2)
    ps = happy_words
    if plfeliz(happy_words,string2):
        #print('Uhu')
        is_happy = True
        tfeliz = tfeliz + 1
    if pltrist(sad_words,string2):
        #print(':(')
        is_happy = False
        ttrist = ttrist + 1

    #if string in happy_words: ta tudo errado
        #is_happy = True
    #else:
        #is_happy = False
print('Existem %d tweets felizes e %d tristes.' %(tfeliz,ttrist))



