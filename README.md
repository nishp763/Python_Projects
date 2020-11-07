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
**Challenge** Write a Python function to determine if a given string is a palindrome.</br>
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