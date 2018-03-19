# -*- coding: utf-8 -*-
from plot_tools import plot_group_bars, xtract_2D_data


def plot_miss_graphic(y_ticks, path_to_csv=".", filename="problem1_py", out_path='.', title="", format="csv", scale='linear', discartColumns=6):
    # dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    # dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    labels = ["Circuito", u'Número de cache misses']
    x_ticks_labels, group_labels, data, unit = xtract_2D_data(
        path_to_csv+"/"+filename+"."+format)
    # y_ticks = [0, 2000000.0, 10000000.0]  # start, step, end

    colors = []
    colors.append((.992, .682, .38))
    colors.append((.168, .513, .729))
    colors.append((1.0, .0, .0))
    colors.append((.0, 1.0, .0))
    colors.append((.0, .0, 1.0))
    colors.append((.6, .6, .6))
    colors.append((.0, .0, .0))
    colors.append((1.0, .0, 1.0))
    colors.append((1.0, 1.0, 1.0))
    colors.append((.5, .5, .5))


    # y_limits = 'None'
    y_limits = [y_ticks[0], y_ticks[2]]
    
    target_format = "pdf"
    # target_format = "svg"
    # target_format = "png"
    bar_width = .75
    # discartColumns = 6 # remove average
    # _data = data[:len(data)-2]  # remove average
    # _group_labels = group_labels[:len(group_labels)-2]  # remove average


    plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks,
                    data, colors, out_path+"/"+filename, y_limits, target_format, bar_width, discartColumns, scale=scale)





# Gerar CSVs Independentes por problema
# def plot_miss_graphic(path_to_csv=".", filename="problem1_py", out_path='.', title="" format="csv"):
# path = '/home/tiago/experiments16-02/0803'
path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O3/miss_O3'
# path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O0'
out_path = path + '/graficos'

#------------------#
problem1 = False 
problem2 = False
grouped = False
problem3 = False
#------------------#
compilacao = 'O0'

if problem1:
    scaleLimits = [0, 2000000.0, 12000000.0] if compilacao == 'O0' else [0, 20000000.0, 100000000.0]
    scale = 'linear' if compilacao == 'O0' else 'symlog'
    # Miss Sequential Problem 1
    plot_miss_graphic(scaleLimits, path+'/csv', "problem1_miss_sequential", out_path, "Problema 1: Miss Sequential", scale=scale)
    # Miss Parallel Problem 1
    plot_miss_graphic(scaleLimits, path+'/csv', "problem1_miss_parallel", out_path, "Problema 1: Miss Parallel", scale=scale)

if problem2:
    scaleLimits = [0, 20000000.0, 90000000.0] if compilacao == 'O0' else [0, 20000000.0, 100000000.0]
    # Miss Sequential Problem 2
    plot_miss_graphic(scaleLimits, path+'/csv', "problem2_miss_sequential", out_path, "Problema 2: Miss Sequential")
    # Miss Parallel Problem 2
    plot_miss_graphic(scaleLimits, path+'/csv', "problem2_miss_parallel", out_path, "Problema 2: Miss Parallel")
    # ORDERED
    # Miss Sequential Problem 2 Ordered
    # plot_miss_graphic(scaleLimits, path+'/csv', "problem2_miss_sequential_ordered", out_path, "Problema 2 (com agrupamento): Miss Sequential")
    # Miss Parallel Problem 2 Ordered
    # plot_miss_graphic(scaleLimits, path+'/csv', "problem2_miss_parallel_ordered", out_path, "Problema 2(com agrupamento): Miss Parallel")
    if grouped:
        # PROPERTY ORDERED
        # Miss Sequential Problem 2 Ordered
        plot_miss_graphic(scaleLimits, path+'/csv', "problem2_miss_sequential_property_ordered", out_path, "Problema 2 (propGrouped): Miss Sequential")    
        # Miss Parallel Problem 2 Ordered
        plot_miss_graphic(scaleLimits, path+'/csv', "problem2_miss_parallel_property_ordered", out_path, "Problema 2(propGrouped): Miss Parallel")

if problem3:
    scaleLimits = [0, 50000000.0, 350000000.0] if compilacao == 'O0' else [0, 50000000.0, 350000000.0]
    # Miss Sequential Problem 3
    plot_miss_graphic(scaleLimits, path+'/csv', "problem3_miss_sequential", out_path, "Problema 3: Miss Sequential")
    # Miss Parallel Problem 3
    plot_miss_graphic(scaleLimits, path+'/csv', "problem3_miss_parallel", out_path, "Problema 3: Miss Parallel")



scaleLimits = [0, 50000000.0, 350000000.0] if compilacao == 'O0' else [0, 50000000.0, 350000000.0]
path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O0/problem3_size'
out_path = path + '/graficos'
plot_miss_graphic(scaleLimits, path+'/csv', "problem3_miss_sequential", out_path, "Problema 3: Miss Sequential", discartColumns=20)
plot_miss_graphic(scaleLimits, path+'/csv', "problem3_miss_parallel", out_path, "Problema 3: Miss Parallel", discartColumns=20)