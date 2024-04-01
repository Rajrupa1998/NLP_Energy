from scipy.stats import f_oneway

NLTK_tokenization_GPU_d3 = [359.23, 355.86, 350.93, 351.73, 342.52]
Spacy_tokenization_GPU_d3 = [29657.6]
Gensim_tokenization_GPU_d3 = [29.1, 34.29, 23.96, 24.4, 25.16, 25.49, 25.29, 24.92, 34.66, 36.23]

print("ANOVA test for GPU-d3-Tokenization")
print(f_oneway(NLTK_tokenization_GPU_d3, Spacy_tokenization_GPU_d3, Gensim_tokenization_GPU_d3))
print("----------------------------------------------------------------------------")

NLTK_stemming_GPU_d3 = [253.56, 276.44, 242.07, 244.47, 237.11]
Gensim_stemming_GPU_d3 = [120.8, 124.6, 124.31, 124.5, 126.62, 126.41, 126.94, 116.85, 118.09]

print("ANOVA test for GPU-d3-Stemming")
print(f_oneway(NLTK_stemming_GPU_d3, Gensim_stemming_GPU_d3))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_GPU_d3 = [470.78, 72.86, 99.39, 101.32, 97.26, 72.8, 71.15]
Spacy_lemmatize_GPU_d3 = [29401.98, 30257.7]

print("ANOVA test for GPU-d3-Lemmatize")
print(f_oneway(NLTK_lemmatize_GPU_d3, Spacy_lemmatize_GPU_d3))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_GPU_d3 = [51.8, 54.15, 53.91, 53.52, 52.72]
Spacy_STOPWORD_GPU_d3 = [30242.14]
Gensim_STOPWORD_GPU_d3 = [27.91, 29.92, 28.06, 29.89, 29.59, 29.64, 29.88, 29.4, 30.77, 29.31]

print("ANOVA test for GPU-d3-STOPWORD")
print(f_oneway(NLTK_STOPWORD_GPU_d3, Spacy_STOPWORD_GPU_d3, Gensim_STOPWORD_GPU_d3))
print("----------------------------------------------------------------------------")

NLTK_POS_GPU_d3 = [4327.76, 4396.51, 4290.59, 4312.97, 4316.53]
Spacy_POS_GPU_d3 = [2979.7, 3772.26, 3540.86, 3970.93, 4001.9, 3827.61, 3983.15, 4040.5]

print("ANOVA test for GPU-d3-POS")
print(f_oneway(NLTK_POS_GPU_d3, Spacy_POS_GPU_d3))
print("----------------------------------------------------------------------------")

NLTK_NER_GPU_d3 = [9747.69, 9497.69, 9451.72, 9378.09, 9355.18, 9429.92, 9504.51]
Spacy_NER_GPU_d3 = [29380.52]

print("ANOVA test for GPU-d3-NER")
print(f_oneway(NLTK_NER_GPU_d3, Spacy_NER_GPU_d3))
print("----------------------------------------------------------------------------")