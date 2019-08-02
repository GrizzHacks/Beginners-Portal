<h1>Tic-Tac-Toe Tutorial</h1>
<h2>Use this tutorial to learn some of the basics of Python</h2>
<h3><a href="https://www.geeksforgeeks.org/python-implementation-automatic-tic-tac-toe-game-using-random-number/">Source</a></h3>

<h3>We're going to playing Tic-Tac-Toe in our Terminal! While simple, this tutorial can serve as a launch point for more complex games or other projects.</h3>

<h2>Set-up</h2>
1) You'll need to start by downloading Python 3.7.X from <a href="https://www.python.org" target="_blank">Python.org</a>. Python can be downloaded for Windows, Linux, Mac, and other OS's. 
*NOTE*: This tutorial will take place on a Mac, so you may need to look up terminal commands for your own operating system.

2) After you've downloaded Python, we'll be able to run it from the terminal by typing `python3.7`. This opens up what is known as the python shell, and allows us to check our code and different commands right in the terminal. 
    - Go ahead and type `print("Hello World")` into the terminal. Congrats! You've just returned what we call a string. Strings are denoted by `''` or `"",` and are collections of alphanumeric characters. Learn more about strings <a href="https://www.w3schools.com/python/python_strings.asp" target="_blank">here.</a>
    - We'll exit out of the shell by typing `quit()`, but if you'd like to keep exploring, <a href="https://www.python-course.eu/python3_interactive.php" target="_blank"> this website</a> gives a nice overview of what you can do. 

3) Go ahead and open up a new file in your text editor. We'll name this file 'TicTacToe.py.' Be sure to save it to a location where you can find it later. Or save it so that you can share it to Github. 
    - You may be wondering: Are there any tools to help me program Python? There are! If you're using VS Code, feel free to look up python extensions and install any that you feel will be beneficial. 

<h2>Packages<h2>
    - For this tutorial, we'll be using three different packages/modules:
       - <a href="https://numpy.org">NumPy</a>
       - <a href="https://docs.python.org/2/library/random.html">Random</a>
       - <a href="https://docs.python.org/3/library/time.html">Time</a>
    <h3>NumPy</h3>
        - NumPy is able to do advanced scientific calculations and data analysis.  
        - Learn more about NumPy at <a href="https://numpy.org">numpy.org</a>. There are a number of tutorials, so it may be interesting to see what you can create outside of a game of Tic-Tac-Toe.
        - We'll need to install NumPy onto our computers. Opening the Terminal app, type in the command `sudo pip3 install numpy`. When prompted to type in a password, give the password you normally use when installing new software/are logging into the computer. 
    <h3>Random</h3>
        - Random gives us pseudo-random numbers for various calculations. 
        - Don't use it for security purposes, but if you wanted to generate random numbers in the future, this is your module.
        - The official <a href="https://docs.python.org/3/library/random.html">Python documentation</a> gives a good overview of how random works.
    <h3>Time</h3>
        - Time is a module which gives us access to time-related functions. 
        - Feel free to read up on the time module in the <a href="https://docs.python.org/3/library/time.html">official Python documentation</a>

<h2>Coding Our Game</h2>
    1) Lets take a look at our TicTacToe.py file. Looks a litte empty, right? Well, you know how we were discussing NumPy, Random, and Time? Let's create a way to use them in our file by typing
        import numpy as np
        import random
        from time import sleep
      
   There's a lot going on there, right? All we're really saying is "Hey, I want these packages/modules." So we bring them in through the keyword `import`. When we use the keyword `as,` we're telling the compilor "When I write np, I'm actually calling the NumPy package." As for `from,` we're selecting a specific function from the time module to import, rather than bringing in the entire thing.

   If you notice your system is unable to import numpy, make sure you've installed it correctly. An important part of being a programmer is knowing how to solve problems, including errors like this. Go to your favorite search engine and try to solve the issue. If you have difficulties, reach out to those around you.

   2) Awesome! The first step is done! Now comes the hard part: where do we start?



