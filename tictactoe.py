import random
from time import sleep
import webbrowser
#Comment the next two lines out if this computer does NOT support pywin32
#import win32com.client as wincl
#speak = wincl.Dispatch('SAPI.SpVoice')

class Speaker:
    def __init__(self, thatsit):
        self.tsi = thatsit
    def Speak(self, newstringthati):
        self.tsil = newstringthati
        self.i = 0
        self.addwait = 0
        for i in range(len(list(self.tsil))):
            self.addwait += 0.04
        sleep(self.addwait)
            

#This is for computers that can NOT support pywin32
speak = Speaker("why u no have pywin32")

line1 = ["-","-","-"]
line2 = ["-","-","-"]
line3 = ["-","-","-"]
aigamesn = 0
ply1games = 0
ply2games = 0
totalgamescount = 0
cask = 0
rask = 0
win = False

def printBoard():
    print("-------------------")
    print(line1[0], line1[1], line1[2])
    print(line2[0], line2[1], line2[2])
    print(line3[0], line3[1], line3[2])

def askNums():
    speak.Speak("Which column?")
    colum = int(input("Which column? "))
    
    while colum < 1 or colum > 3:
        speak.Speak("That is not valid. Please make it be between 1 - 3. Which column?")
        colum = int(input("That is not valid. Please make it be between 1 - 3. Which column? "))

    
    return colum

def askNums2():
    speak.Speak("Which row?")
    row = int(input("Which row? "))
    
    
    while row < 1 or row > 3:
        speak.Speak("That is not valid. Please make it be between 1 - 3. Which row? ")
        row = int(input("That is not valid. Please make it be between 1 - 3. Which row? "))
    
    return row

def reset():
    line1 = ["-","-","-"]
    line2 = ["-","-","-"]
    line3 = ["-","-","-"]
    
    win = False
    main()

def catsGame():
    
    if line1[0] == "X" or line1[0] == "O":
        if line1[1] == "X" or line1[1] == "O":
            if line1[2] == "X" or line1[2] == "O":
                if line2[0] == "X" or line2[0] == "O":
                    if line2[1] == "X" or line2[1] == "O":
                        if line2[2] == "X" or line2[2] == "O":
                            if line3[0] == "X" or line3[0] == "O":
                                if line3[1] == "X" or line3[1] == "O":
                                    if line3[2] == "X" or line3[2] == "O":
                                        return True
    return False
    
    


def isFilled(num1,num2):
    if num1 == 1:
        if line1[num2 - 1] != "-":
            return True
    elif num1 == 2:
        if line2[num2 - 1] != "-":
            return True
    elif num1 == 3:
        if line3[num2 - 1] != "-":
            return True
    return False


def hasWon():
    #LineOne full
    if line1[0] == "O":
        if line1[1] == "O":
            if line1[2] == "O":
                return True
    #Diagiangol topl to bottomr
    if line1[0] == "O":
        if line2[1] == "O":
            if line3[2] == "O":
                return True
    #LineTwo full
    if line2[0] == "O":
        if line2[1] == "O":
            if line2[2] == "O":
                return True
    #Diagiangol topr to bottoml
    if line1[2] == "O":
        if line2[1] == "O":
            if line3[0] == "O":
                return True
    #line3 full
    if line3[0] == "O":
        if line3[1] == "O":
            if line3[2] == "O":
                return True
    #jk i'm stopping with dat
    if line1[0] == "O":
        if line2[0] == "O":
            if line3[0] == "O":
                return True
    if line1[1] == "O":
        if line2[1] == "O":
            if line3[1] == "O":
                return True
    if line1[2] == "O":
        if line2[2] == "O":
            if line3[2] == "O":
                return True
    #For X LineOne full
    if line1[0] == "X":
        if line1[1] == "X":
            if line1[2] == "X":
                return True
    #Diagiangol topl to bottomr
    if line1[0] == "X":
        if line2[1] == "X":
            if line3[2] == "X":
                return True
    #LineTwo full
    if line2[0] == "X":
        if line2[1] == "X":
            if line2[2] == "X":
                return True
    #Diagiangol topr to bottoml
    if line1[2] == "X":
        if line2[1] == "X":
            if line3[0] == "X":
                return True
    #line3 full
    if line3[0] == "X":
        if line3[1] == "X":
            if line3[2] == "X":
                return True
    #jk i'm stopping with dat
    if line1[0] == "X":
        if line2[0] == "X":
            if line3[0] == "X":
                return True
    if line1[1] == "X":
        if line2[1] == "X":
            if line3[1] == "X":
                return True
    if line1[2] == "X":
        if line2[2] == "X":
            if line3[2] == "X":
                return True
    return False

