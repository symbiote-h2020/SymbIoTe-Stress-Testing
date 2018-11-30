import os

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
	matplotlib.rcParams['text.usetex'] = True
	sns.set(font_scale=5)
	sns.set(style="whitegrid")
	base_dir = "results/testRAP_29_2_18/exp_rap_false_AllData/exp_rap_false"
	num_req_field = "Number of Requests"
	times_field = "Response Times (ms)"
	show_outliers = False
	reqs = []
	times = []

	files = os.listdir(base_dir)

	for f_name in files:
		try:
			num_req = int(f_name.split('_')[1])
		except IndexError:
			num_req = -1

		if 0 <= num_req < 100:
			if num_req % 5 != 0:
				continue
			with open(base_dir + "/" + f_name, 'rb') as f:
				for line in f.readlines()[:num_req]:
					reqs.append(num_req)
					times.append(int(line.split(' ')[2]))

	data_frame = pd.DataFrame({num_req_field: reqs, times_field: times})
	response_times_boxplot = pd.melt(data_frame, id_vars=num_req_field, value_name=times_field)

	font = {
		'family': 'Liberation Sans',
		'weight': 'normal',
		'size': 22
	}

	plt.rc('font', **font)
	# plt.xlabel("x label")
	# plt.ylabel("y label")

	plt.title("Stress Test")
	# plt.ylim(ym)
	# plt.legend(['True Positive Ratio'], loc='lower right')
	# plt.legend(loc='upper right', prop={'size': 40})
	sns.boxplot(x=num_req_field, y=times_field, data=response_times_boxplot, showfliers=show_outliers)
	# plt.grid(axis='y')
	# plt.grid(axis='x')
	fig = plt.gcf()
	fig.tight_layout()
	fig.set_size_inches(10, 7)
	# plt.savefig(base_filename + ".eps")
	#
	plt.show()


if __name__ == "__main__":
	main()
