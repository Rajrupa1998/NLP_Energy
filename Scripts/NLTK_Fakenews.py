from pickletools import read_uint1
from random import sample

import pandas as pd
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import nltk
nltk.download('all')
import random
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, pos_tag_sents
from nltk import ne_chunk
import time

df = pd.read_csv("Fake.csv")

def sleep():
    time.sleep(30)

csv_handler = CSVHandler('NLTK_fakenews_output.csv')

def load_csv(path):
    return pd.read_csv(path)

df = load_csv(path="Fake.csv")


def tokenization_NLTK(df):
    df['tokenized']=df['text'].apply(nltk.word_tokenize)
    return df['tokenized']
    

df['tokenized']=tokenization_NLTK(df)
newdf1=df.copy()

def stemming_NLTK(df):
    stemmer = SnowballStemmer("english")
    #df['tokenized']=tokenization_NLTK()
    newdf1['stemmed'] = newdf1['tokenized'].apply(lambda x: [stemmer.stem(y) for y in x])
    return newdf1['stemmed']

df['stemmed']=stemming_NLTK(df)
newdf2=df.copy()

def lemmatization_NLTK(df):
    lmtzr = WordNetLemmatizer()
    #df['stemmed']=stemming_NLTK()
    newdf2['lemmatize'] = newdf2['stemmed'].apply(lambda lst:[lmtzr.lemmatize(word) for word in lst])
    return newdf2['lemmatize']

df['lemmatize']=lemmatization_NLTK(df)
newdf3=df.copy()

def stopwordremoval_NLTK(df):
    stop = stopwords.words('english')
    #df['stemmed']=stemming_NLTK()
    newdf3['Stopword_removed'] = newdf3['stemmed'].apply(lambda x: [item for item in x if item not in stop])
    return newdf3['Stopword_removed'] 


df['Stopword_removed']=stopwordremoval_NLTK(df)
newdf4=df.copy()

def postagging_NLTK(df):
    #df['Stopword_removed']=stopwordremoval_NLTK()
    sw=newdf4['Stopword_removed'].tolist()
    sw_list=[]
    for i in sw:
        sw_list.append(str(i))
    tagged_texts = pos_tag_sents(map(word_tokenize, sw_list))
    newdf4['POS_tags']=tagged_texts
    return newdf4['POS_tags']

df['POS_tags']=postagging_NLTK(df)
newdf5=df.copy()

def entityrecognition_NLTK(df):
    #df['POS_tags']=postagging_NLTK()
    newdf5['entity'] = newdf5['POS_tags'].apply(lambda lst:[nltk.ne_chunk(lst)])
    return newdf5['entity']

@measure_energy(handler=csv_handler)
def test_tokenization_NLTK():
    df['tokenized']=tokenization_NLTK(df)
    return df['tokenized']
    
@measure_energy(handler=csv_handler)
def test_stemming_NLTK():
    global df
    df['stemmed']=stemming_NLTK(df)
    return df['stemmed']

@measure_energy(handler=csv_handler)
def test_lemmatize_NLTK():
    global df
    df['lemmatize']=lemmatization_NLTK(df)
    return df['lemmatize']

@measure_energy(handler=csv_handler)
def test_stopwordremoval_NLTK():
    global df
    df['Stopword_removed']=stopwordremoval_NLTK(df)
    return df['Stopword_removed']

@measure_energy(handler=csv_handler)
def test_postagging_NLTK():
    global df
    df['POS_tags']=postagging_NLTK(df)
    return df['POS_tags']

@measure_energy(handler=csv_handler)
def test_entityrecognition_NLTK():
    global df
    df['entity']=entityrecognition_NLTK(df)
    return df['entity']


function_list=[test_tokenization_NLTK,test_lemmatize_NLTK,test_stemming_NLTK,test_stopwordremoval_NLTK,test_postagging_NLTK,test_entityrecognition_NLTK]

for i in range(10):
    
    print("This is iteration no:",i)

    #random.shuffle(function_list)

    for j in range(len(function_list)):

        sleep()

        function_list[j]()

# test_tokenization_NLTK()
# test_lemmatize_NLTK()
# test_stemming_NLTK()
# test_stopwordremoval_NLTK()
# test_postagging_NLTK()
# test_entityrecognition_NLTK()

print("Process complete")
csv_handler.save_data()