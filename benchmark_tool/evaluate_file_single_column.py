# single columns from function that only executes one function to be benchmarked
import statistics

from scipy import signal


def evaluate_file_so(filename, file_path_output, file_path , date, median_filtered_folder):
    file_path = file_path + filename
    file_path_output = file_path_output + date
    print("EVALUATE FILE SO")
    print(file_path)
    print(file_path_output)
    print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    # debugging
    row_count = len(lines) - 1
    print("Row count: " + str(row_count))

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            data.append(columns)

    median_arr = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            try:
                median_arr.append(int(columns[0]))
            except ValueError:
                print("Data is wrongly formatted, shall be like this:\n44\n58\n290\n12\netc..")

    median = statistics.median(median_arr)

    median_arr = signal.medfilt(median_arr)

    for element in median_arr:
        with open(median_filtered_folder + filename, 'a') as file:
            print(f"{element}", file=file)

    try:
        data = [[int(value) for value in row] for row in data]
    except ValueError:
        print("There was an issue reading the data. Its either not in the right format "
              "or the program had unexpected output.")

    num_columns = len(data[0])
    columns = [sum(data[row][col] for row in range(len(data))) for col in range(num_columns)]
    for col, col_sum in enumerate(columns):
        print(f"Sum of all cycles: {col_sum}")
        print(f"Average cycles: {col_sum / row_count}")
        print(f"Median: {median}")

        with open(file_path_output, 'a') as file:
            print(f"File: " + filename, file=file)
            print(f"Sum of all cycles: {col_sum}", file=file)
            print(f"Average cycles: {col_sum / row_count}", file=file)
            print(f"Median: {median}\n", file=file)

        with open(file_path_output + "-machine_readable", 'a') as file:
            print(f"{filename}", file=file)
            print(f"{col_sum}", file=file)
            print(f"{col_sum / row_count}", file=file)
            print(f"Median: {median}", file=file)
