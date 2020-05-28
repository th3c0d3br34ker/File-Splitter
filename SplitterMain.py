from os import getcwd, listdir, chdir, system
from os.path import isfile, isdir, getsize
from fileSplitCore import fileSplitter, fileJoiner


def main():
    print("*************** Welcome **************")
    print("Enter 1 to Split 2 to Join")
    option = int(input())
    if(option == 1):
        splitter()
    elif(option == 2):
        joiner()
    print("\nThank You!")


def splitter():
    print("\nLooking for files in local directory...\n")
    chdir("TestFiles")
    path = getcwd()
    print("Currently in : \n{}\n".format(path))
    filelist = [x for x in listdir() if isfile(x)]
    n = len(filelist)
    print("List of Files :")
    for i in range(n):
        print("{0}. {1} ".format(i+1, filelist[i]))
    print("\nEnter file number : ")
    x = int(input())
    filename = filelist[x-1]
    print("\nEnter the number of chunks : ")
    n = int(input())
    file_size = getsize(filename)
    Int = file_size//n
    Dec = (file_size/n) - (Int)
    if (Dec == 0):
        chunk = Int
    else:
        chunk = Int + 1
    main_file = path+"\\"+filename
    fileSplitter(main_file, chunk)


def joiner():
    chdir("TestFiles")
    print("\nLooking for available folders in local directory...\n")
    folderlist = [x for x in listdir() if (isdir(x))]
    n = len(folderlist)
    print("List of Folders Available :")
    for i in range(n):
        print("{0}. {1} ".format(i+1, folderlist[i]))
    print("\nEnter file number : ")
    x = int(input())
    foldername = folderlist[x-1]
    fileJoiner(foldername)


if __name__ == '__main__':
    system('cls')
    main()
