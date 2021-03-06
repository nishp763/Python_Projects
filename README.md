# Python_Projects
This repository contains several projects that I have completed in Python to enhance and hone my python programming skills.

### Find prime factors
**Challenge:** Write a Python function to find all prime factors.</br>
**Input:** integer value</br>
**Output:** list of prime factors</br>
**Sample Input & Output:**
```python
>>> get_prime_factors(630)
Input: 630
Output: [2, 3, 3, 5, 7]
Explanation: 2 x 3 x 3 x 5 x 7 = 630

>>> get_prime_factors(13)
Input: 13
Output: [13]
Explanation: 13 x 1 = 13; 13 itself is a prime number
```

### Identify a palindrome
**Challenge:** Write a Python function to determine if a given string is a palindrome.</br>

- Only consider letters (A-Z)</br>
- Ignore case (for example, 'A'=='a')</br>

**Input:** string to evaluate</br>
**Output:** boolean value</br>
**Sample Input & Output:**
```python
>>> is_palindrome("hello world")
Input: "hello world"
Output: False
Explanation: The Input string is not a palindrome

>>> is_palindrome("Go hand a salami - I'm a lasagna hog.")
Input: "Go hand a salami - I'm a lasagna hog."
Output: True
Explanation: Once the case, punctuation and other characters are removed from the string, the string becomes 'gohandasalamiimalasagnahog' which is a palindrome string.
```

### Sort a string
**Challenge:** Write a Python function to sort the words in a string. </br>

- Ignore case when sorting. For example: "The" is same as "the". </br>
- Words in the output strings should have same case as input. </br>

**Input:** string of words, separated by spaces </br>
**Output:** string of words, sorted alphabetically </br>
**Sample Input & Output:**
```python
>>> sort_words('string of words')
Input: 'string of words'
Output: 'of string words'
Explanation: sorted alphabetically.

>>> sort_words('banana ORANGE apple')
Input: 'banana ORANGE apple'
Output: 'apple banana ORANGE'
Explanation: sorted alphabetically and case ignored
```

### Find all list items
**Challenge:** Write a Python function to index all items in a list. </br>

- Keep in mind that lists can contain other lists. </br>

**Input:** list to search, value to search for </br>
**Output:** list of indices </br>
**Sample Input & Output:**
```python
>>> example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
>>> index_all(example, 2)
Input: ([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)
Output: [[0, 0, 1], [0, 1], [1, 1]]
```

### Play the waiting game
**Challenge:** Write a Python function to play a pulse pounding game of patience, known as the <em>waiting game</em>. When the player runs the waiting game program it should print a message for them to wait a random amount of time, somewhere between 2 to 4 seconds. When the player presses <em>Enter</em>, that starts a timer. The player's goal is to wait the specified number of seconds and then press <em>Enter</em> again. That displays the elapsed time, along with a message about whether the player was too fast, too slow, or right on target.</br>

**Input:** 1st Enter keypress will start timer and 2nd Enter keypress will stop the timer.</br>
**Output:** Display the target time to user then display the reaction time along with time difference between the target and the actual.</br>
**Sample Input & Output:**
```python
>>> waiting_game()

Your target time is 4 seconds.
---Press Enter to Begin---

...Press Enter again after 4 seconds...

Elapsed time: 4.213 seconds (0.213 seconds too slow)
```

### Save a dictionary
**Challenge:** 
- Write a Python function to save a dictionary object to a file.</br>
- Write another Python function to load a saved dictionary object from a file and display it.</br>

**Input:** 
- `save_dict`: dictionary to save, output file path as parameters.</br>
- `load_dict`: file path to read the stored dictionary as parameter.</br>
  
**Output:** </br>
- `save_dict`: output file with saved dictionary object.</br>
- `load_dict`: retrieved dictionary object. </br>

**Sample Input & Output:**
```python
>>> save_load_dictionary()
Input: 
dict_for_save =	{"brand": "Ford", "model": "Mustang", "year": 1964}
file_path = current_directory + "carDictionary"

save_dict(dict_for_save, file_path)
load_dict(fpath)

Output:
Dictionary saved successfully to: /home/carDictionary
Dictionary loaded successfully
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Is the loaded dictionary same as the dictionary which was written to the file: True
```

### Set an alarm
**Challenge:** Write a Python function to play a sound and print a message at a set time.</br>
**Input:** alarm time, sound file, message.</br>
**Output:** print a message indicating the alarm time, then alarm message with alarm sound.</br>
**Sample Input & Output:** </br>
```python
>>> set_alarm(time.time()+1, 'alarm.wav', 'Wake up!')
Input: time.time()+1, 'alarm.wav', 'Wake up!'

Output: 
Alarm set for Sat Nov 14 15:08:50 2020
Wake up!
<Playing sound file>
```

