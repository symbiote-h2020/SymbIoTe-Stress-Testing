import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=1.5, style="whitegrid")
    base_filename = "semantic_mapping_simple"
    data_size_field = "Multiples of original data size"
    times_field = "Execution Time (ms)"
    title = "Semantic Mapping Simple Scenario"
    show_outliers = False
    ymax = 10.00001
    ytick = 1
    notch = False
    data_size = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    times = [23, 4, 4, 4, 4, 4, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 4, 6, 4, 3,
             3, 3, 3, 2, 3, 4, 4, 4, 4, 3, 3, 3, 3, 4, 3]

    data_frame = pd.DataFrame({data_size_field: data_size, times_field: times})
    response_times_boxplot = pd.melt(data_frame, id_vars=data_size_field, value_name=times_field)

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
    sns.boxplot(x=data_size_field, y=times_field, data=response_times_boxplot, showfliers=show_outliers, notch=notch)
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
