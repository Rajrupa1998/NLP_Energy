from scipy.stats import f_oneway

NLTK_tokenization_GPU_d2 = [1106.86, 1071.84, 1106.51, 1076.19, 1084.93, 1159.2, 1143.85, 1066.84, 1162.72, 1065.27]
Spacy_tokenization_GPU_d2 = [26885.67]
Gensim_tokenization_GPU_d2 = [123.04, 106.8, 106.72, 127.05, 125.43, 125.91, 127.93, 126.91, 130.97, 129.5]

print("ANOVA test for GPU-d2-Tokenization")
print(f_oneway(NLTK_tokenization_GPU_d2, Spacy_tokenization_GPU_d2, Gensim_tokenization_GPU_d2))
print("----------------------------------------------------------------------------")

NLTK_stemming_GPU_d2 = [1252.92, 1200.38, 1224.19, 1175.88, 1199.21, 1192.89, 1183.94, 1189.52, 1189.2, 1184.62]
Gensim_stemming_GPU_d2 = [574.54, 588.81, 579.46, 578.35, 584.27, 582.91, 587.02, 562.67, 572.47]

print("ANOVA test for GPU-d2-Stemming")
print(f_oneway(NLTK_stemming_GPU_d2, Gensim_stemming_GPU_d2))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_GPU_d2 = [482.61, 491.02, 502.46, 476.5, 490.56, 481.71, 479.14, 481.26, 484.33, 480.55]
Spacy_lemmatize_GPU_d2 = [35196.43, 37227.7]

print("ANOVA test for GPU-d2-Lemmatize")
print(f_oneway(NLTK_lemmatize_GPU_d2, Spacy_lemmatize_GPU_d2))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_GPU_d2 = [280.31, 356.93, 288.19, 279.56, 283.58, 278.93, 355.68, 277.3, 280.75, 278.12]
Spacy_STOPWORD_GPU_d2 = [39469.3]
Gensim_STOPWORD_GPU_d2 = [129.12, 129.12, 108.45, 107.17, 106.3, 108.55, 105.18, 107.75, 130.13, 131.74]

print("ANOVA test for GPU-d2-STOPWORD")
print(f_oneway(NLTK_STOPWORD_GPU_d2, Spacy_STOPWORD_GPU_d2, Gensim_STOPWORD_GPU_d2))
print("----------------------------------------------------------------------------")

NLTK_POS_GPU_d2 = [16082.83, 16028.47, 16054.08, 15908.88, 15957.07, 16050.78]
Spacy_POS_GPU_d2 = [6734.41, 7860.78, 8113.39, 7733.09, 8037.18, 7840.3, 7982.13, 7809.54]

print("ANOVA test for GPU-d2-POS")
print(f_oneway(NLTK_POS_GPU_d2, Spacy_POS_GPU_d2))
print("----------------------------------------------------------------------------")

NLTK_NER_GPU_d2 = [42741.31, 43647.83, 43064.13, 42599.09]
Spacy_NER_GPU_d2 = [17970.75, 19715.95, 19304.05, 20523.93]

print("ANOVA test for GPU-d2-NER")
print(f_oneway(NLTK_NER_GPU_d2, Spacy_NER_GPU_d2))
print("----------------------------------------------------------------------------")