# Energy Measurement Scripts for NLP Preprocessing

### Each script is named following the convention:

`<library_name>_<dataset_name>.py` where:

`library_name` refers to the NLP library used in the script (NLTK, spaCy, or Gensim).
`dataset_name` indicates the dataset on which the preprocessing tasks are performed.

## Overview  
The scripts used in this study measure the **energy consumption and runtime performance** of **NLP preprocessing tasks**,  across **NLTK, spaCy, and Gensim**. Energy usage is captured for both **CPU and GPU** using **Intel RAPL** and **NVIDIA-SMI**, ensuring a comprehensive evaluation of NLP pipeline efficiency.

## Measurement Framework  
Each script follows a structured methodology:
1. **Dataset Loading**: A dataset is loaded into a Pandas DataFrame.
2. **Preprocessing Execution**: NLP preprocessing tasks (tokenization, lemmatization, stemming, stopword removal, POS Tagging and NER) are applied.
3. **Energy Measurement**: The `@measure_energy` decorator from **pyJoules** logs energy consumption in real time.
4. **System Stabilization**: A `sleep()` interval prevents fluctuations in energy readings.
5. **Iterative Processing**: The script runs **10 iterations** for each dataset for stable energy measurements.
6. **Logging and Exporting**: Energy data is stored in a **CSV file** for analysis.

## Script Details  
Each script is tailored for a specific NLP library (**NLTK, spaCy, or Gensim**) but follows the same energy measurement methodology:
- **Tokenization, Lemmatization, Stemming, Stopword Removal Functions, POS Tagging and NER**: Perform preprocessing tasks.
- **Energy Measurement Decorators**: `@measure_energy(handler=csv_handler)` ensures energy consumption tracking.
- **System Stabilization**: `sleep()` prevents carry-over energy effects.
- **Result Storage**: Energy measurements are exported to a **CSV file**.




