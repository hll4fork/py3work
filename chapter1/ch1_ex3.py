#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/25
# brief         : <Programming in Python3 > chapter1 exercise 3 (page:47)
##########################################################################

# How to solve the problem
# 1. create list for article, subject, verb, adverb
# 2. choose items from 4 lists
# 3. loop five times and print the sentence

import random

# 1. create lists
articles = ["the", "a"]
subjects = ["cat", "dog", "man", "woman"]
verbs    = ["sang", "run","jumped"]
adverbs  = ["loudly","quietly", "well","badly"]
sentence = [] # save item and form a sentence for printing

count = 0
while True:
    sentence.append(articles[random.randint(0,1)])     # 2. choose items
    sentence.append(subjects[random.randint(0,3)])
    sentence.append(verbs[random.randint(0,2)])
    sentence.append(adverbs[random.randint(0,3)])
    print(sentence[0], sentence[1], sentence[2], sentence[3])                               # 3. print sentence
    sentence = []
    count += 1
    if count >=5:
        break



