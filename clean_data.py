import csv
from collections import defaultdict as ddict
import os
import xml
import nltk
from nltk.corpus import stopwords
from gensim import corpora, models, similarities
from bs4 import BeautifulSoup
import string

def process_txt_data():
    with open(wd + "jobs.tsv", "r") as infile:
        reader = csv.reader(infile, delimiter="\t",
        quoting=csv.QUOTE_NONE, quotechar="")
        reader.next() # burn the header
        i = 0
        for line in reader:
            (Jobid, WindowId, Title, Description, Requirements, City, State,
            Country, Zip5, StartDate, EndDate) = line
            desc_fn = os.path.join(wd,output,"description "+str(i)+".txt")
            req_fn = os.path.join(wd,output,"requirements"+str(i)+".txt")
            with open(desc_fn, 'w') as f:
                f.write(Description)
            with open(req_fn, 'w') as f:
                f.write(Requirements)
            i+=1
            if i % 500 ==0: print i," records processed.."

def prep_corpus(field):
    files=[]
    for i in range(200000):
        fn = os.path.join(wd,output,field+str(i)+".txt")
        files.append(fn)
    porter = nltk.PorterStemmer()
    stoplist = stopwords.words('english')
    texts=[]
    for f in files:
        document = open(f).read()
        document = ' '.join([line.strip() for line in document.split('\\r')])
        document = ' '.join([line.strip() for line in document.split('\\n')])
        soup = BeautifulSoup(document)
        document=soup.get_text()
        texts.append([porter.stem(word) for word in document.lower().split() if word not in stoplist])
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return dictionary, corpus

def lda_model(dictionary, corpus, n_topic):
    return models.LdaModel(corpus, id2word=dictionary, num_topics=n_topics)

def tf_idf(corpus):
    tfidf = models.TfidfModel(corpus)
    return tfidf[corpus]


wd = "/Users/linahu/Documents/Developer/CareerBuilder/"
output= "output"
#process_txt_data()
print "Building corpus from text files....."
desc_dict,desc_corpus = prep_corpus("description ")

print "Creating tf-idf transformation"

corpus_tfidf=tf_idf(desc_corpus)
n_topics = 20
print "Building LDA models..."
lda = lda_model(desc_dict,desc_corpus,n_topics)
lda1 =lda_model(desc_dict,corpus_tfidf,n_topics)

print "Building LSA models..."

lsi = models.lsimodel.LsiModel(desc_corpus, id2word=desc_dict, num_topics=100)

print "LSA results...."
for i in lsi.print_topics(20):
    print i


print
print "LDA results without tf-idf..."
for i in range(0, n_topics):
    temp = lda.show_topic(i, 10)
    terms = []
    for term in temp:
        terms.append(term[1])
    print "Top 10 terms for topic #" + str(i) + ": "+ ", ".join(terms)

print
print "LDA results with tf-idf..."
for i in range(0, n_topics):
    temp = lda1.show_topic(i, 10)
    terms = []
    for term in temp:
        terms.append(term[1])
    print "Top 10 terms for topic #" + str(i) + ": "+ ", ".join(terms)
