import os
import subprocess
from secrets import token_hex


def call_with_random_values(filename, output_data, path_to_binary):
    print("call_with_random_values")
    print(path_to_binary)
    print(filename)
    print(output_data)
    command = [path_to_binary, '-b', token_hex(4), token_hex(4), token_hex(4), token_hex(4)]
    print("COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMAAAAAAAAAANNNNNNNDOOOOOOOOO")
    print(command)
    print("COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMAAAAAAAAAANNNNNNNDOOOOOOOOO")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if os.name == 'nt':
        output_text = stdout.decode("utf-8").replace("\r\n", "")
    else:
        output_text = stdout.decode("utf-8").replace("\n", "")

    # how to deal with all the files and calculate ?
    # like before, just with one row !!!!
    # if mode_ == mode[1]:
    #    output_text = output_text + os.path.basename(path_name)

    return_code = process.returncode
    if return_code != 0:
        print("Called program did not returned with 0")

    with open(output_data + filename, 'a') as file:
        print(output_text, file=file)
