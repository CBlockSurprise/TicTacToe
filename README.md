# Tic Tac Toe

Oh it's another duplicate of Tic Tac Toe, having completly normal features of: One Player, Two Player, and AI vs AI.

# Notes and Instructions

There may be some typos (in printing) and other stuff. Tic Tac Toe can work with it speaking, but you need pywin32 or pypiwin32. If you copy the code onto your computer:

Step 1: Go to Command Line, and if you have pip (if you don't, install it), enter `pip install pywin32`. If that does not work, enter `pip install pypiwin32`. if that does not work, do not move on to the next step. You can't have it speak sadly, but it still works.

Step 2: Once installed, go to the code that you copied and have on your programming compiler (with python set as programming language), go to the top and uncomment `import win32com.client as wincl` and `speak = wincl.Dispatch('SAPI.SpVoice')`. After, comment out `speak = Speaker("why u no have pywin32")`. It should work. If errors, just comment out the import line and the speak = wincl line, and uncomment speak = Speaker line. 


Also: A cats game is a tie.


# Layout

For playing, (when you are playing) it will ask you for a column and a row. You can refer to [layout.png](/layout.png) to see which one you choose. The first number is the column in it, and the second number is the row. It will only work if the number is between 1 and 3.

# Game Count

While starting the game, it will show how many games you play. All the numbers are going to be 0. It will never save. If you have it on your computer, it will save the count. *Note: Future me deleted the link to the online game. So you will have to  download it on your computer to play.*

# IMPORTANT

If you copy it onto your computer, you WILL NEED a file called 'tttfile.txt'. *Future me, coming back looking upon this project again, realized that past me had no idea what was a try and catch function was. Nice job.*

The file needs to be in the same folder as program.

# Just have some fun lol
