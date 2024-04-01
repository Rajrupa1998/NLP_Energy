from scipy.stats import f_oneway


NLTK_tokenization_time_d1=[38.66331577,39.08108115,38.95606089,38.95857525,42.17606688,38.90274239,38.8856926,38.95070219,38.84591007,38.87867808]
Spacy_tokenization_time_d1=[1119.695555,1122.755282,1171.129569,1189.522821,1195.76536,1204.277273,1213.030612,1215.66676,1217.067656,1223.703054]
Gensim_tokenization_time_d1=[6.338101625,5.922127962,5.951387644,5.801716328,6.876076937,5.884299755,5.811897516,6.684405565,5.896534204,5.871305943]

 
print("ANOVA test for Time-D1-Tokenization")
print(f_oneway(NLTK_tokenization_time_d1,Spacy_tokenization_time_d1,Spacy_tokenization_time_d1 ))
print("----------------------------------------------------------------------------")

NLTK_stemming_time_d1=[68.32100677,68.40498495,68.52991819,68.46985936,68.43417978,68.49536252,68.61542773,68.46559572,68.54123855]
Gensim_stemming_time_d1=[35.91982722,37.21271181,36.53914475,36.23280215,36.29569077,36.30347633,36.29851818,36.199296,36.96099257,36.26372433]



print("ANOVA test for Time-D1-Stemming")
print(f_oneway(NLTK_stemming_time_d1,Gensim_stemming_time_d1 ))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_time_d1=[23.21104789,26.68838382,23.46491528,23.41632867,23.46276426,23.44019699,23.41815066,23.48054194,23.5455029]
Spacy_lemmatize_time_d1=[1247.596822,1247.441547,1282.825068,1289.095642,1287.114352,1302.935485]


print("ANOVA test for Time-D1-Lemmatize")
print(f_oneway(NLTK_lemmatize_time_d1,Spacy_lemmatize_time_d1 ))
print("----------------------------------------------------------------------------")


NLTK_STOPWORD_time_d1=[14.09321332,14.16002297,14.1916306,14.12683463,14.23619533,17.49424529,14.23471999,14.18844032,14.192837,14.16667223]
Spacy_STOPWORD_time_d1=[1156.807748,1286.192639,1302.772353,1324.170579,1338.991364,1339.138652,1348.383282]
Gensim_STOPWORD_time_d1=[6.374686003,6.000588179,7.071595192,6.132572174,6.171862841,6.8503263,6.119367599,6.174915075,6.20775938,6.986350298]


print("ANOVA test for Time-D1-STOPWORD")
print(f_oneway(NLTK_STOPWORD_time_d1,Spacy_STOPWORD_time_d1,Gensim_STOPWORD_time_d1 ))
print("----------------------------------------------------------------------------")

NLTK_POS_time_d1=[772.8477385,776.4039578,773.8592317,771.5939543,772.2887859,776.9040089,773.5711203]
Spacy_POS_time_d1=[467.5332544,469.7831743,467.7802799,468.0177219,464.2280273,467.531971,465.118983,465.5093913,467.1396031,466.9225824]



print("ANOVA test for Time-D1-POS")
print(f_oneway(NLTK_POS_time_d1,Spacy_POS_time_d1 ))
print("----------------------------------------------------------------------------")

NLTK_NER_time_d1=[2065.892813,2072.649386,2089.495171]
Spacy_NER_time_d1=[682.2367332,721.5598686,753.0297604,767.2502131,767.6530943,774.6839664]



print("ANOVA test for Time-D1-NER")
print(f_oneway(NLTK_NER_time_d1,Spacy_NER_time_d1 ))
print("----------------------------------------------------------------------------")


