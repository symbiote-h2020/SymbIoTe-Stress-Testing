import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=1.7, style="whitegrid")
    x_label = "Number of Concurrent Requests"
    y_label = "memory Util (\%)"
    title = "Access Requests"

    base_dir = "results_resource_usage/"
    base_filename = "searchtests_memory_search_for_aam"
    y_min = 0
    y_tick = None
    x_min = 5
    x_max = 50
    x_tick = 5
    linewidth = 3
    reqs = np.arange(x_min, x_max + 1, x_tick)

    files = [("coreAAM 100 - without server authentication", base_dir+"coreaam_memory_searchtests_false_100"),
                 ("coreAAM 1000 - without server authentication", base_dir+"coreaam_memory_searchtests_false_1000"),
                 ("coreAAM 10000 - without server authentication", base_dir+"coreaam_memory_searchtests_false_10000"),
                 ("coreAAM 100 - with server authentication", base_dir+"coreaam_memory_searchtests_true_100"),
                 ("coreAAM 1000 - with server authentication", base_dir+"coreaam_memory_searchtests_true_1000"),
                 ("coreAAM 10000 - with server authentication", base_dir+"coreaam_memory_searchtests_true_10000")]

 

    
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
    for file in files:
        f_name = file[1]
   
        memory_usage = []
        with open(f_name,'r') as f:
             for line in f.readlines():
                 r_x = line.split("\t")[0]
                 memory = line.split("\t")[1]
                 memory_usage.append(float(memory))
	memory_max = max(memory_usage)
        y_max = max(y_max, memory_max)
        plt.ylim(ymax=2.2*y_max)
        plt.plot(reqs, memory_usage, marker='o', label=file[0])

    plt.legend(['True Positive Ratio'], shadow=False)
    plt.legend(loc='upper left', prop={'size': 15})
  #  plt.legend(fancybox=True, framealpha=0.3, bbox_to_anchor=(0, 0))

    plt.legend(framealpha=0.2)
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
