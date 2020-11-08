def index_all(list_to_search, val_to_search):
    index_list = []
    for i in range(0, len(list_to_search)):
        if list_to_search[i] == val_to_search:
            index_list.append([i])

        elif isinstance(list_to_search[i], list):
            for item in index_all(list_to_search[i], val_to_search):
                index_list.append([i]+item)

    return index_list

if __name__ == "__main__":
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))
    #print(index_all([2,2,3], 2))