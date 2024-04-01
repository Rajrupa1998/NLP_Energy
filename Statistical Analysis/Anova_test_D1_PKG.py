from scipy.stats import f_oneway

NLTK_tokenization_PKG_d1 = [3196.76, 3230.06, 3221.46, 3219.3, 3489.14, 3217.8, 3212.1, 3220.54, 3211.12, 3214.96]
Spacy_tokenization_PKG_d1 = [119024.06]
Gensim_tokenization_PKG_d1 = [671.28, 614.5, 574.75, 577.16, 562.43, 665.92, 569.77, 557.87, 640.67, 566.08, 564.73]

print("ANOVA test for PKG-D1-Tokenization")
print(f_oneway(NLTK_tokenization_PKG_d1, Spacy_tokenization_PKG_d1, Spacy_tokenization_PKG_d1))
print("----------------------------------------------------------------------------")

NLTK_stemming_PKG_d1 = [5646.82, 5647.38, 5656.74, 5654.98, 5649.34, 5653.1, 5665.94, 5651.88, 5654.32]
Gensim_stemming_PKG_d1 = [3493.75, 3618.47, 3554.76, 3521.69, 3517.24, 3516.71, 3503.81, 3493.56, 3566.88, 3498.71]

print("ANOVA test for PKG-D1-Stemming")
print(f_oneway(NLTK_stemming_PKG_d1, Gensim_stemming_PKG_d1))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_PKG_d1 = [1915.58, 2201.48, 1934.86, 1932.98, 1938.26, 1933, 1930.68, 1935.9, 1942.18]
Spacy_lemmatize_PKG_d1 = [121205.97, 120710.78, 124597.2, 124846.1, 124306.65, 126402.03]

print("ANOVA test for PKG-D1-Lemmatize")
print(f_oneway(NLTK_lemmatize_PKG_d1, Spacy_lemmatize_PKG_d1))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_PKG_d1 = [1165.18, 1166.44, 1169.98, 1162.14, 1173.8, 1440.36, 1173.34, 1168.56, 1167.42, 1166.74]
Spacy_STOPWORD_PKG_d1 = [113081.91, 124660.7, 126058.09, 128625.09, 129359.02, 129749.85, 130923.76]
Gensim_STOPWORD_PKG_d1 = [620.88, 584.8, 687.57, 596.18, 593.68, 661.82, 589.56, 593.88, 596.99]

print("ANOVA test for PKG-D1-STOPWORD")
print(f_oneway(NLTK_STOPWORD_PKG_d1, Spacy_STOPWORD_PKG_d1, Gensim_STOPWORD_PKG_d1))
print("----------------------------------------------------------------------------")

NLTK_POS_PKG_d1 = [63987.28, 64260.9, 64044.9, 63876, 63893.66, 64302.74, 63979.52]
Spacy_POS_PKG_d1 = [45988.86, 46301.33, 45834.25, 45849.16, 45656.6, 45808.05, 45765.22, 45749.41, 46090.76, 46076.38]

print("ANOVA test for PKG-D1-POS")
print(f_oneway(NLTK_POS_PKG_d1, Spacy_POS_PKG_d1))
print("----------------------------------------------------------------------------")

NLTK_NER_PKG_d1 = [171135.22, 171646.56, 173127.94]
Spacy_NER_PKG_d1 = [66589.51, 70176.91, 73057.53, 74165.9, 74462.65, 74855.92]

print("ANOVA test for PKG-D1-NER")
print(f_oneway(NLTK_NER_PKG_d1, Spacy_NER_PKG_d1))
print("----------------------------------------------------------------------------")