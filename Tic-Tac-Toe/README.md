# Tic-Tac-Toe Tutorial
>Use this tutorial to learn some of the basics of Python  
>[See the Original Tutorial](https://www.geeksforgeeks.org/python-implementation-automatic-tic-tac-toe-game-using-random-number/)

We're going to creating an automated game of Tic-Tac-Toe in our Terminal! While simple, this tutorial can serve as a launch point for more complex games or other projects.

## Set-Up

1. You'll need to start by downloading Python 3.7.X from [Python.org](https://www.python.org) Python can be downloaded for Windows, Linux, Mac, and other OS's. 
*NOTE*: This tutorial will take place on a Mac, so you may need to look up terminal commands for your own operating system.

2. After you've downloaded Python, we'll be able to run it from the terminal by typing `python3.7`. This opens up what is known as the python shell, and allows us to check our code and different commands right in the terminal. 

    Go ahead and type `print("Hello World")` into the terminal. Congrats! You've just returned what we call a string. Strings are denoted by `''` or `"",` and are collections of alphanumeric characters. [Learn more about strings](https://www.w3schools.com/python/python_strings.asp)

    We'll exit out of the shell by typing `quit()`, but if you'd like to keep exploring, [this website](https://www.python-course.eu/python3_interactive.php) gives a nice overview of what you can do.

3. Go ahead and open up a new file in your text editor. We'll name this file 'TicTacToe.py.' Save it to a location where you can find it later by clicking 'File -> Save,' renaming it, and changing the save location to the file where your Github Repository is located, or your Desktop, or etc...

    You may be wondering: Are there any tools to help me program Python? There are! If you're using VS Code, feel free to look up python extensions and install any that you feel will be beneficial. 

## Packages

For this tutorial, we'll be using three different packages/modules:

- [NumPy](https://numpy.org)
- [Random](https://docs.python.org/2/library/random.html)
- [Time](https://docs.python.org/3/library/time.html)

### NumPy
- NumPy is able to do advanced scientific calculations and data analysis.
- Learn more about NumPy at [numpy.org.](https://numpy.org) There are a number of tutorials, so it may be interesting to see what you can create outside of a game of Tic-Tac-Toe.
- We'll need to install NumPy onto our computers. Opening the Terminal, type in the command `sudo pip3 install numpy`. When prompted to type in a password, give the password you normally use when installing new software/are logging into the computer.
>You will not see the passwork line expand as you type in your password. 

### Random
- Random gives us pseudo-random numbers for various calculations.
- Don't use it for security purposes, but if you wanted to generate random numbers in the future, this is your module. 
- The official [Python documentation](https://docs.python.org/3/library/random.html) gives a good overview of how random works.

### Time
- Time is a module which gives us access to time-related functions.
- Feel free to read up on the time module in the [official Python documentation](https://docs.python.org/3/library/time.html)

## Coding Our Game
### Lets take a look at our TicTacToe.py file. 

Looks a litte empty, right? Well, you know how we were discussing NumPy, Random, and Time? Let's create a way to use them in our file by typing 

```python
import numpy as np
import random 
from time import sleep
```
Copy the code exactly as shown in the grey box. Make sure to do the same whenever you see a grey box.

#### __What We've Learned__
- In this section, we're saying "Hey, I want these packages/modules." We can bring them in through the keyword `import`. 
- When we use the keyword `as,` we're telling the compilor "When I write np, I'm actually calling the NumPy package." 
- Using `from,` we're selecting a specific function from the time module to import, rather than bringing in the entire thing.

>If you notice your system is unable to import numpy, make sure you've installed it correctly. An important part of being a programmer is knowing how to solve problems including errors like this. Go to your favorite search engine and try to solve the issue. If you have difficulties, reach out to those around you.

### Awesome! The first step is done!

Now comes the hard part: where do we start?

Let's think: what do we need to play Tic-Tac-Toe?
>Since this game is automated - meaning there is no user input - we don't need to factor in indivdual decisions. Everything is done by the computer

1) We need a 3x3 grid
2) We need to make sure spaces are empty, and that a virtual player can place their piece there 
3) We need to randomly determine where a player places their piece
4) We need to display if the score is a win, loose, or draw for the player and for which player

That seems like a pretty good list. We can always come back and add things on.

### Let's make our 3x3 grid

We're going to write a Python function in order to make our grid. Functions are recognized by the `def` keyword. We use functions to perform specific calculations, keep our code organized, and avoid certain code from running when it isn't needed.
>[Learn More About Python Functions](https://www.tutorialspoint.com/python3/python_functions) 

Let's write this function under where we imported our modules/package:

```python
def create_board():
    return(np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]]))
```

Make sure the `def` keywork is flush with the left-hand side and the `return` statement is indented one tab. Each time you see a new function, you'll need to make sure `def` is flush with the left-hand side and the following line is indented one tab. Otherwise, you'll get an error when you run the program. 

#### __What We've Learned__

- `create_board()` is the name of our function, and what we'll use to 'call' the function later on.  
    - Functions are weird in that if we don't specify a `return` statement inside of them,they won't give us anything back. [This website](https://www.python-course.eu/python3_functions.php) gives a great overview of how `return` works and why we need it.
>Functions don't actually do anything when we run a file, unless we call them. We'll see this in action later on.

### Great! Now, let's check which spaces on the board are empty, and assign a random position for a player

Because we're doing two tasks, let's create two functions. Our first function will check which spaces on the board are empty. The nifty thing is is that this function can be used later on when determining which spaces the player can choose as the board becomes more full.

Write the function below into TicTacToe.py:

```python
def empty_spaces(board):
    available = []

    for row in range(len(board)):
        for column in range(len(board)):

            if board[row][column] == 0:
                available.append((row, column))
    
    return(available)
```
#### __What We've Learned__

- Our function `empty_spaces()` is accepting a parameter called `board`. This represents our tic-tac-toe board/array. However, the cool thing is, we didn't actually need to call it `board.` We could just as easily have called it `cat` or `gamespace.` 
- The first line in the function is creating an empty list called `available.` Lists are enormously useful in storing information. 
    - We see this information storage happening in the `if` statement through the `append()` function. 
    >[Read more about Python lists](https://www.w3schools.com/python/python_lists.asp)
- After our list creation, we see a nested `for` loop (two or more `for` loops together). There's a lot of new information here.
    - `row` and `column` are completely arbitrary. You'll typically see these variables represented as `i` and `j`. 
    - The first `for` loop says that 'for each row (the [0,0,0] in our array) in the range of 0 - number of rows in our array (`len(board)`), do this:"
        > Numbering in programming languages is a bit weird. While we define the first row as 1 and the last as 3, Python sees it as row 0 to row 2. 
    - The second `for` loop says 'for each column (the 0 in a row) in the range of 0 - number of columns (# of 0's), do this:"
        > The numbering characteristic seen with the rows is also seen with the columns; so the first 0 is numbered '0,' while the last is numbered '2'
    - Our `if` statement says "if the space in `board` corresponding to coordinate (row, column) is equivalent to 0, then we will add it to our available list.
        > Coordinates move from left to right and top to bottom. So our array has the coordinates of  
        >(0,0) | (0,1) | (0,2)  
        >(1,0) | (1,1) | (1,2)  
        >(2,0) | (2,1) | (2,2)
    - Then, we move all of the available options out of the function with the `return` statement for use elsewhere in the project.

That's confusing, right? [This website](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3) does a good job of covering `for` loops, and gives more information about the nested `for` loop. If you're still unsure of what is going on, feel free to look up more tutorials and ask for help. Programming is a learning game!

The `if` statement is also new. [This site](https://www.w3schools.com/python/python_conditions.asp) gives an overview of conditionals and `if` statements. 

#### Take a quick break, then come back to work on the next function.

All set? Remember, it's okay to ask for help. This stuff is confusing, and we only have 24 hours. Make the most of the people around you and online tutorials.

Let's assign a random position for the player. This function will work no matter whether it's the first move, or the final move.

Type 

```python
def random_position(board, player):
    selection = empty_spaces(board)
    determined_location = random.choice(selection)
    board[determined_location] = player
    
    return(board)
```
into the file. 

#### __What We've Learned__

- This function is called `random_position()` and accepts two parameters: `board` and `player`. Respectively, they represent the gameboard and which player is making their move.
- `selection = empty_spaces(board)` is calling our `empty_spaces()` function, and assigning its result to the variable `selection`. 
    - Notice how we have `board` in-between the parenthesis? We need to do this because `empty_spaces()` is expecting a variable, known in this context as an argument.  
        >This is seen when we define `empty_spaces(board)` 
    - We're only able to assign a value to selection because we have a `return` statement in our `empty_spaces()` function. In this case, we are assigning `selection` to a list of the empty spaces in the board.
- The next line uses the random module. We call random's `choice()` function to randomly select one of the empty spaces in the board, which all come from the `selection` variable. The specific tile that was chosen is then assigned to the `determined_location` variable.
- Our final, non-return line says "Place the respective player token at the spot that was randomly selected in the above lines"
    > This ultimately determines what we see printed in the terminal when we run the program.
- Finally, we return `board` to whatever called the `random_position()` function.

### Wonderful! Now we just need to figure out whether a player has won, lost, or drawn with their opponent.

How many ways can a player win?  
- Three marks in a horizontal row
- Three marks in a vertical row
- Three marks in a diagnoal row

We'll have to program functions to check for each of these possibilities. Let's tackle the vertical row:

```python
def col_win(board, player):
    for row in range(len(board)):
        win = True

        for column in range(len(board)):
            if board[column][row] != player:
                win = False
                continue

        if win == True:
            return(win)

    return(win)
```

#### __What We've Learned__

Using what you've learned, can you figure out what's going on? 
- The new information we see is the `continue` statement, which returns to the top of the loop (in this case the second `for` loop) and ignores any remaining statements. 
- Remember, `return()` ends the execution of a function. So if an entire column contains the same player marker, we make sure `True` is passed out of the function. 
>If you can't quite understand what's happening, trying drawing it out. Remember, `win` is a variable assigned to the boolean `True`. If at any point a space in the column is not the required player marker, win will be set to `False` for the entire column. 

------

Now let's work on determining if there are three of the same mark in a horizontal row:

```python
def row_win(board, player):
    for row in range(len(board)):
        win = True

        for column in range(len(board)):
            if board[row, column] != player:
                win = False
                continue
            
        if win == True:
            return(win)
    return(win)
```

#### __What We've Learned__
- Notice how our `if` statement is slightly different this time around? We're only able to check a tile using `board[row, column]` because of NumPy. Otherwise, we would only be able to do this via `board[row][column]`.
- Make sure you understand how this section of code works, and then move on to programming the diagonal row checker.

----

Finally, let's see if the player has filled a diagonal section of the board:

```python
def diag_win(board, player):
    win = True

    for tile in range(len(board)):
        if board[tile, tile] != player:
            win = False
    return(win)
```

#### __What We've Learned__
- Try to understand why we only need one return statement in this function. If it's difficult, that's okay. Try visualizing the process on paper, or asking a friend.
- Everything else we have seen before, but if you still struggling to understand, work through the earlier sections again, or ask a friend for help.

### Finally, it's time to decide if there is a winner, or if we have a CATS (tie) game. Remember, our functions above didn't actually tell us if and who the winner was, only if the same player marker was in a winning orientation

```python
def evaluation(board):
    winner = 0

    for player in [1, 2]:
        if (col_win(board, player) or row_win(board, player) or diag_win(board, player)):
            winner = player
        
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
```
#### __What We've Learned__
- See those `or` and `and` statements? Those are known as [logical operators](https://www.programiz.com/python-programming/operators). 
    - `or` gives us the ability to return the boolean value `True` if one of the three functions returns `True`. If we get a `True` value, then we assign the player value (either `1` or `2`) to the `winner` variable. 
    - `and` returns `True` ONLY when all the conditions are satisfied; in this case, all of the tiles on the board are not equal to zero, and the `winner` variable equals 0. 

### Great. We've got all of these functions. So how do we actually make them do anything?
In order for our game to actually work, we need to call the functions (we say this same procedure done in the `random_position()` function). We can create an overarching function to do this for us.

```python
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = random_position(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluation(board)
            if winner != 0:
                break
    return(winner)
```
#### __What We've Learned__
Can you figure out what's going on?
- We can assign values to multiple variables at a time. On the first line, board gets assigned the `return` value of the create_board() function, `winner` = 0, and `counter` = 1
- Remember importing `time`? We're finally using the `sleep` function to delay the program for 2 seconds
- `while` loops are new. They say to the computer that while a condition is true, continue to run the code. [Learn more about while loops](https://www.w3schools.com/python/python_while_loops.asp)
- Using `+` statements in a `print` statement is known as [concatenation](https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python).
It allows us insert variables into a string easily. 
>We need to use `str` to convert an integer into a string. Try using the Python shell and write a small `print` statement without `str` to see what happens if it's missing.
-`break` in a new keywork that terminates a loop. In this case, if we reach `break`, we will exit our `for` loop, and the `while` loop will stop automatically because `winner` is no longer 0.

### Finally, we need to actually run all of this code. This can only be done outside of a function in the main file.

Type this final line of code below all of the functions, flush all the way to the left.

```python
print("Winner is: " + str(play_game()))
```

## Running the game

Go ahead and look through your code. See if there are any noticable issues that the text editor has picked up for you. If not, be sure to save the file. Now, let's test our code!

To do this, we need to navigate to where our code is stored on our computer.   
- Open your terminal, and make sure you're not in the Python shell (remember, we can exit out of it by typing `quit()`)
- You'll want to type `cd` then the path to reach your file. So, if it's on your desktop, you'd type `cd Desktop`. If it's in your Documents, you'd type `cd Documents`. 
>For me, I have it in a folder on my desktop called "Beginners-Portal". I'll type `cd Desktop/Beginners-Portal/Beginners-Portal/Tic-Tac-Toe` to reach the location where I have TicTacToe.py stored.
>Do a quick internet search if you're still unclear on how to navigate to your file's location.
- You can check if TicTacToe.py is there by typing `ls,` which lists all the files and folders in a given location. Look for "TicTacToe.py"
- Finally, you'll type `python3.7 TicTacToe.py` into the Terminal, and vola!

### Difficulties

If you find the code doesn't run, see what type of error the terminal gives you. See if you can figure out where in the code you've made a mistake, and otherwise take to the internet to see if you can figure it out. Programming is all about problem solving. I know you can do it!

## Next steps

You've done it! You've programmed an automated game of Tic-Tac-Toe! Think of all you can do with your new-found knowledge. Here are some ideas to get you started:
- This game is a little slow. Can you figure out a way to speed it up?
- If the game ends up in a tie, we get "Winner is: -1". What does that mean? Can you change this output to something more meaningful?
- Try to make a game of Tic-Tac-Toe that is interactive. Look at how to get user input, store information, and allow for multiple players.
- Make a new game. Try Connect 4, or Mancala. Now that you've picked up some of the basics, there is an endless world of possibilities in front of you.

# Good luck Hackers!

------

##### This code comes from the source listed at the top of the page. No commercial gain is sought from using the code, and is instead intended for educational purposes. 
