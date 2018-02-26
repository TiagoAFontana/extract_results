# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from decimal import Decimal

def xdistribution(nticks, groupsize, width, spacing, offset=0):
    xticks = []
    positions = []
    grouplength = (width + offset) * groupsize
    for n in range(nticks):
        current = n * (grouplength + spacing) + width/2
        positions += [current + i * (width + offset) for i in range(groupsize)]
        # xticks.append((spacing + grouplength) * n + grouplength / 2 - offset / 2 + width)
        xticks.append(current + (grouplength - offset)/4)
    return positions, xticks

def plot_group_bars(title, labels, x_ticks_labels, group_labels, y_ticks, data, colors, out_path, y_limits='None', target_format="png", bar_width=.75):

	fig, ax = plt.subplots()

	ax.set_title(title, fontsize=18)

	# grid
	ax.set_axisbelow(True) #true = set grid to de end
	ax.grid(color='b', axis='y', linestyle='dashed', linewidth=.2, alpha=.2)

	x_position, x_ticks = xdistribution(len(x_ticks_labels), len(group_labels), bar_width, .75, .05 )

	for i, y_data in enumerate(data, 0):
		# print(y_data)
		# print(len(group_labels))
		# print(x_position[i::len(group_labels)])
		bars = ax.bar(x_position[i::len(group_labels)], y_data, bar_width, color=colors[i],  ecolor='black', alpha=1) #hatch=hatches[i]*4,

	ax.tick_params(axis='x', direction='out', top=False)
	ax.tick_params(axis='y', direction='in', right=False)

	ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
	ax.set_yticks(np.arange(y_ticks[0], y_ticks[2], y_ticks[1]))
	ax.set_xticks(x_ticks)

	ax.set_xlabel(labels[0])
	ax.set_ylabel(labels[1])
	ax.set_xticklabels(x_ticks_labels, rotation=45, horizontalalignment='right')

	if y_limits != 'None':
		ax.set_ylim(y_limits[0], y_limits[1])

	# mean line
	mediaOOD = np.mean(data, axis=1)[0]
	mediaDOD = np.mean(data, axis=1)[1]
	plt.axhline(y=mediaOOD, color=colors[0], linestyle='-.')
	plt.axhline(y=mediaDOD, color=colors[1], linestyle='-.')
	ax.text(1.02, mediaOOD, "{:.2E}".format(Decimal(mediaOOD)), va='center', ha="left", bbox=dict(facecolor="w", alpha=0.5), transform=ax.get_yaxis_transform())
	ax.text(1.02, mediaDOD, "{:.2E}".format(Decimal(mediaDOD)), va='center', ha="left", bbox=dict(facecolor="w", alpha=0.5), transform=ax.get_yaxis_transform())

	# Legend
	patches = []
	for color, grp_label in zip(colors, group_labels):
		patches.append(mpatches.Patch(fill=True, color=color, label=grp_label))
	# mean legend
	patches.append(mlines.Line2D(label=u'Média dos dados', color='black', xdata=[0], ydata=[0], linestyle='-.'))
	# print legend
	ax.legend(handles=patches, fontsize=8, bbox_to_anchor=(.01, 1), loc='upper left', ncol=1)

	# Saving Image
	print('saving at', out_path)
	plt.savefig(out_path+'.'+target_format, format=target_format, bbox_inches='tight')
	plt.clf()
	plt.close('all')

def xtract_2D_data(in_file, sep=','):
	data_file = pd.read_csv(in_file, sep=sep)
	key = data_file.columns[0]
	group_labels = [label for label in data_file.columns[1:]]
	x_ticks_labels = list(data_file[key])
	data = []
	for column in group_labels:
		y_data = (list(data_file[column]))
		data.append(y_data)
	# print(x_ticks_labels)
	# print(group_labels)
	# print(data)
	return x_ticks_labels, group_labels, data

# from _plot_tools import *
# def plots():
# 	_samples = samples +["avg"]
# 	_titles = titles+["Average"]

# 	in_path = r_result_path+result_path+"csv/"
# 	out_path = r_result_path+result_path+"plot/"
# 	if os.path.exists(out_path):
# 		shutil.rmtree(out_path)
# 	os.makedirs(out_path)

# 	colors = []
# 	colors.append((1.0, .0, .0))
# 	colors.append((.0, 1.0, .0))
# 	colors.append((.0, .0, 1.0))
# 	colors.append((.6, .6, .6))
# 	colors.append((.0, .0, .0))

# 	for title, sample in zip(_titles, _samples):
# 		in_file = in_path+sample+".csv"
# 		out_path_file = out_path + title
# 		labels = ["cut level", "operations reduction (%)", "QP"]
# 		x_ticks_labels, group_labels, data = xtract_2D_data(in_file)
# 		y_ticks = [0, 10.0, 101.0] #start, step, end
# 		target_format = 'png'
# 		_data = data[:len(data)-1] #remove average
# 		_group_labels = group_labels[:len(group_labels)-1] #remove average
# 		plot_group_bars(title, labels, x_ticks_labels, _group_labels , y_ticks, _data, colors, out_path_file, target_format)
