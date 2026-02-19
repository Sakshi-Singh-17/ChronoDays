ChronoDays

Leap Year Aware Month Day Calculator (Python)

📌 Overview

ChronoDays is a Python-based calendar utility that calculates the number of days in a given month while correctly handling leap year logic according to the Gregorian calendar rules.

This project demonstrates fundamental programming concepts such as:

Functions

Conditional logic

Dictionaries

User input handling

Leap year algorithm implementation

🚀 Features

Accepts user input for month and year

Implements accurate leap year rules:

Divisible by 4

Not divisible by 100 unless divisible by 400

Returns correct number of days for all months

Clean and readable code structure

🧠 Leap Year Logic Used

A year is considered a leap year if:

(year % 400 == 0) OR 
(year % 4 == 0 AND year % 100 != 0)


This ensures century years are handled correctly.



