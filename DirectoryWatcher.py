from sys import *
import os

def directoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists= os.path.isdir(path)

    if exists:
        for foldername,subfolder,filename in os.walk(path):
            print("Current folder is :" +foldername)
            for subf in subfolder:
                print("subfolder of "+ foldername+ "is:" +subf)
            for filen in filename:
                print("File inside " +foldername+ "is :"+ filen)
            print(' ')
    else:
        print("Invalid path")
def main():
    print("-----------Developed by Rani Jadhav-------------")
    print("Application name : "+argv[0])

    if (len(argv)!=2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]== "-H"):
        print("This is script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1]== "-U"):
        print("usage = Application absolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])
    except valueError:
        print("Error: Invalid datatype of input")
    except Exception:
        print("Error: Invalid input")

if __name__ == '__main__':
    main()

