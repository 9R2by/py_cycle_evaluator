import datetime
import time

from tqdm import tqdm

import evaluate_file_single_column as sc
import evaluate_file_multiple_columns as mc
import call_with_random_values as cw


def manual_tests(n, mode_set, modes, executable_path):
    current_datetime_m = datetime.datetime.now()
    current_m = current_datetime_m.strftime("%Y-%m-%d-%H-%M-%S.%f")[:-3]
    x = pow(2, n)
    print('n: ' + str(x))
    print('File: ' + str(current_m))
    start_time = time.time()
    for _ in tqdm(range(x), desc="Loading", unit="item"):
        cw.call_with_random_values(current_m, executable_path, mode_set)

    if mode_set == modes[0]:
        mc.evaluate_file_mo(filename, )
    else:
        sc.evaluate_file_so(current_m)

    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = (end_time - start_time) / 60

    # Display the elapsed time
    print(f"Elapsed Time: {elapsed_time:.2f} minutes")