def twoinrow():
    if line1[0] == "X":
        if line1[1] == "X" and line1[2] == "-":
            return True
    if line1[2] == "X":
        if line1[1] == "X" and line1[0] == "-":
            return True
    if line1[0] == "X":
        if line1[2] == "X" and line1[1] == "-":
            return True
    #--
    if line2[0] == "X":
        if line2[1] == "X" and line2[2] == "-":
            return True
    if line2[2] == "X":
        if line2[1] == "X" and line2[0] == "-":
            return True
    if line2[0] == "X":
        if line2[2] == "X" and line2[1] == "-":
            return True
    #--
    if line3[0] == "X":
        if line3[1] == "X" and line3[2] == "-":
            return True
    if line3[2] == "X":
        if line3[1] == "X" and line3[0] == "-":
            return True
    if line3[0] == "X":
        if line3[2] == "X" and line3[1] == "-":
            return True
    #--
    if line1[0] == "X":
        if line2[0] == "X" and line3[0] == "-":
            return True
    if line2[0] == "X":
        if line3[0] == "X" and line1[0] == "-":
            return True
    if line1[0] == "X":
        if line3[0] == "X" and line2[0] == "-":
            return True
    #--
    if line1[1] == "X":
        if line2[1] == "X" and line3[1] == "-":
            return True
    if line2[1] == "X":
        if line3[1] == "X" and line1[1] == "-":
            return True
    if line1[1] == "X":
        if line3[1] == "X" and line2[1] == "-":
            return True
    #--
    if line1[2] == "X":
        if line2[2] == "X" and line3[2] == "-":
            return True
    if line2[2] == "X":
        if line3[2] == "X" and line1[2] == "-":
            return True
    if line1[2] == "X":
        if line3[2] == "X" and line2[2] == "-":
            return True
    #--
    if line1[0] == "X":
        if line3[2] == "X" and line2[1] == "-":
            return True
    if line1[2] == "X":
        if line3[0] == "X" and line2[1] == "-":
            return True
    ##---
    if line1[0] == "X":
        if line2[1] == "X" and line3[2] == "-":
            return True
    if line2[1] == "X":
        if line3[2] == "X" and line1[0] == "-":
            return True
    ##----
    if line1[2] == "X":
        if line2[1] == "X" and line3[0] == "-":
            return True
    if line2[1] == "X":
        if line3[0] == "X" and line1[2] == "-":
            return True
    return False

def whrtwoinrow():
    if line1[0] == "X":
        if line1[1] == "X" and line1[2] == "-":
            return [1,3]
    if line1[2] == "X":
        if line1[1] == "X" and line1[0] == "-":
            return [1,1]
    if line1[0] == "X":
        if line1[2] == "X" and line1[1] == "-":
            return [1,2]
    #--
    if line2[0] == "X":
        if line2[1] == "X" and line2[2] == "-":
            return [2,3]
    if line2[2] == "X":
        if line2[1] == "X" and line2[0] == "-":
            return [2,1]
    if line2[0] == "X":
        if line2[2] == "X" and line2[1] == "-":
            return [2,2]
    #--
    if line3[0] == "X":
        if line3[1] == "X" and line3[2] == "-":
            return [3,3]
    if line3[2] == "X":
        if line3[1] == "X" and line3[0] == "-":
            return [3,1]
    if line3[0] == "X":
        if line3[2] == "X" and line3[1] == "-":
            return [3,2]
    #--
    if line1[0] == "X":
        if line2[0] == "X" and line3[0] == "-":
            return [3,1]
    if line2[0] == "X":
        if line3[0] == "X" and line1[0] == "-":
            return [1,1]
    if line1[0] == "X":
        if line3[0] == "X" and line2[0] == "-":
            return [2,1]
    #--
    if line1[1] == "X":
        if line2[1] == "X" and line3[1] == "-":
            return [3,2]
    if line2[1] == "X":
        if line3[1] == "X" and line1[1] == "-":
            return [1,2]
    if line1[1] == "X":
        if line3[1] == "X" and line2[1] == "-":
            return [2,2]
    #--
    if line1[2] == "X":
        if line2[2] == "X" and line3[2] == "-":
            return [3,3]
    if line2[2] == "X":
        if line3[2] == "X" and line1[2] == "-":
            return [1,3]
    if line1[2] == "X":
        if line3[2] == "X" and line2[2] == "-":
            return [2,3]
    #--
    if line1[0] == "X":
        if line3[2] == "X" and line2[1] == "-":
            return [2, 2]
    if line1[2] == "X":
        if line3[0] == "X" and line2[1] == "-":
            return [2, 2]
    ##---
    if line1[0] == "X":
        if line2[1] == "X" and line3[2] == "-":
            return [3, 3]
    if line2[1] == "X":
        if line3[2] == "X" and line1[0] == "-":
            return [1, 1]
    ##----
    if line1[2] == "X":
        if line2[1] == "X" and line3[0] == "-":
            return [3, 1]
    if line2[1] == "X":
        if line3[0] == "X" and line1[2] == "-":
            return [1, 3]
    ##row colum

