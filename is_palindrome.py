def is_palindrome(str_input):
    str_cleaned = str_input
    str_cleaned = (str_cleaned.lower()).replace(' ','') # change all char case to lowercase and remove space
    for i in str_cleaned: # loop through the string and remove all non alphabet characters
        if i.isalpha() == False:
            str_cleaned = str_cleaned.replace(i,'')

    reverse_str = str_cleaned[::-1]
    return (str_cleaned == reverse_str)

if __name__ == "__main__":
    print(is_palindrome("hello world"))
    print(is_palindrome("Ra CEcar"))
    print(is_palindrome("Go hang a salami - I'm a lasagna hog."))