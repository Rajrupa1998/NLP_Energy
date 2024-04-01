from scipy.stats import f_oneway

NLTK_tokenization_DRAM_d3 = [230.78, 232.06, 213.41, 209.58, 209.88]
Spacy_tokenization_DRAM_d3 = [20215.51]
Gensim_tokenization_DRAM_d3 = [86.99, 73.78, 74.74, 90.97, 90.74, 90.86, 90.7, 91.51, 92.23, 91.3]

print("ANOVA test for DRAM-d3-Tokenization")
print(f_oneway(NLTK_tokenization_DRAM_d3, Spacy_tokenization_DRAM_d3, Gensim_tokenization_DRAM_d3))
print("----------------------------------------------------------------------------")

NLTK_stemming_DRAM_d3 = [146.61, 146.36, 148.66, 145.44, 165.56]
Gensim_stemming_DRAM_d3 = [390.27, 398.26, 398.85, 398.14, 399.52, 400.41, 400, 383.41, 381.58]

print("ANOVA test for DRAM-d3-Stemming")
print(f_oneway(NLTK_stemming_DRAM_d3, Gensim_stemming_DRAM_d3))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_DRAM_d3 = [64.67, 63.23, 43.3, 42.96, 44.22, 43.43, 43.43]
Spacy_lemmatize_DRAM_d3 = [20178.23, 20526.29]

print("ANOVA test for DRAM-d3-Lemmatize")
print(f_oneway(NLTK_lemmatize_DRAM_d3, Spacy_lemmatize_DRAM_d3))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_DRAM_d3 = [52.02, 53.1, 52.98, 52.53, 32.49]
Spacy_STOPWORD_DRAM_d3 = [15266.35]
Gensim_STOPWORD_DRAM_d3 = [20871.19]

print("ANOVA test for DRAM-d3-STOPWORD")
print(f_oneway(NLTK_STOPWORD_DRAM_d3, Spacy_STOPWORD_DRAM_d3, Gensim_STOPWORD_DRAM_d3))
print("----------------------------------------------------------------------------")

NLTK_POS_DRAM_d3 = [2575.7, 2588.28, 2588.92, 2580.97, 2570.06]
Spacy_POS_DRAM_d3 = [2212.8, 2812, 2651.02, 2957.62, 2970.91, 2870.96, 3021.25, 3019.9]

print("ANOVA test for DRAM-d3-POS")
print(f_oneway(NLTK_POS_DRAM_d3, Spacy_POS_DRAM_d3))
print("----------------------------------------------------------------------------")

NLTK_NER_DRAM_d3 = [5825.11, 5678.78, 5689.2, 5708.74, 5686.78, 5690.73, 5758.48]
Spacy_NER_DRAM_d3 = [20078.19]

print("ANOVA test for DRAM-d3-NER")
print(f_oneway(NLTK_NER_DRAM_d3, Spacy_NER_DRAM_d3))
print("----------------------------------------------------------------------------")