import random

articles = ["the", "a", "one", "some", "any"]
nouns = ["boy", "girl", "dog", "town", "car"]
verbs = ["drove", "jumped", "ran", "walked", "skipped"]
prepositions = ["to", "from", "over", "under", "on"]


for _ in range(20):
    sentence = "{} {} {} {} {} {}".format(
        random.choice(articles),
        random.choice(nouns),
        random.choice(verbs),
        random.choice(prepositions),
        random.choice(articles),
        random.choice(nouns),
    ).capitalize()
    print(sentence)


# def getRandomSenteces():
#     for word in articles:
#
#         for n in nouns:
#
#             for ver in verbs:
#
#                 for prep in prepositions:
#                     print(word + " " + n + " " + " " + ver + " " + " " + prep)
#
#
# getRandomSenteces()
