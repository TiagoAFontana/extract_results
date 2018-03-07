# -*- coding: utf-8 -*-
from plot_tools import plot_group_bars, xtract_2D_data


def plot_miss_graphic(y_ticks, path_to_csv=".", filename="problem1_py", out_path='.', title="", format="csv"):
    # dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    # dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    labels = ["Circuito", u'Número de cache misses']
    x_ticks_labels, group_labels, data = xtract_2D_data(
        path_to_csv+"/"+filename+"."+format)
    # y_ticks = [0, 2000000.0, 10000000.0]  # start, step, end

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
    
    target_format = "pdf"
    # target_format = "png"
    bar_width = .75
    discartColumns = 2 # remove average
    # _data = data[:len(data)-2]  # remove average
    # _group_labels = group_labels[:len(group_labels)-2]  # remove average


    plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks,
                    data, colors, out_path+"/"+filename, y_limits, target_format, bar_width, discartColumns)





# Gerar CSVs Independentes por problema
# def plot_miss_graphic(path_to_csv=".", filename="problem1_py", out_path='.', title="" format="csv"):
path = '/home/tiago/experiments16-02/2602'
out_path = path + '/graficos'

if True:
    # Miss Sequential Problem 1
    plot_miss_graphic([0, 2000000.0, 10000000.0], path+'/csv', "problem1_miss_sequential", out_path, "Problema 1: Miss Sequential")
    # Miss Parallel Problem 1
    plot_miss_graphic([0, 2000000.0, 10000000.0], path+'/csv', "problem1_miss_parallel", out_path, "Problema 1: Miss Parallel")

if True:
    # Miss Sequential Problem 2
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem2_miss_sequential", out_path, "Problema 2: Miss Sequential")
    # Miss Parallel Problem 2
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem2_miss_parallel", out_path, "Problema 2: Miss Parallel")
    # ORDERED
    # Miss Sequential Problem 2 Ordered
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem2_miss_sequential_ordered", out_path, "Problema 2 (com agrupamento): Miss Sequential")
    # Miss Parallel Problem 2 Ordered
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem2_miss_parallel_ordered", out_path, "Problema 2(com agrupamento): Miss Parallel")
if True:
    # PROPERTY ORDERED
    # Miss Sequential Problem 2 Ordered
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem2_miss_sequential_property_ordered", out_path, "Problema 2 (propGrouped): Miss Sequential")    
    # Miss Parallel Problem 2 Ordered
    plot_miss_graphic([0, 20000000.0, 100000000.0], path+'/csv', "problem2_miss_parallel_property_ordered", out_path, "Problema 2(propGrouped): Miss Parallel")

if True:
    # Miss Sequential Problem 3
    plot_miss_graphic([0, 50000000.0, 350000000.0], path+'/csv', "problem3_miss_sequential", out_path, "Problema 3: Miss Sequential")
    # Miss Parallel Problem 3

    plot_miss_graphic([0, 50000000.0, 350000000.0], path+'/csv', "problem3_miss_parallel", out_path, "Problema 3: Miss Parallel")