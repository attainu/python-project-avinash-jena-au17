import os

def by_size():
    dir_path = input("Enter the Path to a directory :-")
    if os.path.isdir(dir_path):
        return dir_path
    else:
        dir_path = by_size()
        return dir_path

if __name__ == '__main__':
# for getting the directory path from the user.
    directory_location = by_size() 
# changing the current directory to the given path
    os.chdir(directory_location)
 # creating dictionary with file sizes
    size_dic = {}
    for files in os.listdir(directory_location):
# restricting for the files only
        if os.path.isfile(files): 
            size_dic[files] = os.stat(files).st_size # give size in bytes

  # sorting dictionary by size, --> value of the dictionary
    print(f'\tFile Name{6*"  "}\t\tFile Size\n{24*"--"}')
    for file,size in sorted(size_dic.items(), key = lambda kv:(kv[1], kv[0])):
# printing file size and names sorted by their size
        print(f'{file}\t\t---> {size/1000:.03f} Kb') 