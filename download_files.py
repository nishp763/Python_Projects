import os # for file directory

def download_files(first_url, out_folder):
    # check if the output directory exists, if not create it
    if os.path.isdir(out_folder) == False:
        os.mkdir(out_folder)
        print('Created directory:',out_folder)

    head, tail = os.path.split(first_url) # head is everything before the slash and tail is everything after the slash
    print(head,'\t',tail)
    return

if __name__ == "__main__":
    out_path = os.path.join(os.getcwd(),'files','images')
    download_files('http://699340.youcanlearnit.net/image001.jpg',out_path)
    