### Send an email
**Challenge:** Write a Python function to send a basic email notification.</br>
**Input:** receiver email address, subject line, message body.</br>
**Output:** email sent to the receiver's email address with the subject line and message body.</br>
**Sample Input & Output** </br>
```python
Input: "receiveremail@gmail.com", "Python: Hello Email!", "Hi, this is an email from Python program."
Output:
        To: receiveremail@gmail.com
        From: senderemail@gmail.com
        Subject: Python: Hello Email!
        Message: Hi, this is an email from Python
```

### Simulate dice
**Challenge:** Write a Python function to determine the probability of certain outcomes when rolling dice. Use Monte Carlo method with 1 million simulations to get a stastically significant result. </br>
**Input:** variable number of arguments for sides of dice. </br>
**Output:** table of probability for each possible outcome. </br>
**Sample Input & Output:** </br>
```python
>>> roll_dice(4,6,6)
Outcome Probability
3	0.69%
4	2.08%
5	4.18%
6	6.94%
7	9.71%
8	12.52%
9	13.87%
10	13.87%
11	12.56%
12	9.69%
13	6.94%
14	4.16%
15	2.09%
16	0.70%
```

### Count unique words
**Challenge:** Write a python function to count the number of unique words and how often each occures. Note:</br>

- Ignore case</br>
   - e.g. "The" is same as "the"</br>
- Words contain:
   - Letters</br>
   - Numbers</br>
   - Apostrophes</br>
   - Hyphens</br>

**Input:** path to a text file.</br>
**Output:** print message with:</br>

- total number of words</br>
- top 20 most frequent words</br>
- number of occurrences for top 20</br>

**Sample Input & Output:** </br>
```python
>>> count_words('input.txt')
Total Words: 473

Top 20 Words:
TEXT             13
CHALLENGE        11
WORDS            9
YOUR             5
FUNCTION         5
...              ...

```

### Generate a password
**Challenge:** Write a python function to generate passphrases using dicemware. Go to https://www.diceware.com to get the diceware list.</br>
**Input:** Number of words in passphrase.</br>
**Output:** String of random words, separated by spaces.</br>
**Sample Input & Output:**</br>
```python
>>> generate_passphrase(5)
'vice fame tango abide verb'
```

### Merge CSV Files
**Challenge:** Write a Python function to merge multiple CSV files. Note: your function must be robust enough to merge CSV files even if the headers don't match or if the header order is different.</br>
**Input:** list of input files, output file path.</br>
**Output:** a single .csv file containing all merged information.</br>
**Sample Input & Output:** </br>
```python
>>> merge_csv(['class1.csv','class2.csv'], 'all_students.csv')
```

### Solve a Sudoku
**Challenge:** Write a Python function to solve a sudoku puzzle. Use a standard 9x9 grid. </br>
**Input:** 2D List representing the puzzle. 0 denotes an empty space.</br>
**Output:** solved Sudoku puzzle with a 2D list.</br>
**Sample Input & Output:** </br>
```python
>>> puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
>>> solve_sudoku(puzzle)
             [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9,1],
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]
```

### Build a ZIP archive
**Challenge:** Write a Python function build a ZIP archive. Note: ZIP archive should maintain folder structure relative to top-level directory.</br>
**Input:** It should accept the following: input directory path, list of file extensions, output file path.</br>
**Output:** a ZIP file. </br>
**Sample Input & Output:** </br>
```python
>>> zip_all('.\\my_stuff',['.jpg','.txt'],'my_stuff.zip')
Output -> single my_stuff.zip file containing all .jpg and .txt file from my_stuff directory
```

### Download sequential files
**Challenge:** Write a Python function to download and save a sequence of files. Note: it is not specified inside the function, how many images to download, so it should continue to download all available sequential files.</br>
**Input:** It should take 2 inputs: URL for first item, output directory path.</br>
**Output:** Automatically download all available sequential files from the internet and store it in the output directory.</br>
**Sample Input & Output:** </br>
```python
>>> download_files('http://699340.youcanlearnit.net/image001.jpg','.\images')

Successfully downloaded
http://699340.youcanlearnit.net/image001.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image002.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image003.jpg
...
...
...
Successfully downloaded
http://699340.youcanlearnit.net/image050.jpg

Could not retrieve
http://699340.youcanlearnit.net/image051.jpg
```