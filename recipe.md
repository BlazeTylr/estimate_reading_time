# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_reading_time(reading_speed, words):
    """Extracts words from a string

    Parameters: (list all parameters and their types)
        words: a string containing words (e.g. "hello WORLD")
        reading_speed: it is a number which describes how many word a user can read a minute approximately (e.g. 200)

    Returns: (state the return value and its type)
        an estimated reading time. (e.g. 2 h 30 min)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a time(number -> reading_speed) and string of words.
It returns an approximate time how fast you can read the string specified.
"""
estimate_reading_time(reading_speed, words): => 2 h 30 min



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.estimate_reading_time import *

"""
Given a time(number -> reading_speed) and string of words.
It returns an approximate time how fast you can read the string specified.
"""
def test_estimate_reading_time_correct_number():
    result = estimate_reading_time(200, string)
    assert result == 2 h 30 mins
```
