from scipy.stats import spearmanr
import csv

def read_csv_column(csv_file, column_index,data_type=float):
    column_data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) > column_index:
                column_data.append(data_type(row[column_index]))
    return column_data


csv_files = ['/Users/rajrupachattaraj/Documents/ICSME_NLP/Results/Gensim_D1.csv','/Users/rajrupachattaraj/Documents/ICSME_NLP/Results/Gensim_D2.csv','/Users/rajrupachattaraj/Documents/ICSME_NLP/Results/Spacy_D3.csv'] # Replace 'example.csv' with your CSV file path
column_index1= 2 #for time
column_index2 = 9  #for cpu
column_index3 = 10  #for cpu

# def read_multiple_csv_files(csv_files, column_index):
#     all_column_data = []
#     for file in csv_files:
#         #column_data = read_csv_column(file, column_index)
#         time_data = read_csv_column(file, column_index1)
#         cpu_energy= read_csv_column(file, column_index2)
#         gpu_energy= read_csv_column(file, column_index3)
#         all_column_data.extend(time_data)
#     return all_column_data

for csv_file in csv_files:

    time_data = read_csv_column(csv_file, column_index1)
    cpu_energy= read_csv_column(csv_file, column_index2)
    gpu_energy= read_csv_column(csv_file, column_index3)
    # # calculate Spearman's correlation coefficient and p-value
    corr_cpu, pval_cpu = spearmanr(time_data, cpu_energy)
    corr_gpu, pval_gpu = spearmanr(time_data, gpu_energy)
 
    # print the result
    print("Correlation coefficient CPU:", corr_cpu)
    print("Correlation coefficient GPU:", corr_gpu)
    print("p-value CPU:", pval_cpu)
    print("p-value GPU:", pval_gpu)