import datetime
import os
import time

from tqdm import tqdm

import call_with_random_values as cwrv
import evaluate_file_multiple_columns as mc
import evaluate_file_single_column as sc
import get_file_list as gfl
import plot_graph as pg


# if commandline arguments are given that indicate automated testing:
# TODO: this part of the code is the furthest developed. Others need adaption to this part!
# TODO: also the file evaluation of so is further than mo
# this is due to this functions beeing more important
# eventually remove other parts?
def automated_tests(file_path, mode_set, modes, executable_path, exponent, number_of_files, file_path_output,
                    median_filtered_folder):
    print("Starting automated tests. This might take some time.\n")
    start_time = time.time()
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d-%H-%M-%S.%f")[:-3]
    filename = "Run-" + date + "-summary"
    n = pow(2, exponent)
    for _ in range(number_of_files):
        path = executable_path[_]
        # debugging
        # print(path)
        print('n=' + str(n))
        print('File: ' + str(os.path.basename(path)))
        for _ in tqdm(range(n + 1), desc="Loading", unit="item"):
            print("YEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            print(os.path.basename(path), file_path_output, path)
            cwrv.call_with_random_values(os.path.basename(path), file_path_output, path)

        if mode_set == modes[0]:
            print(os.path.basename(path), file_path, file_path_output)
            mc.evaluate_file_mo(os.path.basename(path), file_path, file_path_output)
        else:
            print(os.path.basename(path), file_path, file_path_output)
            sc.evaluate_file_so(os.path.basename(path), file_path, file_path_output, filename, median_filtered_folder)
        print("\n\n")

    print("YEEYEEEEEEEEEEEEEEEEEE")
    print(file_path)
    print(file_path)
    print(file_path)
    print(file_path)
    print(file_path)
    print(file_path)
    file_list = gfl.get_file_list(file_path, "")
    if file_list[0] > 0:
        pg.plot_graph(file_list[1], file_path_output)
    else:
        print("No plotting data could be gathered")

    end_string = ['O0', 'O1', 'O2', 'O3', 'Ofast']
    for _ in end_string:
        file_list = gfl.get_file_list(file_path, _)
        if file_list[0] > 0:
            pg.plot_graph(file_list[1], file_path_output, _)
        else:
            print("No plotting data could be gathered")

    end_time_a = time.time()

    elapsed_time_a = (end_time_a - start_time) / 60

    print(f"Elapsed Time: {elapsed_time_a:.2f} minutes")
