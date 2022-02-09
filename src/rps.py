import matplotlib.pyplot as mtp
from configparser import ConfigParser
from random import choice
from sys import exit
from datetime import datetime
from colorama import Style, Fore, init

init()

def play():
    # Adds parser and reads the settings file
    config = ConfigParser()
    config.read('settings.ini')
    
    # Declares the user and comp's score as well as the tie and total no. of games data
    user_score = 0
    comp_score = 0
    tie = 0
    total_games = 0
    
    #Colorama Variables
    
    bright = Style.BRIGHT
    critical = Fore.RED + bright
    success = Fore.GREEN + bright
    dim = Style.DIM
    yellow = Fore.YELLOW + bright
    white = Fore.WHITE + bright
    r = Fore.RESET
    
    datenow = datetime.now()
    dateasstr = datenow.strftime("%Y-%m-%d %H:%M:%S")
    
    nonstop = config.get('RPS', 'nonstop')
    charttype = config.get('Chart','chart_type')
        
    if nonstop == "True":
        print(success + "\nYou can now stop the game by typing \'stop\' while the game plays.\n" + r)
    
    compname = input("Enter the name of your player, or type \"none\" to skip.\nType \"cancel\" or \"exit\" to terminate this program.\n").lower()
    if compname == "cancel" or compname == "exit":
        exit()
    if compname == "none" or compname == '':
        compname = "Computer"
    while True:
        
        user_action = input("Enter a choice: (rock, paper, scissors)\nNote: This is not case sensitive, but don't shortcut any of these words.\n").lower()
        possible_actions = ['rock', 'scissors', 'paper']
        computer_actions = choice(possible_actions)
        
        if user_action not in possible_actions \
            and not user_action == 'stop':
            print(critical + "Invalid option. Try again." + r)
            continue
    
        if user_action == computer_actions:
            print("You choose", user_action.lower())
            print(compname, "chooses", computer_actions)
            print(yellow + "It's a tie" + r)
            tie += 1
            total_games += 1    
        
        elif user_action == "paper" or user_action == "p":
            
            if computer_actions == 'scissors':
                print("You choose paper")
                print(compname, "chooses", computer_actions)
                print(dim + "Scissors win! You Lose." + r)
                comp_score += 1
                total_games += 1
            else:
                print("You choose paper")
                print(compname, "chooses", computer_actions)
                print(bright + "Paper wins! You Won." + r)
                user_score += 1
                total_games += 1
        
        elif user_action == 'rock' or user_action == "r":
            
            if computer_actions == 'paper':
                print("You choose rock")
                print(compname, "chooses", computer_actions)
                print(dim + "Paper wins! You Lose." + r)
                comp_score += 1
                total_games += 1
                
            else:
                print("You choose rock")
                print(compname, "chooses", computer_actions)
                print(bright + "Rock wins! You Won." + r)
                user_score += 1 
                total_games += 1

        elif user_action == 'scissors' or user_action == "s":
            
            if computer_actions == 'paper':
                print("You choose scissors")
                print(compname, "chooses", computer_actions)
                print(bright + "Scissors win! You Won." + r)
                user_score += 1 
                total_games += 1
            else:
                print("You choose scissors")
                print(compname, "chooses", computer_actions)
                print(dim + "Rock wins! You Lose." + r)
                comp_score += 1 
                total_games += 1
        
# If nonstop is False

        if nonstop == 'False':
            while True:            
               user_prompt = input("Wanna play again? y/n\n").lower()
               
               if user_prompt == 'n':
                   user_score = str(user_score)
                   comp_score = str(comp_score)
                   print(success+"You scored", user_score+"."+r)
                   print(success+dim+compname, "scored", comp_score+"."+r)
                   
                   if tie == 1:
                       print(yellow+"Drawn",tie,"time.n"+r)
                   elif tie >= 2 or tie < 1:
                       print(yellow+"Drawn",tie,"times.\n"+r)
                       
                   if total_games == 1:
                       print(white+"You played",total_games,"game.\n"+r)
                   elif total_games >= 2 or total_games < 1:
                       print(white+"You played",total_games,"games.\n"+r)
                    
                   while True:
                       scview = input('Do you want to view your scoreboard chart? (y/n)\n').lower()
                       user_score = int(user_score)
                       comp_score = int(comp_score)
                        
                       if scview == 'y':
                           userscores = ['Wins', 'Loses', 'Draw']
                           compscores = [user_score, comp_score, tie]
                           datacolor = config.get('Chart', 'datachartcolor')
                           
                           if charttype == 'bar':
                               mtp.bar(userscores, compscores, color=datacolor)
                               mtp.title('Your RPS Scoreboard')
                               print("As of", dateasstr)
                               mtp.show()
                               exit()
                            
                           elif charttype == 'plot':
                               mtp.plot(userscores, compscores, marker='o', color=datacolor)
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               exit()
                           
                           elif charttype == 'dots':
                               mtp.scatter(userscores, compscores, color=datacolor, s=[140,70,100])
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               exit()    

                           elif charttype == 'stem':
                               mtp.stem(userscores, compscores, markerfmt='o')
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               exit()  

                           elif charttype == 'step':
                               mtp.step(userscores, compscores, color=datacolor)
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               exit()     
                           
                       elif scview == 'n':
                           print('Exiting...')
                           exit()
                       else:
                           continue
                                  
               elif user_prompt != 'y' and not(user_prompt == 'n'):
                   print("Try again.")
               elif user_prompt == 'y':
                   break
               
# If nonstop is True

        else:
            if user_action == 'stop':
                user_score = str(user_score)
                comp_score = str(comp_score)
                print(success+"You scored", user_score+"."+r)
                print(success+dim+compname, "scored", comp_score+"."+r)
                
                if tie == 1:
                    print(yellow + "Drawn",tie,"time.\n" +r)
                elif tie >= 2 or tie < 1:
                    print(yellow + "Drawn",tie,"times.n" +r)
                    
                if total_games == 1:
                    print(white+"You played",total_games,"game.\n"+r)
                elif total_games >= 2 or total_games < 1:
                    print(white+"You played",total_games,"games.\n"+r)
                    
                while True:
                    scview = input('Do you want to view your scoreboard chart? (y/n)\n').lower()
                    user_score = int(user_score)
                    comp_score = int(comp_score)
                     
                    if scview == 'y':
                        userscores = ['Wins', 'Loses', 'Draw']
                        compscores = [user_score, comp_score, tie]
                        datacolor = config.get('Chart', 'datachartcolor')
                        
                        if charttype == 'bar':
                            mtp.bar(userscores, compscores, color=datacolor)
                            mtp.title('Your RPS Scoreboard')
                            print("As of", dateasstr)
                            mtp.show()
                            exit()
                         
                        elif charttype == 'plot':
                            mtp.plot(userscores, compscores, marker='o', color=datacolor)
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            exit()
                        
                        elif charttype == 'dots':
                            mtp.scatter(userscores, compscores, color=datacolor, sizes=(20,))
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            exit()    

                        elif charttype == 'stem':
                            mtp.stem(userscores, compscores, markerfmt='o')
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            exit()  

                        elif charttype == 'step':
                            mtp.step(userscores, compscores, color=datacolor)
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            exit()  
                          
                    elif scview == 'n':
                        print('Exiting...')
                        exit()
                    else:
                        continue
                        