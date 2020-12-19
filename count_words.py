def count_words(file_to_read):
    
    file = open(file_to_read, 'r') # open text file in read mode
    file_content = file.read() # read the file and its content
    file.close() # close the file

    #print(file_content) # print file content after reading

    # algorithm
    # convert all words to uppercase
    # count occurence of each unique word
    # store in a sorted datatype


if __name__ == "__main__":
    input_text_file = 'input.txt'
    count_words(input_text_file)