# TicTacToe

This is Tic Tac Toe, featuring: One Player, Two Player, and AI vs AI!
It is confusing (for me since there is over 900 lines of code) to have it in html, so it is on ???

# Notes and Instructions

There may be some typos (in printing) and other stuff. Tic Tac Toe can work with it speaking, but you need pywin32 or pypiwin32. If you copy the code onto your computer:

Step 1: Go to Command Line, and if you have pip (if you don't, install it), enter 'pip install pywin32'. If that does not work, enter 'pip install pypiwin32' if that does not work, do not move on to the next step. You can't have it speak sadly, but it still works.

Step 2: Once installed, go to the code that you copied and have on your programming compiler (with python set as programming language), go to the top and uncomment 'import win32com.client as wincl' and 'speak = wincl.Dispatch('SAPI.SpVoice')'. After, comment out 'speak = Speaker("why u no have pywin32")'. It should work. If errors, just comment out the import line and the speak = wincl line, and uncomment speak = Speaker line. 

Also: Cats game is a tie. I just call it that.
