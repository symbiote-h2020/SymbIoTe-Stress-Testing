import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=1.7, style="whitegrid")
    base_dir = "results/"
    x_label = "Number of Concurrent Requests"
    y_label = "Median Response Times (s)"
    title = "Search Comparison"
    base_filename = "search_comparison"
    y_max = 30.0000000000001
    y_tick = 5
    x_min = 5
    x_max = 50
    x_tick = 5
    linewidth = 4
    reqs = np.arange(x_min, x_max + 1, x_tick)
    times = []

    rap_files = [("100 resource, no auth", "results_SearchTest_10_12_18_factory_registered100_searchByName_false/search_add5_repeat10_byclient_byname_registered_100_false"),
                 ("1000 resource, no auth", "results_SearchTest_10_12_18_factory_registered1000_searchByName_false/search_add5_repeat10_byclient_byname_registered_1000_false"),
                 ("10000 resource, no auth", "results_SearchTest_10_12_18_factory_registered10000_searchByName_false/search_add5_repeat10_byclient_byname_registered_10000_false"),
                 ("100 resource, with auth", "results_SearchTest_10_12_18_factory_registered100_searchByName_true/search_add5_repeat10_byclient_byname_registered_100_true"),
                 ("1000 resource, with auth", "results_SearchTest_10_12_18_factory_registered1000_searchByName_true/search_add5_repeat10_byclient_byname_registered_1000_true"),
                 ("10000 resource, with auth", "results_SearchTest_10_12_18_factory_registered10000_searchByName_true/search_add5_repeat10_byclient_byname_registered_10000_true")
                 ]

    for rap_file in rap_files:
        folder = base_dir + rap_file[1]
        files = os.listdir(folder)
        times_experiment = {}

        for f_name in files:

            try:
                num_req = int(f_name.split('_')[1])
            except IndexError:
                num_req = -1

            if 0 <= num_req <= 100:
                if num_req % 5 != 0:
                    continue

                if num_req not in times_experiment:
                    times_experiment[num_req] = []

                with open(folder + "/" + f_name, 'rb') as f:
                    for line in f.readlines()[:num_req]:
                        times_experiment[num_req].append(int(line.split(' ')[2]) / 1000.0)

        medians = []
        for key in reqs:
            medians.append(np.median(times_experiment[key]))

        times.append(medians)

    print times

    font = {
        'family': 'Liberation Sans',
        'weight': 'normal'
    }

    plt.rc('font', **font)
    plt.yticks(np.arange(0, y_max, y_tick))
    plt.xticks(np.arange(0, x_max, x_tick))
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)
    plt.ylim(ymax=y_max)
    plt.xlim(xmax=x_max)

    for i in np.arange(0, len(times), 1):
        plt.plot(reqs, times[i], "-", lw=linewidth, label=rap_files[i][0])

    plt.legend(['True Positive Ratio'], loc='lower right')
    plt.legend(loc='upper left', prop={'size': 22})

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
