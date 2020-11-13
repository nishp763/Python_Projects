def index_all(list_to_search, val_to_search):
    index_list = []
    for i in range(0, len(list_to_search)): # iterate through each item
        if list_to_search[i] == val_to_search: # if the list element contains the value looking for
            index_list.append([i]) # add the index to the list

        elif isinstance(list_to_search[i], list): # check if the element has a list
            for item in index_all(list_to_search[i], val_to_search): # recursive call
                index_list.append([i]+item) # add to our list

    return index_list

if __name__ == "__main__":
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))