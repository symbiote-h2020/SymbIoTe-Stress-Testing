import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=1.7, style="whitegrid")
    x_label = "Number of Concurrent Requests"
    y_label = "CPU Utilization (\%)"
    title = "Access Requests"

    base_dir = "results_resource_usage/"
    base_filename = "raptests_cpu"
    y_min = 0
    y_tick = None
    x_min = 5
    x_max = 50
    x_tick = 5
    linewidth = 3
    reqs = np.arange(x_min, x_max + 1, x_tick)

    rap_files = [("AAM without server authentication", base_dir+"aam_cpu_raptests_false"),
                 ("AAM with server authentication", base_dir+"aam_cpu_raptests_true"),
                 ("RAP without server authentication", base_dir+"rap_cpu_raptests_false"),
                 ("RAP with server authentication", base_dir+"rap_cpu_raptests_true")]

 
    
    font = {
        'family': 'Liberation Sans',
        'weight': 'normal'
    }

    xmin = 0
    y_max = 100

    plt.ylim(ymax=y_max)
    plt.ylim(ymin=0)
    plt.rc('font', **font)
    #plt.yticks(np.arange(0, y_max, y_tick))
    plt.xticks(np.arange(0, x_max+5, x_tick))
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)
    plt.xlim(xmin=0)
    plt.xlim(xmax=x_max+5)

    mem_max = 0 
    for file in rap_files:
        f_name = file[1]
   
        cpu_usage = []
        with open(f_name,'r') as f:
             for line in f.readlines():
                 r_x = line.split("\t")[0]
                 cpu = line.split("\t")[1]
                 cpu_usage.append(float(cpu))
	cpu_max = max(cpu_usage)
        y_max = max(y_max, cpu_max)
        plt.ylim(ymax=1.3*y_max)
        plt.plot(reqs, cpu_usage, marker='o', label=file[0])

    plt.legend(['True Positive Ratio'], loc='lower right', framealpha=0.1)
    plt.legend(loc='upper left', prop={'size': 15})
    plt.legend(fancybox=True)

    # plt.grid(axis='y')
    # plt.grid(axis='x')
    fig = plt.gcf()
    # fig.tight_layout(pad=0.7 * 22 / font_size)
    fig.tight_layout()
    fig.set_size_inches(10, 7)
    # plt.show()
    plt.savefig("eps/" + base_filename + ".eps")
    #


if __name__ == "__main__":
    main()
