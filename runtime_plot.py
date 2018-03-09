# -*- coding: utf-8 -*-
from plot_tools import plot_group_bars, xtract_2D_data


def plot_miss_graphic(y_ticks, path_to_csv=".", filename="problem1_py", out_path='.', title="", format="csv"):
    # dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    # dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    labels = ["Circuito", u'Runtime (us)']
    x_ticks_labels, group_labels, data = xtract_2D_data(
        path_to_csv+"/"+filename+"."+format)
    # y_ticks = [0, 200000.0, 1000000.0]  # start, step, end

    colors = []
    colors.append((.992, .682, .38))
    colors.append((.168, .513, .729))
    #colors.append((1.0, .0, .0))
    #colors.append((.0, 1.0, .0))
    #colors.append((.0, .0, 1.0))
    #colors.append((.6, .6, .6))
    #colors.append((.0, .0, .0))

    # y_limits = 'None'
    y_limits = [y_ticks[0], y_ticks[2]]
    
    # target_format = "pdf"
    # target_format = "svg"
    target_format = "png"
    bar_width = .75
    discartColumns = 2 # remove average

    plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks,
                    data, colors, out_path+"/"+filename, y_limits, target_format, bar_width, discartColumns)





# Gerar CSVs Independentes por problema
# def plot_miss_graphic(path_to_csv=".", filename="problem1_py", out_path='.', title="" format="csv"):
path = '/home/tiago/experiments16-02/0803'
out_path = path + '/graficos'

if True:
    # Runtime Sequential Problem 1
    plot_miss_graphic([0, 200000.0, 1000000.0], path+'/csv', "problem1_runtime_sequential", out_path, "Problema 1: Runtime Sequential")
    # Runtime Parallel Problem 1
    plot_miss_graphic([0, 200000.0, 1000000.0], path+'/csv', "problem1_runtime_parallel", out_path, "Problema 1: Runtime Parallel")

if True:
    # Runtime Sequential Problem 2
    plot_miss_graphic([0, 500000.0, 4000000.0], path+'/csv', "problem2_runtime_sequential", out_path, "Problema 2: Runtime Sequential")
    # Runtime Parallel Problem 2
    plot_miss_graphic([0, 500000.0, 4000000.0], path+'/csv', "problem2_runtime_parallel", out_path, "Problema 2: Runtime Parallel")
    # ORDERED
    # Runtime Sequential Problem 2
    # plot_miss_graphic([0, 500000.0, 4000000.0], path+'/csv', "problem2_runtime_sequential_ordered", out_path, "Problema 2(com agrupamento): Runtime Sequential")
    # Runtime Parallel Problem 2
    # plot_miss_graphic([0, 500000.0, 4000000.0], path+'/csv', "problem2_runtime_parallel_ordered", out_path, "Problema 2(com agrupamento): Runtime Parallel")
if True:
    # PROPERTY ORDERED
    #Runtime Sequential Problem 2
    plot_miss_graphic([0, 500000.0, 4000000.0], path+'/csv', "problem2_runtime_sequential_property_ordered", out_path, "Problema 2(propGrouped): Runtime Sequential")
    # Runtime Parallel Problem 2
    plot_miss_graphic([0, 500000.0, 4000000.0], path+'/csv', "problem2_runtime_parallel_property_ordered", out_path, "Problema 2(propGrouped): Runtime Parallel")

if True:
    # Runtime Sequential Problem 3
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem3_runtime_sequential", out_path, "Problema 3: Runtime Sequential")
    # Runtime Parallel Problem 3
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem3_runtime_parallel", out_path, "Problema 3: Runtime Parallel")