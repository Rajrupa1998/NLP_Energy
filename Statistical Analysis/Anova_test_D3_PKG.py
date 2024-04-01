from scipy.stats import f_oneway

NLTK_tokenization_PKG_d3 = [2863.44, 2878.35, 2681.05, 2665.86, 2657.3]
Spacy_tokenization_PKG_d3 = [217018.06]
Gensim_tokenization_PKG_d3 = [215.35, 243.91, 181.54, 185.17, 183.46, 185.08, 183.33, 183.55, 255.32, 254.69]

print("ANOVA test for PKG-d3-Tokenization")
print(f_oneway(NLTK_tokenization_PKG_d3, Spacy_tokenization_PKG_d3, Gensim_tokenization_PKG_d3))
print("----------------------------------------------------------------------------")

NLTK_stemming_PKG_d3 = [32539.69, 1827.18, 1839.16, 1849.4, 1837.71, 2047.36]
Gensim_stemming_PKG_d3 = [884.1, 914.29, 917.51, 913.27, 915.31, 915.89, 910.79, 846.19, 846.78]

print("ANOVA test for PKG-d3-Stemming")
print(f_oneway(NLTK_stemming_PKG_d3, Gensim_stemming_PKG_d3))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_PKG_d3 = [747.14, 741.53, 540.06, 538.91, 545.49, 544.86, 542.78]
Spacy_lemmatize_PKG_d3 = [217448.32, 220911.1]

print("ANOVA test for PKG-d3-Lemmatize")
print(f_oneway(NLTK_lemmatize_PKG_d3, Spacy_lemmatize_PKG_d3))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_PKG_d3 = [599.36, 610.36, 609.69, 606.81, 404.83]
Spacy_STOPWORD_PKG_d3 = [224388.06]
Gensim_STOPWORD_PKG_d3 = [213.25, 217.31, 213.2, 216.89, 215.87, 215.85, 214.49, 212.92, 218.69, 212.66]

print("ANOVA test for PKG-d3-STOPWORD")
print(f_oneway(NLTK_STOPWORD_PKG_d3, Spacy_STOPWORD_PKG_d3, Gensim_STOPWORD_PKG_d3))
print("----------------------------------------------------------------------------")

NLTK_POS_PKG_d3 = [32561.67, 32709.96, 32880.38, 32707.29]
Spacy_POS_PKG_d3 = [22548.23, 27882.88, 26385.91, 29183.6, 29355.25, 28404.49, 29795.51, 29962.99]

print("ANOVA test for PKG-d3-POS")
print(f_oneway(NLTK_POS_PKG_d3, Spacy_POS_PKG_d3))
print("----------------------------------------------------------------------------")

NLTK_NER_PKG_d3 = [72781.81, 71417.65, 71975.43, 72251.34, 72251.23, 71708.94, 72153.03]
Spacy_NER_PKG_d3 = [216389.51]

print("ANOVA test for PKG-d3-NER")
print(f_oneway(NLTK_NER_PKG_d3, Spacy_NER_PKG_d3))
print("----------------------------------------------------------------------------")