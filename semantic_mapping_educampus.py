import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=1.5, style="whitegrid")
    base_filename = "semantic_mapping_educampus"
    data_size_field = "Multiples of original data size"
    times_field = "Execution Time (ms)"
    title = "Semantic Mapping EduCampus Scenario"
    show_outliers = False
    ymax = 250.00001
    ytick = 50
    notch = False
    data_size = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    times = [46, 18, 13, 12, 10, 10, 9, 9, 8, 7, 25, 22, 20, 20, 22, 20, 19, 17, 17, 16, 33, 36, 31, 31, 30, 28, 29, 28,
             23, 25, 108, 105, 104, 105, 98, 114, 103, 109, 102, 109, 212, 215, 214, 217, 215, 219, 219, 235, 232, 242]

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