def twoinrowwin():
    if line1[0] == "O":
        if line1[1] == "O":
            return True
    if line1[2] == "O":
        if line1[1] == "O":
            return True
    if line1[0] == "O":
        if line1[2] == "O":
            return True
    #--
    if line2[0] == "O":
        if line2[1] == "O":
            return True
    if line2[2] == "O":
        if line2[1] == "O":
            return True
    if line2[0] == "O":
        if line2[2] == "O":
            return True
    #--
    if line3[0] == "O":
        if line3[1] == "O":
            return True
    if line3[2] == "O":
        if line3[1] == "O":
            return True
    if line3[0] == "O":
        if line3[2] == "O":
            return True
    #--
    if line1[0] == "O":
        if line2[0] == "O":
            return True
    if line2[0] == "O":
        if line3[0] == "O":
            return True
    if line1[0] == "O":
        if line3[0] == "O":
            return True
    #--
    if line1[1] == "O":
        if line2[1] == "O":
            return True
    if line2[1] == "O":
        if line3[1] == "O":
            return True
    if line1[1] == "O":
        if line3[1] == "O":
            return True
    #--
    if line1[2] == "O":
        if line2[2] == "O":
            return True
    if line2[2] == "O":
        if line3[2] == "O":
            return True
    if line1[2] == "O":
        if line3[2] == "O":
            return True
    #--
    if line1[0] == "O":
        if line3[2] == "O":
            return True
    if line1[2] == "O":
        if line3[0] == "O":
            return True
    ##---
    if line1[0] == "O":
        if line2[1] == "O":
            return True
    if line2[1] == "O":
        if line3[2] == "O":
            return True
    ##----
    if line1[2] == "O":
        if line2[1] == "O":
            return True
    if line2[1] == "O":
        if line3[0] == "O":
            return True
    return False

def whrtwoinrowwin():
    if line1[0] == "O":
        if line1[1] == "O":
            return [1,3]
    if line1[2] == "O":
        if line1[1] == "O":
            return [1,1]
    if line1[0] == "O":
        if line1[2] == "O":
            return [1,2]
    #--
    if line2[0] == "O":
        if line2[1] == "O":
            return [2,3]
    if line2[2] == "O":
        if line2[1] == "O":
            return [2,1]
    if line2[0] == "O":
        if line2[2] == "O":
            return [2,2]
    #--
    if line3[0] == "O":
        if line3[1] == "O":
            return [3,3]
    if line3[2] == "O":
        if line3[1] == "O":
            return [3,1]
    if line3[0] == "O":
        if line3[2] == "O":
            return [3,2]
    #--
    if line1[0] == "O":
        if line2[0] == "O":
            return [3,1]
    if line2[0] == "O":
        if line3[0] == "O":
            return [1,1]
    if line1[0] == "O":
        if line3[0] == "O":
            return [2,1]
    #--
    if line1[1] == "O":
        if line2[1] == "O":
            return [3,2]
    if line2[1] == "O":
        if line3[1] == "O":
            return [1,2]
    if line1[1] == "O":
        if line3[1] == "O":
            return [2,2]
    #--
    if line1[2] == "O":
        if line2[2] == "O":
            return [3,3]
    if line2[2] == "O":
        if line3[2] == "O":
            return [1,3]
    if line1[2] == "O":
        if line3[2] == "O":
            return [2,3]
    #--
    if line1[0] == "O":
        if line3[2] == "O":
            return [2, 2]
    if line1[2] == "O":
        if line3[0] == "O":
            return [2, 2]
    ##---
    if line1[0] == "O":
        if line2[1] == "O":
            return [3, 3]
    if line2[1] == "O":
        if line3[2] == "O":
            return [1, 1]
    ##----
    if line1[2] == "O":
        if line2[1] == "O":
            return [3, 1]
    if line2[1] == "O":
        if line3[0] == "O":
            return [1, 3]
    ##row colum

