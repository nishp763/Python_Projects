def is_palindrome(str_input):
    str_cleaned = str_input
    str_cleaned = (str_cleaned.lower()).replace(' ','') # change all char case to lowercase and remove space
    for i in str_cleaned: # loop through the string and remove all non alphabet characters
        if i.isalpha() == False:
            str_cleaned = str_cleaned.replace(i,'')

    str_len = len(str_cleaned)
    if str_len%2 == 0:
        middle_index = (int) (str_len/2)
        str_second_reversed = str_cleaned[middle_index:] [::-1]
        str_first = str_cleaned[:middle_index]
    else:
        middle_index = (int) ((str_len/2) + 1)
        str_second_reversed = str_cleaned[middle_index:] [::-1]
        str_first = str_cleaned[:middle_index-1]
    
    return (str_first == str_second_reversed)


if __name__ == "__main__":
    print(is_palindrome("hello world"))
    print(is_palindrome("Ra CEcar"))
    print(is_palindrome("Go hang a salami - I'm a lasagna hog."))