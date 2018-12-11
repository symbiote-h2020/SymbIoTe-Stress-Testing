import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=1.5, style="whitegrid")
    base_dir = "results/results_SearchTest 10_12_18_factory_registered10000_searchByName_false/search_add5_repeat10_byclient_byname_registered_10000_false"
    num_req_field = "Number of Concurrent Requests"
    times_field = "Response Times (s)"
    title = "Search with 10000 registered resources without 2-way authentication"
    base_filename = "search_stress_test_10_12_10000_false"
    show_outliers = False
    ymax = 40.0000000000001
    ytick = 5
    reqs = []
    times = []

    files = os.listdir(base_dir)

    for f_name in files:
        try:
            num_req = int(f_name.split('_')[1])
        except IndexError:
            num_req = -1

        if 0 <= num_req <= 100:
            if num_req % 5 != 0:
                continue
            with open(base_dir + "/" + f_name, 'rb') as f:
                for line in f.readlines()[:num_req]:
                    reqs.append(num_req)
                    times.append(int(line.split(' ')[2]) / 1000.0)

    data_frame = pd.DataFrame({num_req_field: reqs, times_field: times})
    response_times_boxplot = pd.melt(data_frame, id_vars=num_req_field, value_name=times_field)

    font = {
        'family': 'Liberation Sans',
        'weight': 'normal'
    }

    plt.rc('font', **font)
    plt.yticks(np.arange(0, ymax, ytick))
    # plt.xlabel("x label")
    # plt.ylabel("y label")

    plt.title(title)
    plt.ylim(ymax=ymax)
    # plt.legend(['True Positive Ratio'], loc='lower right')
    # plt.legend(loc='upper right', prop={'size': 40})
    sns.boxplot(x=num_req_field, y=times_field, data=response_times_boxplot, showfliers=show_outliers, notch=True)
    # plt.grid(axis='y')
    # plt.grid(axis='x')
    fig = plt.gcf()
    # fig.tight_layout(pad=0.7 * 22 / font_size)
    fig.tight_layout()
    fig.set_size_inches(10, 7)
    # plt.show()
    plt.savefig("pdf/" + base_filename + ".pdf")
    #


if __name__ == "__main__":
    main()
