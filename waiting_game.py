import random # use random to generate random target time
import time # for timer

def waiting_game():
    print("Welcome to the Waiting Game\n")

    target_time_int = random.randint(2,4) # randomly choose a target time between 2 to 4 seconds
    print("Your target time is", target_time_int, "seconds.\n")
    input("---Press Enter to Begin---\n")
    start_timestamp = time.perf_counter()

    input("---Press Enter again after {} seconds.\n".format(target_time_int))
    finish_timestamp = time.perf_counter()
    elapsed_time = finish_timestamp - start_timestamp

    print("Your elapsed time:", elapsed_time)


if __name__ == "__main__":
    waiting_game()