from random import randint # for random generation

# this method will generate a five digit number aka simulating a dice roll
def gen_five_rand_digits():
    five_dig_str = ''
    for i in range(1,6): # get 5 digits
        five_dig_str = five_dig_str + str(randint(1,6)) # get a random int between 1 to 6 exclusive
    return five_dig_str # return as a string to match dictionary keys datatype
    
def generate_passphrase(num_words):
    file_path = 'diceware_list.txt' # file path containing diceware list
    file = open(file_path, 'r') # open text file in read mode

    diceware_dict = {} # create a dictionary to hold dice value and passphrase from the diceware list
    for i in file.readlines()[2:7778]: # read only lines 2 to 7777
        item = i.split() # split string separated by space
        dice_value = item[0] # dice value
        passphrase = item[1] # passphrase
        diceware_dict[dice_value] = passphrase # add to dictionary
    file.close() # close the file
   
    dice_passphrase = [] # list to hold all generated passphrase
    for i in range(0,num_words): # generate num_words passphrase from dice list
        five_dig_str = gen_five_rand_digits() # get a random 5 digit number aka dice roll outcome
        dice_passphrase.append(diceware_dict[five_dig_str]) # lookup the digit in dice dictionary and get the passphrase

    separator = ' ' # seperate passphrase by space
    generated_passphrase = separator.join(dice_passphrase) # concatenate all passphrase into one

    print(generated_passphrase)
    return generated_passphrase

if __name__ == "__main__":
    generate_passphrase(5)