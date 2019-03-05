import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


def main():
    matplotlib.rcParams['text.usetex'] = True
    sns.set(font_scale=4, style="whitegrid")
    x_label = "Number of resources registered concurrently"
    y_label = "Response Time (ms)"
    title = "Smart Home Registration Tests"
    base_filename = "smart_home_registration"
    file_format = 'eps'
    y_min = 300
    y_max = 600
    x_min = 10
    x_max = 10000
    linewidth = 6

    resources = [20, 50, 100, 200, 500, 1000, 5000]
    times = [7, 18, 37, 73, 192, 405, 2873]
    times_per_resource = [times[i] / resources[i] * 1000 for i in range(0, len(resources))]

    print(times_per_resource)

    font = {
        'family': 'Liberation Sans',
        'weight': 'normal'
    }

    plt.rc('font', **font)
    # exp = int(math.log10(y_max))
    # majors = [10 ** x for x in range(exp + 1)]
    # majors = [10**n for n in range(len(str(max(y))))]
    # plt.yticks(np.arange(3), [10, 100, 1000])
    plt.xticks([10, 100, 1000, 10000])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(b=True, which='minor', color='0.65', linestyle='-')

    plt.title(title)

    plt.plot(resources, times_per_resource, "-", lw=linewidth, marker='o')

    # plt.grid(axis='y')
    # plt.grid(axis='x')
    # ax.xaxis.grid(False)
    fig = plt.gcf()
    ax = plt.gca()
    ax.set_xscale("log")
    ax.set_ylim(bottom=y_min, top=y_max)
    ax.set_xlim(left=x_min, right=x_max)
    ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.xaxis.get_major_formatter().set_scientific(False)
    ax.xaxis.set_major_locator(mticker.LogLocator())
    ax.xaxis.set_minor_locator(mticker.LogLocator(base=10.0, subs=(0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)))
    ax.tick_params(axis='x', which='minor', bottom=True, grid_linewidth=0.1)
    # ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

    # fig.tight_layout(pad=0.7 * 22 / font_size)
    # fig.tight_layout()
    fig.set_size_inches(20, 14)
    # plt.show()
    plt.savefig(file_format + "/" + base_filename + "." + file_format)
    #


if __name__ == "__main__":
    main()
