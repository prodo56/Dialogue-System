from nltk.corpus import stopwords
import codecs
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
import dialogueSystem

tokenizer = TreebankWordTokenizer()


with codecs.open("taylor.txt",encoding="utf-8") as f:
    taylor_data = f.readlines()

#print taylor_data
#sent_tokenize_list = sent_tokenize(taylor_data)
#print sent_tokenize_list,len(sent_tokenize_list)
i=1
for sentence in taylor_data:
    #sentences.append(" ".join([word for word in tokenizer.tokenize(sentence) if word not in stopwords.words('english')]))
    #print sentence, sentences[-1]
    sentence = sentence.replace("\n"," ").replace("\r"," ")
    #print sentence
    dialogueSystem.addDocument({'id': str(i), 'sentence': sentence})
    i+=1

#print sentences
