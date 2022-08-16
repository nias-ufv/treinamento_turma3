tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited",
    "Spend my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
    ]

# 1. Quantos tweets existem nesse banco de dados?
print("Existem", len(tweets), "tweets nesse banco de dados")

# 2. Identifique se os tweets são felizes ou não
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

def apaga(tweet):
    """"É uma função para remover qualquer pontuação (.,:;!@#?) que esteja
    para facilitar na identificação de humor no tweet
    
    >>> apaga('Spend my day with family!! #happy')
    
    Spend my day with family!! happy
    """
    
    pont = ".,:;!@#?"
    for p in pont:
        tweet = tweet.replace(p, "")
    return tweet

def identificacaoFeliz(words):
    """"É uma função para verficar se uma frase contém uma palavra considerada
    feliz
    
    >>> identificacaoTriste('Why do bad things happen to me?')
    
    False
    
    >>> identificacaoTriste('Spend my day with family!! #happy')
    
    True
    """
    i = 0
    j = 0
    while i < len(happy_words):
        while j < len(words):
            if words[j] == happy_words[i]:
                return True
            j += 1
        i += 1
        j = 0
    return False

def identificacaoTriste(words):
    """"É uma função para verficar se uma frase contém uma palavra considerada
    triste
    
    >>> identificacaoTriste('Why do bad things happen to me?')
    
    True
    
    >>> identificacaoTriste('Spend my day with family!! #happy')
    
    False
    """
    i = 0
    j = 0
    while i < len(sad_words):
        while j < len(words):
            if words[j] == sad_words[i]:
                return True
            j += 1
        i += 1
        j = 0
    return False

k = 0
contHappy = 0
contSad = 0
#prints de organização
print("")
print("")
while k < len(tweets):
    newTweet = apaga(tweets[k])
    words = newTweet.split()
    # o programa executa o if se alguma palavra contida na variavel 'happy_words'
    # estiver contida na frase
    if identificacaoFeliz(words) == True:
        print('"{}" é um tweet feliz'.format(tweets[k]))
        contHappy += 1
    # o programa executa o if se alguma palavra contida na variavel 'sad_words'
    # estiver contida na frase
    elif identificacaoTriste(words) == True:
        print('"{}" é um tweet triste'.format(tweets[k]))
        contSad += 1
    # alguns tweets não possuem palavras consideradas feliz ou palavras
    # consideradas triste, então foi tido como um tweet neutro
    else:
        print('"{}" é um tweet neutro'.format(tweets[k]))
    k += 1

#prints de organização
print("")
print("")
# 3. Conte quantos tweets felizes e quantos tweets triste estão
# contido na lista "tweets"
print('Existe {} tweets felizes contidos na lista "tweets"'.format(contHappy))
print('Existe {} tweets tristes contidos na lista "tweets"'.format(contSad))