import os;
import sys;
import MarvellousChecksum;
import schedule;
import time;

def DuplicateRemoval(path):
    print("Files are....");
    
    data = {};
    for Folder,Subfolder,Files in os.walk(path):
        for name in Files:
            #print(name);
            name = os.path.join(Folder,name);
            
            checksum = MarvellousChecksum.hashfile(name);
            #print(checksum);

            if checksum in data:
                data[checksum].append(name);
            else:
                data[checksum] = [name];

    newdata = [];
    newdata = list(filter(lambda x: len(x)>1,data.values()));

    count = 0;
    for outer in newdata:
        icnt = 0;
        for inner in outer:
            icnt+=1;
            if icnt >= 2:
                count+=1;
                print("Delete",inner);
                os.remove(inner);

    print("Total files deleted",count);

def main():
    print("Duplicate file removal...");

    schedule.every(1).minute.do(DuplicateRemoval,path=sys.argv[1]);

    while True:
        schedule.run_pending();
        time.sleep(1);


if __name__ == "__main__":
    main();



















