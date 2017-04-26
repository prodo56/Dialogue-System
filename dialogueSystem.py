import pysolr
solr = pysolr.Solr('http://localhost:8983/solr/lincoln/', timeout=10)

# How you would index data.
def addDocument(data):
    try:
        solr.add([data])
    except Exception as e:
        print "Exception while adding document to solr with message: ", e.message

def search(tokens):
    results = solr.search(" ".join(tokens))
    #print results.docs
    #print("Saw {0} result(s).".format(len(results)))
    return results

#print search("Awesome").docs