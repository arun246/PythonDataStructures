import os

def diskusage(path=""):
    total_size=os.path.getsize(path)
    if(os.path.isdir(path)):
        for dire in os.path.listdir(path):
            child_path = os.path.join(path,dire)
            total_size=total_size+diskusage(child_path)
    return " size is"+total+"of path is"+path

print(diskusage("C:\\Users"))
