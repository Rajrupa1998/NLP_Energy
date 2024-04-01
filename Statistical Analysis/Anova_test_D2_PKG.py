from scipy.stats import f_oneway

NLTK_tokenization_PKG_d2 = [8127.86, 7872.72, 7970.53, 7993.83, 7953.24, 8521.43, 8546.17, 7960.55, 8557.14, 7984.29]
Spacy_tokenization_PKG_d2 = [194762.96]
Gensim_tokenization_PKG_d2 = [933.71, 897.68, 779.29, 785.66, 933.89, 934.04, 926.45, 931.04, 936.12, 935.37, 925.12]

print("ANOVA test for PKG-d2-Tokenization")
print(f_oneway(NLTK_tokenization_PKG_d2, Spacy_tokenization_PKG_d2, Spacy_tokenization_PKG_d2))
print("----------------------------------------------------------------------------")

NLTK_stemming_PKG_d2 = [9117.65, 8859.08, 8817.55, 8834.28, 8813.65, 8819.41, 8820.97, 8858.37, 8826.71, 8839.5]
Gensim_stemming_PKG_d2 = [4230.46, 4307.87, 4285.51, 4285.92, 4256.31, 4266.99, 4301.98, 4118.46, 4113.33]

print("ANOVA test for PKG-d2-Stemming")
print(f_oneway(NLTK_stemming_PKG_d2, Gensim_stemming_PKG_d2))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_PKG_d2 = [3554.26, 3602.97, 3601.38, 3604.77, 3606.08, 3600.32, 3624.91, 3631.3, 3610.25, 3609.33]
Spacy_lemmatize_PKG_d2 = [253268.88, 268693.27]

print("ANOVA test for PKG-d2-Lemmatize")
print(f_oneway(NLTK_lemmatize_PKG_d2, Spacy_lemmatize_PKG_d2))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_PKG_d2 = [2051.82, 2620.94, 2092, 2070.55, 2084.78, 2070.6, 2655.87, 2074.89, 2079.51, 2071.5]
Spacy_STOPWORD_PKG_d2 = [282045.83]
Gensim_STOPWORD_PKG_d2 = [956.98, 958.33, 803.43, 802.68, 790.95, 793.38, 790.53, 794.5, 950.84]

print("ANOVA test for PKG-d2-STOPWORD")
print(f_oneway(NLTK_STOPWORD_PKG_d2, Spacy_STOPWORD_PKG_d2, Gensim_STOPWORD_PKG_d2))
print("----------------------------------------------------------------------------")

NLTK_POS_PKG_d2 = [118515.22, 118236.55, 118587.63, 118712.85, 118550.12, 118475.22]
Spacy_POS_PKG_d2 = [49668.22, 57677.78, 59922.46, 57917.95, 59026.84, 57814.89, 57486.18]

print("ANOVA test for PKG-d2-POS")
print(f_oneway(NLTK_POS_PKG_d2, Spacy_POS_PKG_d2))
print("----------------------------------------------------------------------------")

NLTK_NER_PKG_d2 = [1319886.56, 317129.63, 316900.31, 313532.73]
Spacy_NER_PKG_d2 = [129992.07, 141728.83, 140346.25, 147335.4]

print("ANOVA test for PKG-d2-NER")
print(f_oneway(NLTK_NER_PKG_d2, Spacy_NER_PKG_d2))
print("----------------------------------------------------------------------------")