from bs4 import BeautifulSoup
import codecs
with open("photocaptions.txt") as f:
    s=f.read()
#s ="<a class=\"tumblr_blog\" href=\"http://swift13updates.tumblr.com/post/130463758194\" target=\"_blank\">swift13updates</a>:"
soup = BeautifulSoup(s)
l=[]
for anchor in soup.find_all('a'):
    l.append(anchor.text)

print len(l)

with codecs.open("photoanchortags.txt",'w',encoding='utf8') as f:
    for line in l:
        if line:
            f.write(line+"\n")