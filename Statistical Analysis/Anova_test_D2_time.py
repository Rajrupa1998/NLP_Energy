from scipy.stats import f_oneway

NLTK_tokenization_time_d2 = [81.53812671, 78.82896924, 79.89587569, 80.13414741, 79.70389748, 85.57254028, 85.82710218, 79.81734133, 85.92401791, 80.07121563]
Spacy_tokenization_time_d2 = [2005.219893]
Gensim_tokenization_time_d2 = [9.311569452, 8.049530983, 8.112555027, 9.626907825, 9.625812054, 9.608787537, 9.650310516, 9.689656973, 9.688742161, 9.602855206]

print("ANOVA test for Time-d2-Tokenization")
print(f_oneway(NLTK_tokenization_time_d2, Spacy_tokenization_time_d2, Spacy_tokenization_time_d2))
print("----------------------------------------------------------------------------")

NLTK_stemming_time_d2 = [91.81220126, 89.01014566, 88.66599202, 88.90760708, 88.59483695, 88.63767219, 88.71799612, 89.13510227, 88.74390173, 88.8426609]
Gensim_stemming_time_d2 = [43.51381946, 44.31510162, 44.10205507, 43.939533, 43.89966559, 44.01592326, 44.14751267, 42.43503881, 42.46275449]

print("ANOVA test for Time-d2-Stemming")
print(f_oneway(NLTK_stemming_time_d2, Gensim_stemming_time_d2))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_time_d2 = [35.51025033, 35.9642446, 35.96412563, 36.00459504, 36.01308775, 35.92154193, 36.16924691, 36.25559282, 36.02112126, 36.0195322]
Spacy_lemmatize_time_d2 = [2640.376809, 2812.150773]

print("ANOVA test for Time-d2-Lemmatize")
print(f_oneway(NLTK_lemmatize_time_d2, Spacy_lemmatize_time_d2))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_time_d2 = [20.70226407, 26.5618782, 21.04893255, 20.87487149, 21.03406572, 20.85415173, 26.91418934, 20.93002057, 20.93805099, 20.88191438]
Spacy_STOPWORD_time_d2 = [2942.933996]
Gensim_STOPWORD_time_d2 = [9.841174603, 9.867509127, 8.232871771, 8.189648628, 8.133188963, 8.142651081, 8.105086088, 8.113297939, 9.818936586, 9.689815044]

print("ANOVA test for Time-d2-STOPWORD")
print(f_oneway(NLTK_STOPWORD_time_d2, Spacy_STOPWORD_time_d2, Gensim_STOPWORD_time_d2))
print("----------------------------------------------------------------------------")

NLTK_POS_time_d2 = [1183.496827, 1180.081821, 1182.304313, 1185.954592, 1184.825948, 1183.841866]
Spacy_POS_time_d2 = [499.8360214, 581.2228706, 607.5410852, 584.3917854, 593.2109926, 593.8472986, 585.1266749, 578.8529379]

print("ANOVA test for Time-d2-POS")
print(f_oneway(NLTK_POS_time_d2, Spacy_POS_time_d2))
print("----------------------------------------------------------------------------")

NLTK_NER_time_d2 = [3188.312799, 3169.296007, 3168.809763, 3135.953574]
Spacy_NER_time_d2 = [1339.091886, 1466.271373, 1451.085066, 1525.313761]

print("ANOVA test for Time-d2-NER")
print(f_oneway(NLTK_NER_time_d2, Spacy_NER_time_d2))
print("----------------------------------------------------------------------------")