# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from decimal import Decimal

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

def plot_group_bars(title, labels, x_ticks_labels, _group_labels, y_ticks, _data, colors, out_path, y_limits='None', target_format="png", bar_width=.75, discartColumns=0):
	group_labels = _group_labels[:len(_group_labels)-discartColumns]
	data = _data[:len(_data)-discartColumns]

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

	#error bar
	height = []
	for ood, dod in zip(_data[0], _data[1]):
		height.append(ood)
		height.append(dod)
	error = []
	for ood, dod in zip(_data[2], _data[3]):
		error.append(ood)
		error.append(dod)
	for pos, y, err in zip(x_position, height, error):
		ax.errorbar(pos, y, err, lw=.5, capsize=2, capthick=.5, color='gray', zorder=5)
		# print error % in relation to bar
		val = err / y * 100
		ax.text(pos, y + 2* err , "{:.2f}".format(val)+ " %" , fontsize=6, rotation=90, va='bottom', ha="center")

	# mean line
	mediaOOD = np.mean(data, axis=1)[0]
	mediaDOD = np.mean(data, axis=1)[1]
	plt.axhline(y=mediaOOD, color=colors[0], linestyle='-.')
	plt.axhline(y=mediaDOD, color=colors[1], linestyle='-.')
	# print mean value on rigth side of chart
	t1 = ax.text(1.02, mediaOOD, "{:.2E}".format(Decimal(mediaOOD)), va='center', ha="left", bbox=dict(facecolor="w", alpha=0.5), transform=ax.get_yaxis_transform())
	t2 = ax.text(1.02, mediaDOD, "{:.2E}".format(Decimal(mediaDOD)), va='center', ha="left", bbox=dict(facecolor="w", alpha=0.5), transform=ax.get_yaxis_transform())
	# print the percentage of redution
	tt = ax.text(1.02, ((mediaOOD+mediaDOD)/2), str(round(((1-(mediaDOD/mediaOOD))*100), 2)) + " %", va='center', ha="left", transform=ax.get_yaxis_transform() )
	
	# mean arrow

	# bbox_props = dict(boxstyle="darrow,pad=0.4", fc="w", ec="black", lw=1)
	# ax.text(1.08, (mediaOOD+mediaDOD)/2, str(round(((1-(mediaDOD/mediaOOD))*100), 2)) + " %", ha="center", va="center", rotation=90,size=10, bbox=bbox_props, transform=ax.get_yaxis_transform())

	# ax.arrow( 3000000, 3000000, 3000000, -3000000, fc="k", ec="k", head_width=0.05, head_length=0.1 )
	# plt.axvline(x=25, color=colors[0], linestyle='-.', clip_box=[[1, mediaDOD], [2, mediaOOD]])
	# ax.add_line(mlines.Line2D(label=u'Média dos dados', color='black', xdata=[0], ydata=[0], linestyle='-.'))
	# line = plt.Line2D(t1, t2, transform=ax.get_xaxis_transform(), color='black')
	# line.set_clip_on(True)
	# ax.add_line(line)

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