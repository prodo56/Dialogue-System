import json
import re
import codecs
with open("taylorswift.json") as f:
    jsons = json.load(f)

tags= []
photocaptions=[]
linktext=[]
linkdescriptions=[]
for jsondata in jsons["posts"]:
    if "tags" in jsondata:
        tags+=jsondata["tags"]
    if "photo-caption" in jsondata:
        photocaptions.append(jsondata["photo-caption"])
    if "link-text" in jsondata:
        linktext.append(jsondata["link-text"])
    if "link-description" in jsondata:
        linkdescriptions.append(jsondata["link-description"])
#print tags
#print linkdescriptions
#print " ".join(linktext)
#print photocaptions

#with codecs.open("tags.txt",'w',encoding='utf8') as f:
 #   f.write(" ".join(tags))
with codecs.open("linktext.txt","w",encoding='utf8') as f:
    for line in linktext:
        if line:
            f.write(line+"\n")
with codecs.open("photocaptions.txt","w",encoding='utf8') as f:
    for line in photocaptions:
        if line:
            f.write(line+"\n")
with codecs.open("linkdescriptions.txt","w",encoding='utf8') as f:
    for line in linkdescriptions:
        if line:
            f.write(line+"\n")
