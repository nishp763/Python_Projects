''' 
Algorithm:
1. check if the file path are valid and file exists
2. read 1 file and display the output
3. then merge it into existing one
4. write to the outfile
5. close files
'''

import os # for file path manipulation
import pandas as pd # for reading csv files

def merge_csv(myfilelist, outfile):
    # check all file which will be read exists and file path is valid
    for file_to_read in myfilelist:
        if (os.path.exists(file_to_read) == False):
            print("ERROR File Doesn't Exist:",file_to_read)
            return

    df1 = pd.read_csv(myfilelist[0])
    print(df1)
    df2 = pd.read_csv(myfilelist[1])

    print(df2)
    # print(myfilelist)
    # print(outfile)
    
    

if __name__ == "__main__":
    file_dir =  os.path.join(os.getcwd(), 'files')
    class1_file = os.path.join(file_dir, 'class1.csv')
    class2_file = os.path.join(file_dir, 'class2.csv')
    merged_csv_file = os.path.join(file_dir, 'all_students.csv')
    merge_csv([class1_file, class2_file],merged_csv_file)