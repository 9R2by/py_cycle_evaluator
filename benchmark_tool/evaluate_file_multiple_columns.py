# multiple columns from file that executes multiple functions that shall be compared
def evaluate_file_mo(filename, file_path, file_path_output):
    file_path = file_path + filename
    file_path_output = file_path_output + filename

    # Open the file and read all lines into a list
    # with open(file_path, 'r') as file:
    #   lines = file.readlines()
    # Calculate the row count based on the length of the list
    # row_count = len(lines)
    # print("Row count: " + str(row_count))

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()  # Split each line into columns based on whitespace
            data.append(columns)

    try:
        data = [[int(value) for value in row] for row in data]
    except ValueError:
        print("There was an issue reading the data. Its either not in the right format "
              "or the programm had unexpected output.")

    num_columns = len(data[0])
    column_sums = [sum(data[row][col] for row in range(len(data))) for col in range(num_columns)]
    minimal = 0
    printed = 0
    filed = 0
    print("Sum of each column:")
    for col, col_sum in enumerate(column_sums):
        print(f"Column {col + 1}: {col_sum}")
        print(f"Average Column {col + 1}: {col_sum / row_count}")
        if min(column_sums) == col_sum:
            minimal = col + 1
        if (minimal != 0) and (printed == 0):
            print(f"\n\nColumn with minimal value: " + str(minimal))
            print(f"Minimal value: " + str(min(column_sums)) + "\n\n")
            printed = 1

        with open(file_path_output + '-summary', 'a') as file:
            # Print to the console and append to the file
            # print(output_text)
            print(f"Column {col + 1}: {col_sum}", file=file)
            print(f"Average Column {col + 1}: {col_sum / row_count}", file=file)
            if (minimal != 0) and (filed == 0):
                print(f"\n\nColumn with minimal value: " + str(minimal), file=file)
                print(f"Minimal value: " + str(min(column_sums)) + "\n\n", file=file)
                filed = 1
