import pandas as pd
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import gensim
from gensim.utils import tokenize
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
from operator import attrgetter
import random
from pyJoules.device.nvidia_device import NvidiaGPUDomain
import time

df=pd.DataFrame()
df_samp = pd.DataFrame()


def load_csv(path):
    return pd.read_csv(path)

df = load_csv(path="drug_review.csv")



def sleep():
    time.sleep(30)

csv_handler = CSVHandler('Gensim_drug_review_output.csv')

def tokenization_GENSIM(df):
    
    df['tokenized'] = df['review'].apply(lambda row:([x for x in tokenize(row)]))
    return df['tokenized']


df['tokenized']=tokenization_GENSIM(df)
newdf1=df.copy()

def stemming_GENSIM(df):
    stemmer = PorterStemmer()
    
    newdf1['stemmed'] = newdf1['tokenized'].apply(lambda x: [stemmer.stem(y) for y in x])
    # df['tokenized']=attrgetter('tokenized')
    # df['stemmed'] = df['tokenized'].apply(lambda x: [stemmer.stem(y) for y in x])
    return newdf1['stemmed']

df['stemmed']=stemming_GENSIM(df)
newdf2=df.copy()

def stopword_removal_GENSIM(df):
   
    newdf2['removed']=newdf2['stemmed'].apply(lambda x: [remove_stopwords(y) for y in x])
    return newdf2['removed']



@measure_energy(handler=csv_handler)
def test_tokenization_GENSIM():
    df['tokenized']=tokenization_GENSIM(df)
    return df['tokenized'] 


@measure_energy(handler=csv_handler)
def test_stemming_GENSIM():
    global df
    df['stemmed']=stemming_GENSIM(df)
    return df['stemmed'] 

@measure_energy(handler=csv_handler)
def test_stopword_removal_GENSIM():
    global df
    df['removed']=stopword_removal_GENSIM(df)
    return df['removed']    


function_list=[test_tokenization_GENSIM,test_stemming_GENSIM,test_stopword_removal_GENSIM]

for i in range(10):

    print("This is iteration no:",i)

    #random.shuffle(function_list)

    for j in range(len(function_list)):

        sleep()

        function_list[j]()

    

print("Process complete")
csv_handler.save_data()