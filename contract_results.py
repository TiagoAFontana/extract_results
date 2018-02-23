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

from plot import plot_group_bars, xtract_2D_data
def plot_miss_graphic(path=".", filename="problem1_py.csv"):
    # dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    # dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    title="test"
    labels=["circuit", "# misses"]
    x_ticks_labels, group_labels, data = xtract_2D_data(path+"/"+filename)
    y_ticks  = [0, 1000000.0, 10000000.0]

    colors = []
    colors.append((1.0, .0, .0))
    colors.append((.0, 1.0, .0))
    colors.append((.0, .0, 1.0))
    colors.append((.6, .6, .6))
    colors.append((.0, .0, .0))

    out_path="./test"
    y_limits='None'
    target_format="pdf"
    bar_width=.75
    _data = data[:len(data)] #remove average
    _group_labels = group_labels[:len(group_labels)] #remove average

    plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks, data, colors, out_path, y_limits, target_format, bar_width)


# contract_results(os.getcwd(), "problem1", "_py", True, True, True, True)
# plot_graphic(os.getcwd(), "problem1")

plot_miss_graphic()

# contract_results(os.getcwd()+"/test", "problem2", "_V3_AllCacheMiss", True, False, True, False)
# plot_graphic(os.getcwd(), "problem2")

# contract_results(os.getcwd()+"/test", "problem3", "ttt", True, False, True, False)
# plot_graphic(os.getcwd(), "problem3")
