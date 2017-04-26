from dialogueSystem import search
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer

def findHighestMatch(processedSentences,processedQuery):
    maxMatch = 0
    maxKey = None
    for key in processedSentences.keys():
        result = processedSentences[key].intersection(processedQuery)
        if len(result) > maxMatch:
            maxMatch = len(result)
            maxKey = key
    return maxKey

def similarityScore(processedSentence, processedQuery):
    intersectionCount = len(processedSentence.intersection(processedQuery))
    unionCount = len(processedSentence.union(processedQuery))
    return float(intersectionCount/float(unionCount))

question = raw_input("enter question: ")
tokenizer = TreebankWordTokenizer()

data = search(question.split())
#print("Saw {0} result(s).".format(len(data)))
#awesomeprint data.docs
sentence = {}
processedSentences = {}
for doc in data.docs:
    doc = dict(doc)
    sentence[doc['id']] = str(doc['sentence']).replace('\n', ' ').replace('\r', '')
    processedSentences[doc['id']] = set([word for word in tokenizer.tokenize(str(doc['sentence']).replace("\n", " ")) if word not in stopwords.words('english')])

processedQuery = set([word for word in tokenizer.tokenize(question) if word not in stopwords.words('english')])
maxMatchDoc = findHighestMatch(processedSentences,processedQuery)
print str(sentence[maxMatchDoc])
print similarityScore(processedSentences[maxMatchDoc], processedQuery)
