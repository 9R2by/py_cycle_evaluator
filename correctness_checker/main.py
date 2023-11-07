import os
import subprocess
import datetime
import time

from secrets import token_hex

from tqdm import tqdm

executable_path = '../benchmark_tool/binaries/quick_byteswap_demo'


def evaluate_file(filename):
    file_path = './data/' + filename  # Replace with the path to your file

    # Open the file and read all lines into a list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Calculate the row count based on the length of the list
    row_count = len(lines)
    print("Row count: " + str(row_count))

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()  # Split each line into columns based on whitespace
            data.append(columns)

    # Step 2: Convert the data to numbers
    # Convert the data to a list of lists of integers
    data = [[int(value) for value in row] for row in data]

    # Step 3: Calculate the sum of each column
    # Transpose the data to work with columns
    num_columns = len(data[0])
    column_sums = [sum(data[row][col] for row in range(len(data))) for col in range(num_columns)]
    minimal = 0
    print("Sum of each column:")
    for col, col_sum in enumerate(column_sums):
        print(f"Column {col + 1}: {col_sum}")
        print(f"Average Column {col + 1}: {col_sum / row_count}")
        if min(column_sums) == col_sum:
            minimal = col + 1

        with open('./data/' + filename + '-summary', 'a') as file:
            # Print to the console and append to the file
            # print(output_text)
            print(f"Column {col + 1}: {col_sum}", file=file)
            print(f"Average Column {col + 1}: {col_sum / row_count}", file=file)
            print(f"Minimal value: " + str(min(column_sums)), file=file)
            print(f"Column with minimal value: " + str(minimal), file=file)


def call_with_random_values(filename):
    x0 = token_hex(4)
    x1 = token_hex(4)
    x2 = token_hex(4)
    x3 = token_hex(4)
    x0_bytearray = bytearray.fromhex(x0)
    x1_bytearray = bytearray.fromhex(x1)
    x2_bytearray = bytearray.fromhex(x2)
    x3_bytearray = bytearray.fromhex(x3)
    x0_bytearray.reverse()
    x1_bytearray.reverse()
    x2_bytearray.reverse()
    x3_bytearray.reverse()

    command = [executable_path, "-c", x0, x1, x2, x3]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # return_code = process.returncode
    if os.name == 'nt':
        output_text = stdout.decode("utf-8").replace("\r\n", "")
    else:
        output_text = stdout.decode("utf-8")

    with open('./data/' + filename, 'a') as file:
        # Print to the console and append to the file
        # print(output_text)
        # print(x0, x1, x2, x3, file=file)
        print(x0_bytearray.hex(), x1_bytearray.hex(), x2_bytearray.hex(), x3_bytearray.hex(), file=file)
        print(output_text, file=file)
    # print(output_text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    current = current_datetime.strftime("%Y-%m-%d-%H-%M-%S.%f")[:-3]
    x = pow(2, 15)
    print('Sample size: ' + str(x))
    print('Sample file: ' + str(current))
    start_time = time.time()
    for _ in tqdm(range(x), desc="Loading", unit="item"):
        call_with_random_values(current)

    evaluate_file(current)

    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = (end_time - start_time) / 60

    # Display the elapsed time
    print(f"Elapsed Time: {elapsed_time:.2f} minutes")
