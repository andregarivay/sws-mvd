## Spreetail Work Sample - Multi Value Dictionary
### Andre Garivay
#### Environment Setup
In order to run this program, make sure you have installed python version 3.9.5. To verify your python version, run `python3 --version` in your command line.
#### Running the Program
To run this program, `cd` into the project directory and run `python3 main.py`. When running, you will be able to use the following commands followed by their parameters.

1.  KEYS
2. MEMBERS
3. ADD
4. REMOVE
5. REMOVEALL
6. CLEAR
7. KEYEXISTS  
8. MEMBEREXISTS
9. ALLMEMBERS
10. ITEMS
11. QUIT

Each method is documented in `main.py`.

#### Opportunity for Extension
Due to the time-constricted nature of this project, there are a few things I would like to mention that would have improved the program but taken too much time.
1. Input Validation: Each function currently only accepts a command in all-caps and will allow any value to be stored. Input validation would improve the security (in a larger system implementation) and usability of this program.
2. Unit Testing: While I have been able to manually test each function in several ways, unit testing is the most consistent and unbiased way to catch mistakes in single-responsibility methods in a small program like this one.
3. Refactoring of Runtime Code: The code in this program that is used to run in  the command line is a little clunky. I went with a simple `if/elif/else` strategy in order to focus more on the dictionary methods, but the code could certainly be more readable by using other strategies.
