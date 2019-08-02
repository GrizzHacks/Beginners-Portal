# Tic-Tac-Toe Tutorial
>Use this tutorial to learn some of the basics of Python  
>[Reference](https://www.geeksforgeeks.org/python-implementation-automatic-tic-tac-toe-game-using-random-number/)

We're going to playing Tic-Tac-Toe in our Terminal! While simple, this tutorial can serve as a launch point for more complex games or other projects.

## Set-Up

1. You'll need to start by downloading Python 3.7.X from [Python.org](https://www.python.org) Python can be downloaded for Windows, Linux, Mac, and other OS's. 
*NOTE*: This tutorial will take place on a Mac, so you may need to look up terminal commands for your own operating system.

2. After you've downloaded Python, we'll be able to run it from the terminal by typing `python3.7`. This opens up what is known as the python shell, and allows us to check our code and different commands right in the terminal. 

    Go ahead and type `print("Hello World")` into the terminal. Congrats! You've just returned what we call a string. Strings are denoted by `''` or `"",` and are collections of alphanumeric characters. [Learn more about strings](https://www.w3schools.com/python/python_strings.asp)

    We'll exit out of the shell by typing `quit()`, but if you'd like to keep exploring, [this website](https://www.python-course.eu/python3_interactive.php) gives a nice overview of what you can do.

3. Go ahead and open up a new file in your text editor. We'll name this file 'TicTacToe.py.' Be sure to save it to a location where you can find it later. Or save it so that you can share it to Github. 

    You may be wondering: Are there any tools to help me program Python? There are! If you're using VS Code, feel free to look up python extensions and install any that you feel will be beneficial. 

## Packages

For this tutorial, we'll be using three different packages/modules:

- [NumPy](https://numpy.org)
- [Random](https://docs.python.org/2/library/random.html)
- [Time](https://docs.python.org/3/library/time.html)

### NumPy
- NumPy is able to do advanced scientific calculations and data analysis.
- Learn more about NumPy at [numpy.org.](https://numpy.org) There are a number of tutorials, so it may be interesting to see what you can create outside of a game of Tic-Tac-Toe.
- We'll need to install NumPy onto our computers. Opening the Terminal app, type in the command `sudo pip3 install numpy`. When prompted to type in a password, give the password you normally use when installing new software/are logging into the computer.

### Random
- Random gives us pseudo-random numbers for various calculations.
- Don't use it for security purposes, but if you wanted to generate random numbers in the future, this is your module. 
- The official [Python documentation](https://docs.python.org/3/library/random.html) gives a good overview of how random works.

### Time
- Time is a module which gives us access to time-related functions.
- Feel free to read up on the time module in the [official Python documentation(https://docs.python.org/3/library/time.html)

## Coding Our Game
### Lets take a look at our TicTacToe.py file. 

Looks a litte empty, right? Well, you know how we were discussing NumPy, Random, and Time? Let's create a way to use them in our file by typing 

```python
import numpy as np
import random from time
import sleep
```