##///
def player1():
    global ply1games
    print("You are: X")
    speak.Speak("You are: X")
    printBoard()
    while not win:
        if catsGame():
            ply1games += 1
            writefiles()
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return
        print("Your turn.")
        speak.Speak("Your turn.")
        cask = askNums()
        rask = askNums2()
        while isFilled(rask, cask):
            printBoard()
            print("That is filled. Please pick something else.")
            speak.Speak("That is filled. Please pick something else.")
            cask = askNums()
            rask = askNums2()
        
        if rask == 1:
            line1[cask - 1] = "X"
        elif rask == 2:
            line2[cask - 1] = "X"
        else:
            line3[cask - 1] = "X"
        rask = 0
        cask = 0
        printBoard()
        if hasWon():
            ply1games += 1
            writefiles()
            print("You win!")
            speak.Speak("You win!")
            replay()
            return
        if catsGame():
            ply1games += 1
            writefiles()
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return
            
        print("Opponet's turn.")
        speak.Speak("Opponet's turn.")
        if catsGame():
            ply1games += 1
            writefiles()
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return
        toctw = False
        toctwn = False
        if twoinrowwin():
            whrtogowin = whrtwoinrowwin()
            cask = whrtogowin[1]
            rask = whrtogowin[0]
            toctwn = True
        if toctwn == True:
            if isFilled(rask, cask):
                toctw = False
            else:
                toctw = True
        if toctw == False:
            if twoinrow():
                whrtogo = whrtwoinrow()
                cask = whrtogo[1]
                rask = whrtogo[0]
            else:
                cask = random.randint(1,3)
                rask = random.randint(1,3)
            while isFilled(rask, cask):
                printBoard()
                print("Filled. Choosing other...")
                speak.Speak("Filled. Choosing other...")
                cask = random.randint(1,3)
                rask = random.randint(1,3)
        
        if rask == 1:
            line1[cask - 1] = "O"
        elif rask == 2:
            line2[cask - 1] = "O"
        else:
            line3[cask - 1] = "O"
        rask = 0
        cask = 0
        printBoard()
        if hasWon():
            ply1games += 1
            writefiles()
            print("You Lose...")
            speak.Speak("You Lose...")
            webbrowser.open_new_tab("https://www.flickr.com/photos/jimyounkin/5059286742")
            
            replay()
            return
        if catsGame():
            ply1games += 1
            writefiles()
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return

