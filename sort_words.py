# this function will convert a string to lowercase and then sort it as a sort criteria
def sort_criteria(my_str):
  return my_str.lower()

# this function takes a string of words and returns a sorted string while ignoring the case
def sort_words(str_input):
    my_list = str_input.split(' ') # extract words by splitting string with space char
    my_list.sort(key = sort_criteria) # sort the list using the custom declared criteria
    list_to_str = (" ").join(my_list) # convert list to string and add spaces in between

    if len(str_input) == len(list_to_str): # ensure the length is the same as the original string
        return list_to_str
    else:
        return "Code Error!"

if __name__ == "__main__":
    print(sort_words('string of words'))
    print(sort_words('banana ORANGE apple'))