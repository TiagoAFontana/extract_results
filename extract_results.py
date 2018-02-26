# -*- coding: utf-8 -*-
from extract_miss import *
from extract_runtime import *


def contract_results(path=".", problem="problem1", aux="", miss=True, runtime=True, sequential=True, parallel=True):
    #contract results in one CSV

    fileName = path + "/" + problem + aux + ".csv"

    if miss and sequential:
        dfMissSequential = mean_miss_dataFrame(path , "sequential", problem)
    if miss and parallel:
        dfMissParallel = mean_miss_dataFrame(path , "parallel", problem)
    if runtime and sequential:
        dfRuntimeSequential = mean_runtime_dataFrame(path , "sequential", problem)
    if runtime and parallel:
        dfRuntimeParallel = mean_runtime_dataFrame(path , "parallel", problem)

    if miss and sequential:
        with open(fileName, 'w') as outfile:
            outfile.write('\n')
        dfMissSequential.to_csv(fileName, mode='a')
    if runtime and sequential:
        with open(fileName, 'a') as outfile:
            outfile.write('\n')
        dfRuntimeSequential.to_csv(fileName, mode='a')
    if miss and parallel:
        with open(fileName, 'a') as outfile:
            outfile.write('\n')
        dfMissParallel.to_csv(fileName, mode='a')
    if runtime and parallel:
        with open(fileName, 'a') as outfile:
            outfile.write('\n')
        dfRuntimeParallel.to_csv(fileName, mode='a')

    print("write csv on " + fileName)


def plot_graphic(path=".", problem="problem1"):
    #contract results in one CSV

    dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    dfRuntimeSequential = mean_runtime_dataFrame(path, "sequential", problem)
    dfRuntimeParallel = mean_runtime_dataFrame(path, "parallel", problem)

    dfMissSequential.plot(kind="bar")
    dfMissParallel.plot(kind="bar")
    # dfRuntimeSequential.plot(kind="bar")
    # dfRuntimeParallel.plot(kind="bar")
    plt.show()



# contract_results(os.getcwd()+"/test", "problem2", "_V3_AllCacheMiss", True, False, True, False)
# plot_graphic(os.getcwd(), "problem2")

# contract_results(os.getcwd()+"/test", "problem3", "ttt", True, False, True, False)
# plot_graphic(os.getcwd(), "problem3")