def aiai():
    global aigamesn
    print("Ai one: X, Ai two: O")
    speak.Speak("Ai one: X, Ai two: O")
    printBoard()
    while not win:
        if catsGame():
            aigamesn += 1
            writefiles()
            print("Results: Cats game")
            speak.Speak("Results: Cats game.")
            replay()
            return
        print("Ai one's turn.")
        speak.Speak("Ai one's turn.")
        cask = random.randint(1,3)
        rask = random.randint(1,3)
        while isFilled(rask, cask):
            printBoard()
            print("Filled. Choosing other...")
            speak.Speak("Filled. Choosing other...")
            cask = random.randint(1,3)
            rask = random.randint(1,3)
        
        if rask == 1:
            line1[cask - 1] = "X"
        elif rask == 2:
            line2[cask - 1] = "X"
        else:
            line3[cask - 1] = "X"
        rask = 0
        cask = 0
        printBoard()
        if hasWon():
            aigamesn += 1
            writefiles()
            print("Results: Ai one wins, Ai two loses")
            speak.Speak("Results: Ai one wins, Ai two loses")
            replay()
            return
        if catsGame():
            aigamesn += 1
            writefiles()
            print("Results: Cats game")
            speak.Speak("Results: Cats game.")
            replay()
            return
            
        print("Ai two's turn.")
        speak.Speak("Ai two's turn.")
        if catsGame():
            aigamesn += 1
            writefiles()
            print("Results: Cats game")
            speak.Speak("Results: Cats game.")
            replay()
            return
        cask = random.randint(1,3)
        rask = random.randint(1,3)
        while isFilled(rask, cask):
            printBoard()
            print("Filled. Choosing other...")
            speak.Speak("Filled. Choosing other...")
            cask = random.randint(1,3)
            rask = random.randint(1,3)
        
        if rask == 1:
            line1[cask - 1] = "O"
        elif rask == 2:
            line2[cask - 1] = "O"
        else:
            line3[cask - 1] = "O"
        rask = 0
        cask = 0
        printBoard()
        if hasWon():
            aigamesn += 1
            writefiles()
            print("Results: Ai two wins, Ai one loses")
            speak.Speak("Results: Ai two wins, Ai one loses") 
            replay()
            return
        if catsGame():
            aigamesn += 1
            writefiles()
            print("Results: Cats game")
            speak.Speak("Results: Cats game.")
            replay()
            return

def backreplay():
    replay()

def replay():
    print("Do you want to play again? Type in exatcly 'play', or to play google's version, type in 'tictactoe'")
    speak.Speak("Do you want to play again? Type in exatcly 'play', or to play google's version, type in 'tictactoe'")
    choicereplay = input("> ")
    if choicereplay == "play":
        print("Starting...")
        reset()
        main()
        return
    elif choicereplay == "tictactoe":
        print("Loading...")
        speak.Speak("Opening page...")
        sleep(1)
        webbrowser.open_new_tab("https://www.google.com/search?q=tic+tac+toe&rlz=1C1GCEA_enUS780US780&oq=tic+tac+toe&aqs=chrome..69i57j0l5.3692j0j7&sourceid=chrome&ie=UTF-8")
        backreplay()
        return
    else:
        print("Stopping...")
        print("Thanks for playing! This is made by Jaiden.")
        speak.Speak("Thanks for playing! This is made by Jaiden.")
        return

def player2():
    global speak
    global ply2games
    print("Decide which player are you (1 or 2). It will be a random choice of who goes first. You have 5 seconds")
    speak.Speak("Decide which player are you (1 or 2). It will be a random choice of who goes first. You have 5 seconds")
    plyxstr = "a"
    plyostr = "a"
    sleep(5)
    wpgf = random.randint(1,2)
    if wpgf == 1:
        print("Player 1 goes first. Player 1 is X, and Player 2 is O.")
        speak.Speak("Player 1 goes first. Player 1 is X, and Player 2 is O.")
        plyxstr = "Player 1's turn."
        plyostr = "Player 2's turn."
    elif wpgf == 2:
        print("Player 2 goes first. Player 1 is O, and Player 2 is X.")
        speak.Speak("Player 2 goes first. Player 1 is O, and Player 2 is X.")
        plyxstr = "Player 2's turn."
        plyostr = "Player 1's turn."
    printBoard()
    while not win:
        if catsGame():
            ply2games += 1
            writefiles()
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return
        print(plyxstr)
        speak.Speak(plyxstr)
        cask = askNums()
        rask = askNums2()
        while isFilled(rask, cask):
            printBoard()
            print("That is filled. Please pick something else.")
            speak.Speak("That is filled. Please pick something else.")
            cask = askNums()
            rask = askNums2()
        
        if rask == 1:
            line1[cask - 1] = "X"
        elif rask == 2:
            line2[cask - 1] = "X"
        else:
            line3[cask - 1] = "X"
        rask = 0
        cask = 0
        printBoard()
        if hasWon():
            ply2games += 1
            writefiles()
            if wpgf == 1:
                print("Player 1 has won, and Player 2 has lost.")
                speak.Speak("Player 1 has won, and Player 2 has lost.")
            else:
                print("Player 2 has won, and Player 1 has lost.")
                speak.Speak("Player 2 has won, and Player 1 has lost.")
            replay()
            return
        if catsGame():
            ply2games += 1
            writefiles()
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return
        
        print(plyostr)
        speak.Speak(plyostr)
        if catsGame():
            print("Cats game.")
            speak.Speak("Cats game.")
            replay()
            return
        cask = askNums()
        rask = askNums2()
        while isFilled(rask, cask):
            printBoard()
            print("That is filled. Please pick something else.")
            speak.Speak("That is filled. Please pick something else.")
            cask = askNums()
            rask = askNums2()
        
        if rask == 1:
            line1[cask - 1] = "O"
        elif rask == 2:
            line2[cask - 1] = "O"
        else:
            line3[cask - 1] = "O"
        rask = 0
        cask = 0
        printBoard()
        if hasWon():
            ply2games += 1
            writefiles()
            if wpgf == 1:
                print("Player 2 has won, and Player 1 has lost.")
                speak.Speak("Player 2 has won, and Player 1 has lost.")
            else:
                print("Player 1 has won, and Player 2 has lost.")
                speak.Speak("Player 1 has won, and Player 2 has lost.")
            replay()
            return
        if catsGame():
            print("Cats game.")
            speak.Speak("Cats game.")
            ply2games += 1
            writefiles()
            replay()
            return


