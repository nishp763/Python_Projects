import os # for file path manipulation
import pandas as pd # for reading csv files

def merge_csv(myfilelist, outfile):
    master_df = pd.DataFrame()
    # check all file which will be read exists and file path is valid
    for file_to_read in myfilelist:
        if (os.path.exists(file_to_read) == False):
            print("ERROR File Doesn't Exist:",file_to_read)
            return
        else:
            df_read = pd.read_csv(file_to_read, header=0)
            master_df = master_df.append(df_read, ignore_index=True)
 
    master_df.to_csv(outfile, index=False)
    return
    

if __name__ == "__main__":
    file_dir =  os.path.join(os.getcwd(), 'files')
    class1_file = os.path.join(file_dir, 'class1.csv')
    class2_file = os.path.join(file_dir, 'class2.csv')
    merged_csv_file = os.path.join(file_dir, 'all_students.csv')
    merge_csv([class1_file, class2_file],merged_csv_file)