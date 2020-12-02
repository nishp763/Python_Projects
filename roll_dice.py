from random import randint # for random generation
from collections import Counter # for counting

def roll_dice(*dice):
    min_outcome = len(dice) # 1 outcome on all dice face
    max_outcome = sum(dice) # add all dice faces together 
    
    counts = Counter() # initialize Counter collection
    num_trials = 1_000_000 # runs for monte carlo experiment

    for trial in range(0, num_trials): # run experiement
        roll_outcome = 0 
        for sides in dice: # go through all dice 
            roll_outcome += randint(1, sides) # roll all dice and add it to outcome
        counts[roll_outcome] += 1 # increment the count with the dice roll outcome
        
    # print the table
    print('{}\t{}'.format("OUTCOME","PROBABILITY"))
    for dice_outcome in range(min_outcome, max_outcome+1):
        # calculate probability by dividing count / # of trials
        print('{}\t{:0.2f}%'.format(dice_outcome, counts[dice_outcome]*100/num_trials))

if __name__ == "__main__":
    roll_dice(4, 6, 6)