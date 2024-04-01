from scipy.stats import f_oneway

NLTK_tokenization_DRAM_d1 = [302.64, 304.88, 306.83, 307.62, 338.26, 308.78, 303.55, 304.64, 303.32, 302.9]
Spacy_tokenization_DRAM_d1 = [10442.26, 10979.39, 11290.43, 11379.2, 11478.76, 11466.04, 11554.41]
Gensim_tokenization_DRAM_d1 = [57.36, 53.5, 53.79, 52.1, 63.27, 52.92, 52.3, 61.41, 53.16, 53.41]

print("ANOVA test for DRAM-D1-Tokenization")
print(f_oneway(NLTK_tokenization_DRAM_d1, Spacy_tokenization_DRAM_d1, Spacy_tokenization_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_stemming_DRAM_d1 = [533.49, 531.19, 542.36, 534.32, 543.53, 538.72, 533.79, 532.01, 530.77]
Gensim_stemming_DRAM_d1 = [318.12, 331.82, 324.67, 321.73, 321.31, 321.36, 321.91, 321.7, 321.88]

print("ANOVA test for DRAM-D1-Stemming")
print(f_oneway(NLTK_stemming_DRAM_d1, Gensim_stemming_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_DRAM_d1 = [181.47, 213.52, 183.08, 187.39, 184.66, 184.76, 184.61, 183.84, 183.33]
Spacy_lemmatize_DRAM_d1 = [11892.01, 11849.4, 12209.98, 12248.03, 12225.25, 12436.27]

print("ANOVA test for DRAM-D1-Lemmatize")
print(f_oneway(NLTK_lemmatize_DRAM_d1, Spacy_lemmatize_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_DRAM_d1 = [110.14, 110.79, 110.75, 113.52, 112.7, 143.84, 113.97, 111.33, 110.7, 110.32]
Spacy_STOPWORD_DRAM_d1 = [10908.35, 12221.62, 12375.69, 12550.22, 12728.73, 12749.45, 12840.08]
Gensim_STOPWORD_DRAM_d1 = [57.64, 53.98, 65.17, 55.45, 55.51, 62.94, 55.08, 56.55, 57.14, 64.7]

print("ANOVA test for DRAM-D1-STOPWORD")
print(f_oneway(NLTK_STOPWORD_DRAM_d1, Spacy_STOPWORD_DRAM_d1, Gensim_STOPWORD_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_POS_DRAM_d1 = [6004.67, 6050.66, 6057.24, 6059.57, 6019.42, 6038.07, 5991.08]
Spacy_POS_DRAM_d1 = [6296.34, 6708.08, 7064.25, 7247.36, 7272.84, 7281.17]

print("ANOVA test for DRAM-D1-POS")
print(f_oneway(NLTK_POS_DRAM_d1, Spacy_POS_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_NER_DRAM_d1 = [16087.13, 16232.74, 16334.72]
Spacy_NER_DRAM_d1 = [6296.34, 6708.08, 7064.25, 7247.36, 7272.84, 7281.17]

print("ANOVA test for DRAM-D1-NER")
print(f_oneway(NLTK_NER_DRAM_d1, Spacy_NER_DRAM_d1))
print("----------------------------------------------------------------------------")