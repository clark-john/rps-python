import random as r
import sys
import matplotlib.pyplot as mtp
import configparser
from datetime import datetime

def play():
    # Adds parser and reads the settings file
    config = configparser.ConfigParser()
    config.read('settings.ini')
    
    # Declares the user and xomp's score as well as the tie and total no. of games data
    user_score = 0
    comp_score = 0
    tie = 0
    total_games = 0
    
    datenow = datetime.now()
    dateasstr = datenow.strftime("%Y-%m-%d %H:%M:%S")
    
    nonstop = config.get('RPS', 'nonstop')
    charttype = config.get('Chart','chart_type')
        
    if nonstop == "True":
        print("\nYou can now stop the game by typing \'stop\' while the game plays.")
    
    compname = input("Enter the name of your player, or type \"none\" to skip.\nType \"cancel\" or \"exit\" to terminate this program.\n")
    if compname.lower() == "cancel" or compname.lower() == "exit":
        sys.exit()
    if compname.lower() == "none":
        compname = "Computer"
    while True:
        
        user_action = input("Enter a choice: (rock, paper, scissors)\nNote: This is not case sensitive, but don't shortcut any of these words.\n")
        user_action.lower()
        possible_actions = ['rock', 'scissors', 'paper']
        computer_actions = r.choice(possible_actions)
        
        
        user_action.lower()
        computer_actions.lower()
        if user_action not in possible_actions and not user_action == 'stop':
            print("Invalid option. Try again.")
            continue
        
        
        if user_action == computer_actions:
            print("You choose", user_action.lower())
            print(compname, "chooses", computer_actions)
            print("It's a tie")
            tie += 1
            total_games += 1    
        
        elif user_action.lower() == "paper":
            
            if computer_actions.lower() == 'scissors':
                print("You choose paper")
                print(compname, "chooses", computer_actions)
                print("Scissors win! You Lose.")
                comp_score += 1
                total_games += 1
            else:
                print("You choose paper")
                print(compname, "chooses", computer_actions)
                print("Paper wins! You Won.")
                user_score += 1
                total_games += 1
        
        elif user_action.lower() == 'rock':
            
            if computer_actions.lower() == 'paper':
                print("You choose rock")
                print(compname, "chooses", computer_actions)
                print("Paper wins! You Lose.")
                comp_score += 1
                total_games += 1
                
            else:
                print("You choose rock")
                print(compname, "chooses", computer_actions)
                print("Rock wins! You Won.")
                user_score += 1 
                total_games += 1

        elif user_action.lower() == 'scissors':
            
            if computer_actions.lower() == 'paper':
                print("You choose scisssors")
                print(compname, "chooses", computer_actions)
                print("Scissors win! You Won.")
                user_score += 1 
                total_games += 1
            else:
                print("You choose scissors")
                print(compname, "chooses", computer_actions)
                print("Rock wins! You Lose.")
                comp_score += 1 
                total_games += 1
        
# this crapload of lines below is for the 'nonstop' option

        if nonstop == 'False':
            while True:            
               user_prompt = input("Wanna play again? y/n\n")
               
               if user_prompt.lower() == 'n':
                   user_score = str(user_score)
                   comp_score = str(comp_score)
                   print("You scored", user_score+".")
                   print(compname, "scored", comp_score+".")
                   
                   if tie == 1:
                       print("Drawn",tie,"time.\n")
                   elif tie >= 2 or tie < 1:
                       print("Drawn",tie,"times.\n")
                       
                   if total_games == 1:
                       print("You played",total_games,"game.")
                   elif total_games >= 2 or total_games < 1:
                       print("You played",total_games,"games.")
                    
                   while True:
                       scview = input('Do you want to view your scoreboard chart? (y/n)\n')
                       user_score = int(user_score)
                       comp_score = int(comp_score)
                        
                       if scview.lower() == 'y':
                           userscores = ['Wins', 'Loses', 'Draw']
                           compscores = [user_score, comp_score, tie]
                           datacolor = config.get('Chart', 'datachartcolor')
                           
                           if charttype == 'bar':
                               mtp.bar(userscores, compscores, color=datacolor)
                               mtp.title('Your RPS Scoreboard')
                               print("As of", dateasstr)
                               mtp.show()
                               sys.exit()
                            
                           elif charttype == 'plot':
                               mtp.plot(userscores, compscores, marker='o', color=datacolor)
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               sys.exit()
                           
                           elif charttype == 'dots':
                               mtp.scatter(userscores, compscores, color=datacolor, s=[140,70,100])
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               sys.exit()    

                           elif charttype == 'stem':
                               mtp.stem(userscores, compscores, markerfmt='o')
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               sys.exit()  

                           elif charttype == 'step':
                               mtp.step(userscores, compscores, color=datacolor)
                               mtp.title('Your RPS Scoreboard')
                               print("\nAs of", dateasstr)
                               mtp.show()
                               sys.exit()     
                           
                       elif scview.lower() == 'n':
                           print('Exiting...')
                           sys.exit()
                       else:
                           continue
                                  
               elif user_prompt.lower() != 'y' and not(user_prompt.lower() == 'n'):
                   print("Try again.")
               elif user_prompt.lower() == 'y':
                   break
        else:
            if user_action.lower() == 'stop':
                user_score = str(user_score)
                comp_score = str(comp_score)
                print("You scored", user_score+".")
                print(compname, "scored", comp_score+".")
                
                if tie == 1:
                    print("Drawn",tie,"time.\n")
                elif tie >= 2 or tie < 1:
                    print("Drawn",tie,"times.\n")
                    
                if total_games == 1:
                    print("You played",total_games,"game.")
                elif total_games >= 2 or total_games < 1:
                    print("You played",total_games,"games.")
                    
                while True:
                    scview = input('Do you want to view your scoreboard chart? (y/n)\n')
                    user_score = int(user_score)
                    comp_score = int(comp_score)
                     
                    if scview.lower() == 'y':
                        userscores = ['Wins', 'Loses', 'Draw']
                        compscores = [user_score, comp_score, tie]
                        datacolor = config.get('Chart', 'datachartcolor')
                        
                        if charttype == 'bar':
                            mtp.bar(userscores, compscores, color=datacolor)
                            mtp.title('Your RPS Scoreboard')
                            print("As of", dateasstr)
                            mtp.show()
                            sys.exit()
                         
                        elif charttype == 'plot':
                            mtp.plot(userscores, compscores, marker='o', color=datacolor)
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            sys.exit()
                        
                        elif charttype == 'dots':
                            mtp.scatter(userscores, compscores, color=datacolor, sizes=(20,))
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            sys.exit()    

                        elif charttype == 'stem':
                            mtp.stem(userscores, compscores, markerfmt='o')
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            sys.exit()  

                        elif charttype == 'step':
                            mtp.step(userscores, compscores, color=datacolor)
                            mtp.title('Your RPS Scoreboard')
                            print("\nAs of", dateasstr)
                            mtp.show()
                            sys.exit()  
                          
                    elif scview.lower() == 'n':
                        print('Exiting...')
                        sys.exit()
                    else:
                        continue
                        