import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=4, style="whitegrid")
    x_label = "Data Size (in multiple of original size)"
    y_label = "Median Execution Time (ms)"
    title = "Data Transformation Performance"
    base_filename = "semantic_mapping_comparison"
    file_format = "eps"
    labels = ["Simple Scenario", "EduCampus Scenario"]
    y_max = 1000
    x_min = 0
    x_max = 4
    linewidth = 6

    simple = [23, 4, 4, 4, 4, 4, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 4, 6, 4, 3,
              3, 3, 3, 2, 3, 4, 4, 4, 4, 3, 3, 3, 3, 4, 3]
    educampus = [46, 18, 13, 12, 10, 10, 9, 9, 8, 7, 25, 22, 20, 20, 22, 20, 19, 17, 17, 16, 33, 36, 31, 31, 30, 28, 29,
                 28, 23, 25, 108, 105, 104, 105, 98, 114, 103, 109, 102, 109, 212, 215, 214, 217, 215, 219, 219, 235, 232, 242]
    data_size = [1, 5, 10, 50, 100]
    medians_simple = []
    medians_educampus = []
    reqs = [medians_simple, medians_educampus]

    for i in range(0, 50, 10):
        medians_simple.append(np.median(simple[i:i+10]))
        medians_educampus.append(np.median(educampus[i:i+10]))

    font = {
        'family': 'Liberation Sans',
        'weight': 'normal'
    }

    print(reqs)

    plt.rc('font', **font)
    # exp = int(math.log10(y_max))
    # majors = [10 ** x for x in range(exp + 1)]
    # majors = [10**n for n in range(len(str(max(y))))]
    # plt.yticks(np.arange(3), [10, 100, 1000])
    plt.xticks(np.arange(len(data_size)), data_size)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)

    for i in np.arange(0, len(reqs), 1):
        plt.plot(np.arange(len(data_size)), reqs[i], "-", lw=linewidth, label=labels[i], marker='o')

    plt.legend(['True Positive Ratio'], loc='lower right')
    plt.legend(loc='upper left', prop={'size': 38})

    plt.grid(True, axis='y', which='both')
    # plt.grid(axis='x')
    fig = plt.gcf()
    ax = plt.gca()
    ax.set_yscale("log")
    ax.set_ylim(top=y_max)
    ax.set_xlim(left=x_min, right=x_max)
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.yaxis.get_major_formatter().set_scientific(False)
    ax.yaxis.set_minor_locator(mticker.LogLocator(base=10.0, subs=(0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)))
    ax.tick_params(axis='y', which='minor', left=True, grid_linewidth=0.1)
    ax.tick_params(axis='x', which='minor', bottom=True, grid_linewidth=0.1)

    # ax.set_xticks(data_size)
    # fig.tight_layout(pad=0.7 * 22 / font_size)
    # fig.tight_layout()
    fig.set_size_inches(20, 14)
    # plt.show()
    plt.savefig(file_format + "/" + base_filename + "." + file_format)
    #


if __name__ == "__main__":
    main()
