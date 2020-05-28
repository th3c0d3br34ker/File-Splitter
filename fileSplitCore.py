from traceback import print_exc
from os import getcwd, remove, chdir, listdir, mkdir
from os.path import basename


def fileJoiner(folder):
    """
    This function joins all the files in the input folder and outputs a single file.

    Args:

        folder: path of the folder which contains the splitted files.
    """
    try:
        chdir(folder)
        print("Current directory : ", getcwd())
        print("{} is selected.".format(folder))
        files = [x for x in listdir()]
        print("\nFile to be joned : ")
        for i in files:
            print(i)
        fn = files[0]
        filename = fn.replace(fn[fn.index('_partfile_'):], '')
        with open(filename, 'wb') as main_file:
            for f in files:
                with open(f, 'rb') as part_file:
                    file_obj = part_file.read()
                main_file.write(file_obj)
                remove(f)
        chdir("..")
        print("\nFiles joined to {} file.".format(filename))
    except Exception:
        print("\nFailed!")
        print_exc()


def fileSplitter(filename, size):
    """
    This functions splits the input file into equal sizes of size size and outputs the files in a folder with '_partfile'.

    Args:

        filename: name of the file.
        size: size of each chunk.
    """
    print("{} will be splitted.".format(basename(filename)))
    try:
        with open(filename, 'rb') as file:
            f = file.read(size)
            count = 0
            foldername = basename(filename)
            foldername = foldername+"_partfile"
            mkdir(foldername)
            chdir(foldername)
            while(len(f) > 0):
                if(count < 10):
                    fpart = '0'+str(count)
                else:
                    fpart = str(count)
                with open(foldername+"_"+fpart, 'wb') as part:
                    part.write(f)
                    part.close()
                count += 1
                f = file.read(size)
        file.close()
        print("\nFile Splitted to", foldername)
    except Exception:
        print("\nFailed!")
        print_exc()
