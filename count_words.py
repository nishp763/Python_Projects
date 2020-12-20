from collections import Counter # for counting
import re # for regular expressions

def count_words(path):
    file = open(path, 'r', encoding='utf-8') # open text file in read mode
    file_content = file.read() # read the file and its content
    file.close() # close the file

    all_words = re.findall(r"[0-9a-zA-Z-']+",file_content)
    all_words = [word.upper() for word in all_words] # convert all words to upper case
    print("\n# of Total Words:", len(all_words),"\n")

    unique_words = Counter() # initialize Counter collection
    for word in all_words: # count unique words
        unique_words[word] += 1

    most_common_words = unique_words.most_common(20) # get the top 20 words used
    print("TOP 20 WORDS:\n")
    for item in most_common_words: # print top 20 words used
        print('{}\t{}'.format(item[0],item[1]))

    return
    
if __name__ == "__main__":
    input_text_file = 'input.txt' # file to read
    count_words(input_text_file)