def main():
    global speak
    line1[0] = "-"
    line1[1] = "-"
    line1[2] = "-"
    line2[0] = "-"
    line2[1] = "-"
    line2[2] = "-"
    line3[0] = "-"
    line3[1] = "-"
    line3[2] = "-"
    playtype = 0
    print("Which mode? '1' for 1 player, '2' for 2 players, and '3' for AI vs. AI.")
    speak.Speak("Which mode? '1' for 1 player, '2' for 2 players, and '3' for AI vs. AI.")
    playtype = int(input("> "))

    if playtype == 1:
        speak.Speak("Have fun!")
        player1()
    elif playtype == 2:
        speak.Speak("Have fun!")
        player2()
    elif playtype == 3:
        speak.Speak("Have fun watching!")
        aiai()

def writefiles():
    global ply1games
    global ply2games
    global aigamesn
    global totalgamescount
    tttfile = open("tttfile.txt","w")
    tttfile.write("Player 1 games: \n")
    tttfile.write(str(ply1games) + "\n")
    tttfile.write("Player 2 games: \n")
    tttfile.write(str(ply2games) + "\n")
    tttfile.write("Ai games: \n")
    tttfile.write(str(aigamesn) + "\n")
    tttfile.write("Total games: \n")
    totalgamescount = aigamesn + ply2games + ply1games
    tttfile.write(str(totalgamescount) + "\n")
    tttfile.close()

if __name__ == "__main__":
    sleep(1)
    print("Loading files...")
    blahstuff = ""
    tttfile = open("tttfile.txt", "r")
    blahstuff = tttfile.readline()
    ply1games = int(tttfile.readline())
    blahstuff = tttfile.readline()
    ply2games = int(tttfile.readline())
    blahstuff = tttfile.readline()
    aigamesn = int(tttfile.readline())
    blahstuff = tttfile.readline()
    totalgamescount = int(tttfile.readline())
    tttfile.close()
    writefiles()
    sleep(3)
    print("Success... Loading game...")
    sleep(5)
    print("Testing voice...")
    speak.Speak("voice test")
    sleep(2)
    print("Voice successful... Loading...")
    sleep(3)
    print("Running game...")
    sleep(3)
    print("Welcome to tic tac toe! ")
    speak.Speak("welcome to tic tac toe")
    sleep(2)
    print("You have played " + str(ply1games) + " Player one games, " + str(ply2games) + " Player two games, and " + str(aigamesn) + " Ai games.")
    speak.Speak("You have played " + str(ply1games) + " Player one games " + str(ply2games) + " Player two games and " + str(aigamesn) + " Ai games")
    sleep(1)
    print("You have played: " + str(totalgamescount) + " total games.")
    speak.Speak("You have played: " + str(totalgamescount) + " total games")
    sleep(2)
    main()
