from scipy.stats import f_oneway

NLTK_tokenization_GPU_d1 = [506.13, 499.73, 509.02, 500.47, 546.42, 498.32, 517.67, 507.13, 506.53, 511.76]
Spacy_tokenization_GPU_d1 = [14585.8, 14745.34, 15612.34, 15437.45, 15623.2, 15448.7, 15723.42, 15768.25, 15700.4, 15778.58]
Gensim_tokenization_GPU_d1 = [79.64, 74.23, 75.19, 73.48, 87.73, 74.76, 75.68, 85.61, 74.41, 74.85]

print("ANOVA test for GPU-D1-Tokenization")
print(f_oneway(NLTK_tokenization_GPU_d1, Spacy_tokenization_GPU_d1, Gensim_tokenization_GPU_d1))
print("----------------------------------------------------------------------------")

NLTK_stemming_GPU_d1 = [891.32, 885.33, 891.9, 888.26, 878.52, 902.83, 880.86, 897.76, 182.8]
Gensim_stemming_GPU_d1 = [455.58, 473.29, 469.15, 466.07, 464.56, 464.01, 465.35, 458.75, 473.35, 467.4]

print("ANOVA test for GPU-D1-Stemming")
print(f_oneway(NLTK_stemming_GPU_d1, Gensim_stemming_GPU_d1))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_GPU_d1 = [303.06, 346.4, 305.42, 303.16, 305.01, 304.51, 305.95, 304.32, 304.67]
Spacy_lemmatize_GPU_d1 = [16344.75, 16105.2, 16589.97, 16608.06, 16535.59, 16790.87]

print("ANOVA test for GPU-D1-Lemmatize")
print(f_oneway(NLTK_lemmatize_GPU_d1, Spacy_lemmatize_GPU_d1))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_GPU_d1 = [184.11, 183.24, 184.07, 184.42, 227.14, 187.11, 181.64, 183.14, 184.74, 184.74]
Spacy_STOPWORD_GPU_d1 = [15103.22, 16924.66, 16764.91, 16983.95, 17277.57, 17330.04, 17595.01]
Gensim_STOPWORD_GPU_d1 = [80.22, 75.89, 90.99, 78.51, 79.15, 88.61, 78.02, 78.48, 79.47, 91.4]

print("ANOVA test for GPU-D1-STOPWORD")
print(f_oneway(NLTK_STOPWORD_GPU_d1, Spacy_STOPWORD_GPU_d1, Gensim_STOPWORD_GPU_d1))
print("----------------------------------------------------------------------------")

NLTK_POS_GPU_d1 = [10063, 10151.03, 10050.66, 10113.72, 10089.44, 9978.13, 10089.47]
Spacy_POS_GPU_d1 = [6119.54, 6165.66, 6116.19, 6041.78, 5830.47, 6012.21, 6021.49, 6085.85, 6012.67, 6026.27]

print("ANOVA test for GPU-D1-POS")
print(f_oneway(NLTK_POS_GPU_d1, Spacy_POS_GPU_d1))
print("----------------------------------------------------------------------------")

NLTK_NER_GPU_d1 = [26926.13, 27185.7, 27060.11]
Spacy_NER_GPU_d1 = [9008.87, 9548.25, 9596.69, 9902.81, 10026.65, 10121.23]

print("ANOVA test for GPU-D1-NER")
print(f_oneway(NLTK_NER_GPU_d1, Spacy_NER_GPU_d1))
print("----------------------------------------------------------------------------")