import os # for getting the file path
import pickle # for storing & retrieving dictionary object to a file

def save_dict(dict_for_save, out_fpath):
    outfile = open(out_fpath,'wb') # open the file to store the obj in
    pickle.dump(dict_for_save, outfile, protocol=0) # store it
    outfile.close() # close the file
    print("Dictionary saved successfully to:",out_fpath)
    return

def load_dict(in_fpath):
    infile = open(in_fpath,'rb') # open the file to read the obj from
    new_dict = pickle.load(infile) # load it in a new dictionary
    infile.close() # close the file
    print("Dictionary loaded successfully")
    return new_dict # return read dictionary

if __name__ == "__main__":
    dict_for_save =	{"brand": "Ford", 
                     "model": "Mustang", 
                     "year": 1964}
    fpath = os.path.join(os.getcwd(),"carDictionary") # file to write and read from

    save_dict(dict_for_save, fpath) # save dict obj to a file

    read_dict = load_dict(fpath) # read dict obj stored in a file
    print(read_dict) # print out the read dict obj
    print("Is the loaded dictionary same as the dictionary which was written to the file:", dict_for_save == read_dict)