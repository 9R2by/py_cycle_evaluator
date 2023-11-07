import os

from matplotlib import pyplot as plt


def plot_graph(file_names, file_path_output, plot_name="combined_plot"):
    # List of file names
    # file_names = ["file1.txt", "file2.txt", "file3.txt"]

    print("PPPPPPPPLLLLLLLLOOOOOOOOOOOOOT\nGRAAAAAAAAAAPPPPHHHHHHH")
    print(file_names, file_path_output, plot_name)
    plt.figure()
    # Iterate through each file and create a plot
    for file_name in file_names:
        with open(file_name, "r") as file:
            data = [int(line.strip()) for line in file]

        plt.plot(data, label=f"{os.path.basename(file_name)}")
        plt.title(f"Cycle comparison: {plot_name}")
        plt.xlabel("n")
        plt.ylabel("Cycles")
        plt.grid(True)
        plt.legend()

        # Show all the plots
        # plt.show()
    plt.savefig(file_path_output + plot_name + ".svg", format="svg")

    boxplot = []
    if plot_name == "combined_plot":
        plt.figure()
        for file_name in file_names:
            with open(file_name, "r") as file:
                data = ([int(line.strip()) for line in file])
                print(data)
            boxplot.append(data)
        plt.boxplot(data)
        # Show all the plots
        # plt.show()
        plt.title(f"Cycle comparison: {plot_name}")
        plt.xlabel("n")
        plt.ylabel("Cycles")
        plt.grid(True)
        plt.legend()
        # plt.show()
        plt.savefig(file_path_output + "boxplot" + ".svg", format="svg")
