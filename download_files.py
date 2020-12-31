import os # for file directory
import urllib.parse # for creating URL paths
import urllib.request # for downloading files via URL

def download_files(first_url, out_folder):
    # check if the output directory exists, if not create it
    if os.path.isdir(out_folder) == False:
        os.mkdir(out_folder)
        print('Created directory:',out_folder)

    # head is everything before the slash and tail is everything after the slash
    head, tail = os.path.split(first_url)
    fname,fext = os.path.splitext(tail) # split into file name and file extension
    fname_without_index = fname[:fname.find('0')] # remove all indexes 001 for example and grab only the raw filename
    index = int(fname[fname.find('0'):]) # grab the index in integer format so it starts counting from here

    try:
        while(True): # keep downloading all files while URL is valid
            myfile = fname_without_index + ("%03d" % index) + fext # create a file name
            fullurl = urllib.parse.urljoin(head, myfile) # create a URL with file name
            local_f_path = os.path.join(out_folder,myfile) # path to save the downloaded file with file name
            urllib.request.urlretrieve(fullurl,os.path.join(out_folder,local_f_path)) # download file from internet
            print('Successfully downloaded {}\n'.format(fullurl)) # confirmation message
            index += 1 # increment index to try downloading next file

    except urllib.error.HTTPError: # couldn't retrive the URL aka 404 erro
        print('Could not retrieve {}\n'.format(fullurl)) # error message

    return

if __name__ == "__main__":
    out_path = os.path.join(os.getcwd(),'files','images') # develop an output path
    download_files('http://699340.youcanlearnit.net/image001.jpg',out_path) # call function