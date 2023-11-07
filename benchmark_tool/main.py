import os
import sys

import manual_tests as mt
import automated_tests as at

data_folder = './data/'
output_data_folder = './output_data/'
executable_path = './binaries/'
median_filtered_folder = './median_filtered_data/'
modes = ['mo', 'so']

if __name__ == '__main__':
    # single file, multiple output or multiple files, single output
    # for the ones that do not want to use the menu, there are commandline arguments
    # if value passed is = 1 then automated tests, else manual
    # the second value determines the exponent of two as n-1
    # so if you give 20 it will be 2¹⁹
    mode_set = 'mo'
    mode_temp = 'mo'
    cmd = 0
    exponent = 1
    try:
        cmd = int(sys.argv[1])
        exponent = int(sys.argv[2])
        mode_tmp = str(sys.argv[3])
        if mode_tmp == modes[0]:
            mode_set = modes[0]
        else:
            mode_set = modes[1]
    except IndexError:
        print("Handled Index Error")
        cmd = 0
        exponent = 16
        mode_set = modes[0]
    except ValueError:
        print("Handled Value Error")
        cmd = 0
        exponent = 16
        mode_set = modes[0]

    if exponent <= 0 or exponent > 32:
        print("You entered an invalid samplesize. Defaulting to 16.")
        exponent = 16

    # defines where the exes are located
    # searches files in this folder, files beginning with a dot are ignored
    filenames = []
    print("Detecting files...")
    for filename in os.listdir(executable_path):
        if os.path.isfile(os.path.join(executable_path, filename)):
            if not (filename.startswith('.') or filename.endswith('.sh')):
                filenames.append(executable_path + filename)
                # print(filename)
    # print(filenames)
    number_of_files = len(filenames)

    executable_path = filenames
    print("Detected files: ")
    for _ in executable_path:
        print(os.path.basename(_))
    print("\n")

    exec_path = False
    # if no commandline arguments are given, or it was chosen to manually choose:
    if cmd == 0:
        try:
            tests = int(input("Enter \"0\" for manual inputs tests or \"1\" if you want to execute "
                              "automated tests over commandline arguments: "))
            if tests == 0:
                exec_path = True
            else:
                exec_path = False
        except ValueError:
            exec_path = True

        if exec_path.__eq__(True):
            try:
                exponent = int(
                    input("Please enter the samplesize. The number you enter will be the exponent of 2 and must be "
                          "bigger"
                          "than 0.\nValues over 20 will increase the runtime massively and values over 32 are not "
                          "allowed:"
                          " "))
            except ValueError:
                exponent = 16
            # defines which exe to execute
            if exponent <= 0 or exponent > 32:
                print("You entered an invalid samplesize. Defaulting to 16.")
                exponent = 16

            mt.manual_tests(exponent, mode_set, modes, executable_path)

        else:
            at.automated_tests(data_folder, mode_set, modes, executable_path, exponent, number_of_files,
                               output_data_folder,
                               median_filtered_folder)

    else:
        at.automated_tests(data_folder, mode_set, modes, executable_path, exponent, number_of_files, output_data_folder,
                           median_filtered_folder)
