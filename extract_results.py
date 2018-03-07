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


def plot_graphic(path=".", problem="problem1"):
    # contract results in one CSV

    dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    dfRuntimeSequential = mean_runtime_dataFrame(path, "sequential", problem)
    dfRuntimeParallel = mean_runtime_dataFrame(path, "parallel", problem)

    dfMissSequential.plot(kind="bar")
    dfMissParallel.plot(kind="bar")
    # dfRuntimeSequential.plot(kind="bar")
    # dfRuntimeParallel.plot(kind="bar")
    plt.show()


# Gerar CSVs Independentes por problema
# contract_results(path=".", problem="problem1", aux="", out_path='.', miss=True, runtime=True, sequential=True, parallel=True):
path = '/home/tiago/experiments16-02/2602'
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

if True:
    # Miss Sequential Problem 2
    contract_results(path, "problem2", "_miss_sequential", out_path, True, False, True, False)
    # Miss Parallel Problem 2
    contract_results(path, "problem2", "_miss_parallel", out_path, True, False, False, True)
    # Runtime Sequential Problem 2
    contract_results(path, "problem2", "_runtime_sequential", out_path, False, True, True, False)
    # Runtime Paralel Problem 2
    contract_results(path, "problem2", "_runtime_parallel", out_path,  False, True, False, True)
    #ORDERED
    # Miss Sequential Problem 2 Ordered
    contract_results(path, "problem2", "_miss_sequential_ordered", out_path, True, False, True, False, "ordered_")
    # Miss Parallel Problem 2 Ordered
    contract_results(path, "problem2", "_miss_parallel_ordered", out_path, True, False, False, True, "ordered_")
    # Runtime Sequential Problem 2 Ordered
    contract_results(path, "problem2", "_runtime_sequential_ordered", out_path, False, True, True, False, "ordered_")
    # Runtime Paralel Problem 2 Ordered
    contract_results(path, "problem2", "_runtime_parallel_ordered", out_path,  False, True, False, True, "ordered_")
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

if True:
    # Miss Sequential Problem 3
    contract_results(path, "problem3", "_miss_sequential", out_path, True, False, True, False)
    # Miss Parallel Problem 3
    contract_results(path, "problem3", "_miss_parallel", out_path, True, False, False, True)
    # Runtime Sequential Problem 3
    contract_results(path, "problem3", "_runtime_sequential", out_path, False, True, True, False)
    # Runtime Paralel Problem 3
    contract_results(path, "problem3", "_runtime_parallel", out_path,  False, True, False, True)

