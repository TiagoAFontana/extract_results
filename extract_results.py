# -*- coding: utf-8 -*-
from extract_miss import *
from extract_runtime import *


def contract_results(path=".", problem="problem1", aux="", out_path='.', miss=True, runtime=True, sequential=True, parallel=True, order=""):
    # contract results in one CSV

    fileName = out_path + "/" + problem  + aux + ".csv"

    if miss and sequential:
        dfMissSequential = mean_miss_dataFrame(path, "sequential", problem, ordered=order)
    if miss and parallel:
        dfMissParallel = mean_miss_dataFrame(path, "parallel", problem, ordered=order)
    if runtime and sequential:
        dfRuntimeSequential = mean_runtime_dataFrame(
            path, "sequential", problem, ordered=order)
    if runtime and parallel:
        dfRuntimeParallel = mean_runtime_dataFrame(path, "parallel", problem, ordered=order)

    if miss and sequential:
        dfMissSequential.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')
    if runtime and sequential:
        dfRuntimeSequential.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')
    if miss and parallel:
        dfMissParallel.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')
    if runtime and parallel:
        dfRuntimeParallel.to_csv(fileName, mode='w')
        # with open(fileName, 'a') as outfile:
            # outfile.write('\n')

    print("write csv on " + fileName)

def generateProblemCSV(name_csv="out.csv", csvs_path=".", out_path=".", list_csv=[]):
    # Abre o arquivo redacao.txt para escrita:
    with open(out_path+'/'+name_csv, "w") as file:
        # Percorre a lista de arquivos a serem lidos:
        for temp in list_csv:
            # Abre cada arquivo para leitura:
            with open(csvs_path+'/'+temp, "r") as t:
                # Escreve no arquivo o conteúdo:
                file.writelines(t)
            file.write("\n")
    

# Gerar CSVs Independentes por problema
# contract_results(path=".", problem="problem1", aux="", out_path='.', miss=True, runtime=True, sequential=True, parallel=True):
path = '/home/tiago/experiments16-02/0803'
out_path = path + '/csv'

if True:
    # Miss Sequential Problem 1
    contract_results(path, "problem1", "_miss_sequential", out_path, True, False, True, False)
    # Miss Parallel Problem 1
    contract_results(path, "problem1", "_miss_parallel", out_path, True, False, False, True)
    # Runtime Sequential Problem 1
    contract_results(path, "problem1", "_runtime_sequential", out_path, False, True, True, False)
    # Runtime Paralel Problem 1
    contract_results(path, "problem1", "_runtime_parallel", out_path,  False, True, False, True)
    # Problem1 CSV
    files = ["problem1_miss_sequential.csv", "problem1_runtime_sequential.csv", "problem1_miss_parallel.csv", "problem1_runtime_parallel.csv"]
    generateProblemCSV("Problem1.csv", out_path, out_path, files)

if True:
    # Miss Sequential Problem 2
    contract_results(path, "problem2", "_miss_sequential", out_path, True, False, True, False)
    # Miss Parallel Problem 2
    contract_results(path, "problem2", "_miss_parallel", out_path, True, False, False, True)
    # Runtime Sequential Problem 2
    contract_results(path, "problem2", "_runtime_sequential", out_path, False, True, True, False)
    # Runtime Paralel Problem 2
    contract_results(path, "problem2", "_runtime_parallel", out_path,  False, True, False, True)
if True:
    #PROPERTY ORDERED
    # Miss Sequential Problem 2 Ordered
    contract_results(path, "problem2", "_miss_sequential_property_ordered", out_path, True, False, True, False, "property_ordered_")    
    # Miss Parallel Problem 2 Ordered
    contract_results(path, "problem2", "_miss_parallel_property_ordered", out_path, True, False, False, True, "property_ordered_")    
    # Runtime Sequential Problem 2 Ordered
    contract_results(path, "problem2", "_runtime_sequential_property_ordered", out_path, False, True, True, False, "property_ordered_")
    # Runtime Paralel Problem 2 Ordered
    contract_results(path, "problem2", "_runtime_parallel_property_ordered", out_path,  False, True, False, True, "property_ordered_")
    #ORDERED
    # Miss Sequential Problem 2 Ordered
    # contract_results(path, "problem2", "_miss_sequential_ordered", out_path, True, False, True, False, "ordered_")
    # Miss Parallel Problem 2 Ordered
    # contract_results(path, "problem2", "_miss_parallel_ordered", out_path, True, False, False, True, "ordered_")
    # Runtime Sequential Problem 2 Ordered
    # contract_results(path, "problem2", "_runtime_sequential_ordered", out_path, False, True, True, False, "ordered_")
    # Runtime Paralel Problem 2 Ordered
    # contract_results(path, "problem2", "_runtime_parallel_ordered", out_path,  False, True, False, True, "ordered_")
    
    # Problem2 CSV
    files = ["problem2_miss_sequential.csv", "problem2_runtime_sequential.csv", "problem2_miss_parallel.csv", "problem2_runtime_parallel.csv",
             "problem2_miss_sequential_property_ordered.csv", "problem2_runtime_sequential_property_ordered.csv", "problem2_miss_parallel_property_ordered.csv", "problem2_runtime_parallel_property_ordered.csv"]
    generateProblemCSV("Problem2.csv", out_path, out_path, files)

if True:
    # Miss Sequential Problem 3
    contract_results(path, "problem3", "_miss_sequential", out_path, True, False, True, False)
    # Miss Parallel Problem 3
    contract_results(path, "problem3", "_miss_parallel", out_path, True, False, False, True)
    # Runtime Sequential Problem 3
    contract_results(path, "problem3", "_runtime_sequential", out_path, False, True, True, False)
    # Runtime Paralel Problem 3
    contract_results(path, "problem3", "_runtime_parallel", out_path,  False, True, False, True)
    # Problem3 CSV
    files = ["problem3_miss_sequential.csv", "problem3_runtime_sequential.csv", "problem3_miss_parallel.csv", "problem3_runtime_parallel.csv"]
    generateProblemCSV("Problem3.csv", out_path, out_path, files)
