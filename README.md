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