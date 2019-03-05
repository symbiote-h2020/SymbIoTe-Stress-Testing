import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=4, style="whitegrid")
    base_dir = "results/"
    component_field = "Component"
    times_field = "Response Time (ms)"
    title = "SMEUR Performance Tests"
    base_filename = "smeur"
    file_format = "eps"
    show_outliers = False
    boxplot_width = 0.25
    ymax = 350
    ytick = 50
    components = []
    times = []

    files = ["rap_smeur.txt", "aam_smeur.txt"]

    for f_name in files:
        comp = ""
        if f_name == "rap_smeur.txt":
            comp = "RAP"
        else:
            comp = "AAM"

        with open(base_dir + "/" + f_name, 'rb') as f:
            for line in f.readlines():
                parts = line.split()
                time = float(parts[0]) * 1000
                occurrences = int(parts[1])

                for i in range(0, occurrences):
                    components.append(comp)
                # times.append(time)
                times.extend(occurrences * [time])

    print(times)
    data_frame = pd.DataFrame({component_field: components, times_field: times})
    response_times_boxplot = pd.melt(data_frame, id_vars=component_field, value_name=times_field)

    font = {
        'family': 'Liberation Sans',
        'weight': 'normal'
    }

    plt.rc('font', **font)
    plt.yticks(np.arange(0, ymax + ytick, ytick))
    plt.ylim(ymax=ymax)
    plt.title(title)

    sns.boxplot(x=component_field, y=times_field, data=response_times_boxplot, showfliers=show_outliers, notch=True, width=boxplot_width)
    # plt.grid(axis='y')
    # plt.grid(axis='x')
    fig = plt.gcf()
    # fig.tight_layout(pad=0.7 * 22 / font_size)
    # fig.tight_layout()
    fig.set_size_inches(20, 14)
    # plt.show()
    plt.savefig(file_format + "/" + base_filename + "." + file_format)
    #


if __name__ == "__main__":
    main()
