import os # for dealing with directories
import zipfile # for creating a zipped file

def zip_all(input_dir, file_ext, out_zip_path):
    with zipfile.ZipFile(out_zip_path, 'w') as myzip: # create a zip file
        for root, directories, files in os.walk(input_dir): # scan the entire directory
            rel_path = os.path.relpath(root,input_dir) # get only the relative path my_stuff
            for file in files: # loop through all files
                fname, fext = os.path.splitext(file) # split filename and extension
                if fext in file_ext: # check if the file extension is in the list of files to be zipped
                    actual_f_path = os.path.join(root,file) # file to be read with full path
                    rel_f_path = os.path.join(rel_path,file) # relative path inside the zipped archive
                    myzip.write(filename=actual_f_path, arcname=rel_f_path) # write to zipped folder
    myzip.close() # close zip file
    print("Succefully created a zipped folder:",out_zip_path) # confirmation message
    return

if __name__ == "__main__":
    in_dir = os.path.join(os.getcwd(),'files/my_stuff') # path to my stuff folder
    file_ext = ['.jpg','.txt'] # list containing file extensions to include
    out_zip_path = os.path.join(os.getcwd(),'files/my_stuff.zip') # path for zipped file
    zip_all(in_dir, file_ext, out_zip_path)