import random # use random to generate random target time
import time # for timer

def waiting_game():
    print("Welcome to the Waiting Game\n")

    target_time_int = random.randint(2,4) # randomly choose a target time between 2 to 4 seconds
    print("Your target time is", target_time_int, "seconds.\n")
    input("---Press Enter to Begin---\n")
    start_timestamp = time.perf_counter() # start timer

    input("---Press Enter again after {} seconds.\n".format(target_time_int))
    finish_timestamp = time.perf_counter() # stop timer
    elapsed_time = finish_timestamp - start_timestamp # calculate elapsed time
    print(("Elapsed time: {0:.3f} seconds").format(elapsed_time))
    
    time_difference = elapsed_time - target_time_int # calculate the time difference

    if time_difference == 0: # right on time
        print(" (Unbelievable! Perfect timing!)\n")
    elif time_difference < 0: # too fast
        print(("({0:.3f} seconds too fast)\n").format(time_difference))
    else: # too slow
        print(("({0:.3f} seconds too slow)\n").format(time_difference))

if __name__ == "__main__":
    waiting_game()