# NLP Libraries Energy Consumption and Run-time Study

## Overview
This repository contains the code and data for an empirical study comparing the energy consumption and run-time performance of three popular Natural Language Processing (NLP) libraries: NLTK, spaCy, and Gensim.

## Objective
The objective of this study is to evaluate the energy efficiency and computational performance of these NLP libraries under various test conditions.

## Data
The data used in this study includes:

- 3 text datasets for processing by each library.
    - Fake and real news dataset
    - Drug Review dataset
    - Online Retail II dataset
- Energy consumption measurements using the Intel-RAPL.
- Run-time performance metrics recorded during execution.

## Methodology
The study follows a systematic approach:

1. Selection of NLP libraries: NLTK, Space, and Genesis.
2. Design of test scenarios covering common NLP tasks.
3. Execution of experiments on a standardized hardware platform.
4. Measurement of energy consumption using DBJoules.
5. Recording of run-time performance metrics.
6. Analysis of results and comparison of energy efficiency and run-time performance across libraries.

## Repository Structure
- `Raw_Output/`: Contains raw measurement data.
- `Scripts/`: Includes scripts for running experiments and collecting data.
- `Results/`: Contains analysis results and visualizations.
- `Statistical Analysis/`: Contains statistical analysis scripts.
- `README.md`: This file, providing an overview of the study.

## Usage
To reproduce the experiments or analyze the results:
1. Clone this repository to your local machine.
2. Navigate to the appropriate directory (`scripts/` for running experiments or `results/` for analysis).


## Results and Discussion
The results of the study are summarized in the `Results/` directory. Detailed analysis and discussion of the findings are provided in the accompanying paper.




