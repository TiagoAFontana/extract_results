# -*- coding: utf-8 -*-
from plot_tools import plot_group_bars, xtract_2D_data


def plot_miss_graphic(path=".", filename="problem1_py", format="csv"):
    # dfMissSequential = mean_miss_dataFrame(path, "sequential", problem)
    # dfMissParallel = mean_miss_dataFrame(path, "parallel", problem)

    title = filename
    labels = ["Circuito", u'Número de cache misses']
    x_ticks_labels, group_labels, data = xtract_2D_data(
        path+"/"+filename+"."+format)
    y_ticks = [0, 2000000.0, 10000000.0]  # start, step, end

    colors = []
    colors.append((.992, .682, .38))
    colors.append((.168, .513, .729))
    #colors.append((1.0, .0, .0))
    #colors.append((.0, 1.0, .0))
    #colors.append((.0, .0, 1.0))
    #colors.append((.6, .6, .6))
    #colors.append((.0, .0, .0))

    out_path = "./"+filename
    y_limits = 'None'
    target_format = "pdf"
    bar_width = .75
    _data = data[:len(data)]  # remove average
    _group_labels = group_labels[:len(group_labels)]  # remove average

    plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks,
                    data, colors, out_path, y_limits, target_format, bar_width)


# contract_results(os.getcwd(), "problem1", "_py", True, True, True, True)
# plot_graphic(os.getcwd(), "problem1")

plot_miss_graphic()
