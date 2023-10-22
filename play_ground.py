#script to rename files in /leeetcode directory
#these directory contains other folders e.g "8. Add Two"
#these folders contain files named solution.py
#Rename solution.py to the parent folder name e.g 8_Add_Two.py


import os

def main():
   
    folder = "Leetcode"
    for filename in os.listdir(folder):
        path = folder + "/" + filename
        if os.path.isdir(path):  
            print("\nIt is a directory")  
            
            newName = "Leetcode" + "/" + filename.replace(".", "_").replace(" ", "_") + ".py"
            print(filename, newName)
            rename_and_move_file(path, newName)
            break
 
def rename_and_move_file(path, newPath):
    file = os.listdir(path)[0]
    src = f"{path}/{file}"
    dst = newPath

    print(src, dst)
    # os.rename(src, dst)
    # os.rmdir(path)

# Driver Code
if __name__ == '__main__':
     
    main()