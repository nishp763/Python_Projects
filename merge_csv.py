import os # for file path manipulation
import csv # for dealing with CSV files

def merge_csv(myfilelist, outfile):
    col_list = list() # holds all column names for merged csv file

    # loop through all csv files ensure path is correct and get column names
    for file_to_read in myfilelist:
        if (os.path.exists(file_to_read) == False): # invalid path
            print("ERROR File Doesn't Exist:",file_to_read)
            return
        else: # read column names and add it to col_list
            csv_file = open(file_to_read, 'r')
            reader = csv.DictReader(csv_file).fieldnames # read col names
            csv_file.close()
            for col in reader: # go through all cols in csv file
                if col not in col_list: # its a unique col then add it
                    col_list.append(col)
    
    # start writing to merged output file
    out_merged_file = open(outfile,'w')
    writer = csv.DictWriter(out_merged_file,fieldnames=col_list) # provide all columns
    writer.writeheader() # write all col values

    # read csv files and write to merged files row by row
    for file_to_read in myfilelist:
        csv_file_read = open(file_to_read,'r') # open csv file
        reader = csv.DictReader(csv_file_read) # read the entire csv as dict obj
        writer.writerows(reader) # write to output file
        csv_file_read.close()  
    out_merged_file.close()
    return
    

if __name__ == "__main__":
    file_dir =  os.path.join(os.getcwd(), 'files')
    class1_file = os.path.join(file_dir, 'class1.csv')
    class2_file = os.path.join(file_dir, 'class2.csv')
    merged_csv_file = os.path.join(file_dir, 'all_students.csv')
    merge_csv([class1_file, class2_file],merged_csv_file)