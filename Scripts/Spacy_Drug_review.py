from pickletools import read_uint1
from random import sample
import pandas as pd
import random
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import spacy
import time



def sleep():
    time.sleep(30)

csv_handler = CSVHandler('Spacy_drug_review_output.csv')




def load_csv(path):
    return pd.read_csv(path)

df = load_csv(path="drug_review.csv")


spacy.prefer_gpu()
nlp = spacy.load('en_core_web_md')


def tokenization_SPACY(df):
    df['tokenized'] = df['review'].apply(lambda x: nlp(x))
    return  df['tokenized']


df['tokenized']=tokenization_SPACY(df)
newdf1=df.copy()

def lemmatization_SPACY(df):
    #newdf1['tokenized']=tokenization_SPACY()
    newdf1['lemmatize'] = newdf1['tokenized'].apply(lambda row: " ".join([w.lemma_ for w in nlp(row)]))
    return newdf1['lemmatize']


df['lemmatize']=lemmatization_SPACY(df)
newdf2=df.copy()

def stopword_removal_SPACY(df):
    #newdf2['lemmatize']=lemmatization_SPACY()
    newdf2['removed'] = newdf2.lemmatize.apply(lambda text: 
                                          " ".join(token.lemma_ for token in nlp(text) 
                                                   if not token.is_stop))
    return newdf2['removed']

df['removed']=stopword_removal_SPACY(df)
newdf3=df.copy()

def pos_tagging_SPACY(df):
    #newdf3['removed']=stopword_removal_SPACY()
    pos = []
    token= []
    for sent in nlp.pipe(newdf3['removed']):
        if sent.has_annotation('DEP'):
            token.append([word.text for word in sent])
            pos.append([word.pos_ for word in sent])
    newdf3['pos'] = pos
    newdf3['token'] = token
    newdf3['noun'] = newdf3.apply(lambda x: x['pos'].count('NOUN'), axis=1)
    return newdf3['pos']


df['pos']=pos_tagging_SPACY(df)
newdf4=df.copy()

def ner_SPACY(df):
    #newdf4['pos']=pos_tagging_SPACY()
    newdf4['NER'] = newdf4['removed'].apply(lambda x: list(nlp(x).ents))
    return newdf4['NER']

@measure_energy(handler=csv_handler)
def test_tokenization_SPACY():
    df['tokenized']=tokenization_SPACY(df)
    return df['tokenized']
 
@measure_energy(handler=csv_handler)   
def test_lemmatization_SPACY():
    global df
    df['lemmatize'] = lemmatization_SPACY(df)
    return df['lemmatize']

@measure_energy(handler=csv_handler)
def test_stopword_removal_SPACY():
    global df
    df['removed']=stopword_removal_SPACY(df)
    return df['removed']

@measure_energy(handler=csv_handler)
def test_pos_tagging_SPACY():
    global df
    df['pos']=pos_tagging_SPACY(df)
    return df['pos']

@measure_energy(handler=csv_handler)
def test_ner_SPACY():
    global df
    df['NER']=ner_SPACY(df)
    return df['NER']

function_list=[test_tokenization_SPACY,test_lemmatization_SPACY,test_stopword_removal_SPACY,test_pos_tagging_SPACY,test_ner_SPACY]

for i in range(8):

    print("This is iteration no:",i)

    #random.shuffle(function_list)

    for j in range(len(function_list)):

        sleep()

        function_list[j]()



print("Process complete")
csv_handler.save_data()

