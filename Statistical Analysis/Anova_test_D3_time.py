from scipy.stats import f_oneway

NLTK_tokenization_time_d3 = [29.07777834, 29.0322001, 26.97786307, 26.82215738, 26.89895082]
Spacy_tokenization_time_d3 = [2269.649424]
Gensim_tokenization_time_d3 = [2.27701807, 2.585670471, 1.919152975, 1.951876879, 1.91710639, 1.935140371, 1.919406414, 1.918698311, 2.676758051, 2.670757532]

print("ANOVA test for Time-d3-Tokenization")
print(f_oneway(NLTK_tokenization_time_d3, Spacy_tokenization_time_d3, Gensim_tokenization_time_d3))
print("----------------------------------------------------------------------------")

NLTK_stemming_time_d3 = [18.59130812, 18.60119319, 18.67294455, 18.59022784, 20.79216909]
Gensim_stemming_time_d3 = [9.223056555, 9.538462877, 9.562011957, 9.518354654, 9.481669188, 9.491172791, 9.488211393, 8.750970125, 8.74625802]

print("ANOVA test for Time-d3-Stemming")
print(f_oneway(NLTK_stemming_time_d3, Gensim_stemming_time_d3))
print("----------------------------------------------------------------------------")

NLTK_lemmatize_time_d3 = [7.66656065, 7.591208458, 5.490649223, 5.451028109, 5.508652449, 5.50701189, 5.526708364]
Spacy_lemmatize_time_d3 = [2273.414853, 2313.398797]

print("ANOVA test for Time-d3-Lemmatize")
print(f_oneway(NLTK_lemmatize_time_d3, Spacy_lemmatize_time_d3))
print("----------------------------------------------------------------------------")

NLTK_STOPWORD_time_d3 = [6.158387184, 6.266943455, 6.267998934, 6.222388744, 4.119571686]
Spacy_STOPWORD_time_d3 = [2349.016348]
Gensim_STOPWORD_time_d3 = [2.234417439, 2.302556515, 2.259038687, 2.276105404, 2.265676737, 2.271717548, 2.249631405, 2.234736443, 2.295969248, 2.231498003]

print("ANOVA test for Time-d3-STOPWORD")
print(f_oneway(NLTK_STOPWORD_time_d3, Spacy_STOPWORD_time_d3, Gensim_STOPWORD_time_d3))
print("----------------------------------------------------------------------------")

NLTK_POS_time_d3 = [329.8378415, 331.4202051, 330.72837, 329.0701251, 329.3176975]
Spacy_POS_time_d3 = [230.337096, 288.3734117, 272.2212787, 302.7525642, 304.7660506, 293.9706922, 308.9124739, 309.2203462]

print("ANOVA test for Time-d3-POS")
print(f_oneway(NLTK_POS_time_d3, Spacy_POS_time_d3))
print("----------------------------------------------------------------------------")

NLTK_NER_time_d3 = [733.8986366, 719.9152999, 720.3283937, 723.5692542, 723.6125817, 723.3160825, 722.8182507]
Spacy_NER_time_d3 = [2261.813757]

print("ANOVA test for Time-d3-NER")
print(f_oneway(NLTK_NER_time_d3, Spacy_NER_time_d3))
print("----------------------------------------------------------------------------")