import os


def get_file_list(path_, endswith):
    filenames_ = []
    print("Detecting files in " + path_)
    for fname in os.listdir(path_):
        if os.path.isfile(os.path.join(path_, fname)):
            if not (fname.startswith('.') or fname.endswith('.sh')):
                if endswith == "":
                    filenames_.append(path_ + fname)
                else:
                    if fname.endswith(endswith):
                        filenames_.append(path_ + fname)

                # print(filename)
    # print(filenames)
    filenumber_ = len(filenames_)
    print(filenumber_)

    print("Detected files in " + path_ + ":")
    for _ in filenames_:
        print(os.path.basename(_))
    print("\n")
    # check if filenumber is 0 in caller
    return filenumber_, filenames_