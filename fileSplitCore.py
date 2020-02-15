import traceback
import os

def fileJoiner(folder):
    try:
        os.chdir(folder)
        print("Current directory : ",os.getcwd())
        print("{} is selected.".format(folder))
        path = os.getcwd()
        files = [x for x in os.listdir()]
        print("\nFile to be joned : ")
        for i in files: print(i)
        fn = files[0]
        filename = fn.replace(fn[fn.index('_partfile_'):],'')
        with open(filename,'wb') as main_file:
            for f in files:
                with open(f,'rb') as part_file:
                    file_obj = part_file.read()        
                main_file.write(file_obj)
                os.remove(f)
        os.chdir("..")
        print("\nCurrent directory : ",os.getcwd())
        print("\nFiles joined to {} file.".format(filename))
    except Exception:
        print("\nFailed!")
        traceback.print_exc()

def fileSplitter(filename,size):
    print("{} will be splitted.".format(os.path.basename(filename)))
    try:
        with open(filename,'rb') as file:
            f = file.read(size)
            count = 0
            foldername = os.path.basename(filename)
            foldername = foldername+"_partfile"
            os.mkdir(foldername)
            os.chdir(foldername)
            while(len(f) > 0):
                
                if(count < 10):
                    fpart = '0'+str(count)
                else:
                    fpart = str(count)
                
                with open(foldername+"_"+fpart,'wb') as part:
                    part.write(f)
                    part.close()
                
                count+=1
                f = file.read(size)
            
        file.close()
        print("\nFile Splitted to",foldername)
    except Exception:
        print("\nFailed!")
        traceback.print_exc()

