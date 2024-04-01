from scipy.stats import f_oneway

NLTK_tokenization_DRAM_d1 = [659.39, 635.9, 634.75, 639.5, 634.32, 702.72, 687.79, 631.85, 684.39, 633.07]
Spacy_tokenization_DRAM_d1 = [9372.66]
Gensim_tokenization_DRAM_d1 = [86.99, 73.78, 74.74, 90.97, 90.74, 90.86, 90.7, 91.51, 92.23, 91.3]

print("ANOVA test for DRAM-D1-Tokenization")
print(f_oneway(NLTK_tokenization_DRAM_d1, Spacy_tokenization_DRAM_d1, Gensim_tokenization_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_stemming_DRAM_d1 = [744.29, 701.52, 701.19, 703.96, 718.1, 715.1, 704.86, 700.38, 695.73, 702.77]
Gensim_stemming_DRAM_d1 = [390.27, 398.26, 398.85, 398.14, 399.52, 400.41, 400, 383.41, 381.58]

print("ANOVA test for DRAM-D1-Stemming")
print(f_oneway(NLTK_stemming_DRAM_d1, Gensim_stemming_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_DRAM_d1 = [287.26, 290.15, 287.6, 288.05, 289.35, 293.1, 289.32, 285.73, 282.61, 287.4]
Spacy_lemmatize_DRAM_d1 = [13674.36, 14550.28]

print("ANOVA test for DRAM-D1-Lemmatize")
print(f_oneway(NLTK_lemmatize_DRAM_d1, Spacy_lemmatize_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_DRAM_d1 = [167.52, 219.92, 170.7, 166.93, 173.73, 168.79, 227.22, 168.49, 166.6, 168.9]
Spacy_STOPWORD_DRAM_d1 = [15266.35]
Gensim_STOPWORD_DRAM_d1 = [92.47, 93.64, 77.34, 76.6, 76.3, 77.12, 76.12, 76.02, 93.27, 90.85]

print("ANOVA test for DRAM-D1-STOPWORD")
print(f_oneway(NLTK_STOPWORD_DRAM_d1, Spacy_STOPWORD_DRAM_d1, Gensim_STOPWORD_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_POS_DRAM_d1 = [9525.7, 9384.91, 9498.43, 9508.57, 9550.45, 5890.84]
Spacy_POS_DRAM_d1 = [2728.16, 2976.46, 3117, 2946.21, 3038.31, 3047.07, 3031.08, 2962.15]

print("ANOVA test for DRAM-D1-POS")
print(f_oneway(NLTK_POS_DRAM_d1, Spacy_POS_DRAM_d1))
print("----------------------------------------------------------------------------")

NLTK_NER_DRAM_d1 = [25132.41, 25070.84, 25062.24, 25062.24]
Spacy_NER_DRAM_d1 = [6183.45, 6921.08, 6880.72, 7434.07]

print("ANOVA test for DRAM-D1-NER")
print(f_oneway(NLTK_NER_DRAM_d1, Spacy_NER_DRAM_d1))
print("----------------------------------------------------------------------------")