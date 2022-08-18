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

# 1. Quantos tweets existem nesse banco de dados?
# R: Existem 10 tweets
print("Exercício 1:")
print(len(tweets))
print()

# 2. A partir das listas de palavras apresentadas abaixo,
# tome o primeiro tweet como amostra e identifique se é feliz ou não.
print("Exercício 2:")
happy_words = [
    'great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best'
]
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

happy_tweets = 0
print("HAPPY:")
for i in happy_words:
    for j in range(len(tweets)):
        if i in tweets[j]:
            happy_tweets += 1
            print("O tweet:")
            print(tweets[j])
            print(f"contem a palavra '{i}'")
            print()
print(f"existem {happy_tweets} tweets felizes na lista 'tweeets'")
print()

sad_tweets = 0
print("SAD:")
for i in sad_words:
    for j in range(len(tweets)):
        if i in tweets[j]:
            sad_tweets += 1
            print("O tweet:")
            print(tweets[j])
            print(f"contem a palavra '{i}'")
            print()
print(f"existem {sad_tweets} tweets tristes na lista 'tweeets'")
print()
