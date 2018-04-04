# -*- coding: utf-8 -*-
from plot_tools import plot_group_bars, xtract_2D_data


def plot_miss_graphic(y_ticks, path_to_csv=".", filename="problem1_py", out_path='.', title="", format="csv", scale='linear', discartColumns=6):
    # dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    # dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    
    x_ticks_labels, group_labels, data, unit = xtract_2D_data(
        path_to_csv+"/"+filename+"."+format)
    # y_ticks = [0, 200000.0, 1000000.0]  # start, step, end
    labels = ["Circuito", u'Runtime ('+unit+')']

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

    plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks,
                    data, colors, out_path+"/"+filename, y_limits, target_format, bar_width, discartColumns, scale=scale)





# Gerar CSVs Independentes por problema
# def plot_miss_graphic(path_to_csv=".", filename="problem1_py", out_path='.', title="" format="csv"):
# path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O0'
path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O3'
# path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O3/runtime_03'
out_path = path + '/graficos'

#------------------#
problem1 = True
problem2 = True
grouped = True
problem3 = True
extraSize = True
problem4 = True
#------------------#
compilacao = 'O3'

if problem1:
    scaleLimits = [0, 200000.0, 1000000.0] if compilacao == 'O0' else [0, 200000000.0, 1500000000.0]
    scale = 'linear' if compilacao == 'O0' else 'symlog'
    # Runtime Sequential Problem 1
    plot_miss_graphic(scaleLimits, path+'/csv', "problem1_runtime_sequential", out_path, "P1: Runtime Sequential", scale=scale)
    # Runtime Parallel Problem 1
    plot_miss_graphic(scaleLimits, path+'/csv', "problem1_runtime_parallel", out_path, "P1: Runtime Parallel", scale=scale)

if problem2:
    scaleLimits = [0, 500000.0, 4000000.0] if compilacao == 'O0' else [0, 200000000.0, 1000000000.0]
    # Runtime Sequential Problem 2
    plot_miss_graphic(scaleLimits, path+'/csv', "problem2_runtime_sequential", out_path, "P2: Runtime Sequential")
    # Runtime Parallel Problem 2
    plot_miss_graphic(scaleLimits, path+'/csv', "problem2_runtime_parallel", out_path, "P2: Runtime Parallel")
    # ORDERED
    # Runtime Sequential Problem 2
    # plot_miss_graphic(scaleLimits, path+'/csv', "problem2_runtime_sequential_ordered", out_path, "P2(com agrupamento): Runtime Sequential")
    # Runtime Parallel Problem 2
    # plot_miss_graphic(scaleLimits, path+'/csv', "problem2_runtime_parallel_ordered", out_path, "P2(com agrupamento): Runtime Parallel")
    if grouped:
        # PROPERTY ORDERED
        #Runtime Sequential Problem 2
        plot_miss_graphic(scaleLimits, path+'/csv', "problem2_runtime_sequential_property_ordered", out_path, "P2: Runtime Sequential (agrupado)")
        # Runtime Parallel Problem 2
        plot_miss_graphic(scaleLimits, path+'/csv', "problem2_runtime_parallel_property_ordered", out_path, "P2: Runtime Parallel (agrupado)")

if problem3:
    scaleLimits = [0, 12000000.0, 60000000.0] if compilacao == 'O0' else [0, 560000000.0, 2800000000.0]
    # Runtime Sequential Problem 3
    plot_miss_graphic(scaleLimits, path+'/csv', "problem3_runtime_sequential", out_path, "P3: Runtime Sequential")
    # Runtime Parallel Problem 3
    plot_miss_graphic(scaleLimits, path+'/csv', "problem3_runtime_parallel", out_path, "P3: Runtime Parallel")
    if extraSize:
        # scaleLimits = [0, 50000000.0, 350000000.0] if compilacao == 'O0' else [0, 50000000.0, 350000000.0]
        # path = '/home/tiago/Dropbox/mestrado/experiments/0309_cold_cache_o0_30/O0/problem3_size'
        # out_path = path + '/graficos'
        plot_miss_graphic(scaleLimits, path+'/csv', "problem3_runtime_sequential_extraSize", out_path, "Problema 3: Miss Sequential", discartColumns=18)
        plot_miss_graphic(scaleLimits, path+'/csv', "problem3_runtime_parallel_extraSize", out_path, "Problema 3: Miss Parallel", discartColumns=18)

if problem4:
    scaleLimits = [0, 66000000000.0, 330000000000.0] if compilacao == 'O0' else [0, 8400000000.0, 42000000000.0]
    # Runtime Sequential Problem 3
    plot_miss_graphic(scaleLimits, path+'/csv', "problem4_runtime_sequential", out_path, "P4: Runtime Sequential")
