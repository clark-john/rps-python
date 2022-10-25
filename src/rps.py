import matplotlib.pyplot as mtp
from yamlparser import get_data
from random import choice
from colorama import init, Fore, Style
from console_colors import consolecolor
from platform import system
from tkinter import messagebox as msgbox
from time import sleep
from csv import writer
from datetime import datetime
from pandas import DataFrame
from InquirerPy import prompt

def play():
  yaml = get_data()

  global user_score, comp_score
  global rock_user, paper_user, scissors_user, rock_c, scissors_c, paper_c
  user_score = 0
  comp_score = 0
  tie = 0
  total_games = 0

  # other variables
  rock_user = 0
  paper_user = 0
  scissors_user = 0
  rock_c = 0
  paper_c = 0
  scissors_c = 0

  if system() == 'Windows':
    init()
    dim = Style.DIM
    normal = Style.BRIGHT # since Windows has only dim and bright colors.
    bright = Style.BRIGHT

  elif system() == 'Linux':
    dim = Style.DIM
    normal = Style.NORMAL
    bright = Style.BRIGHT
  
  critical = Fore.RED
  success = Fore.GREEN
  yellow = Fore.YELLOW
  white = Fore.WHITE
  charttype = yaml['Chart']['chart_type']

# ----------------------------------------------------------------------------------------------------

  def game_done():
    global user_score, comp_score
    global rock_user, paper_user, scissors_user, rock_c, scissors_c, paper_c
    # inquirer setup

    plot_options = {
      "name": "plot",
      "type": "rawlist",
      "message": "Plot scoreboard with?",
      "choices": [
        'matplotlib',
        'pandas (dataframe)'
      ]
    }

    user_score = user_score
    comp_score = comp_score

    rock_user = rock_user
    paper_user = paper_user
    scissors_user = scissors_user
    rock_c = rock_c
    scissors_c = scissors_c
    paper_c = paper_c

    if system() == 'Windows':
      init()
      dim = Style.DIM
      normal = Style.BRIGHT # since Windows has only dim and bright colors.
      bright = Style.BRIGHT

    elif system() == 'Linux':
      dim = Style.DIM
      normal = Style.NORMAL
      bright = Style.BRIGHT

    datenow = datetime.now()
    dateasstr = datenow.strftime("%B %d, %Y %I:%M %p")

    user_score = str(user_score)
    comp_score = str(comp_score)
    print(success+"You scored", user_score+"."+consolecolor)
    print(success+dim+compname, "scored", comp_score+"."+bright+consolecolor)
     
    if tie == 1:
      print(yellow+"Drawn",tie,"time.\n"+consolecolor)
    elif tie >= 2 or tie == 0:
      print(yellow+"Drawn",tie,"times.\n"+consolecolor)
         
    if total_games == 1:
      print(white+"You played",total_games,"game.\n"+consolecolor)
    elif total_games >= 2 or total_games == 0:
      print(white+"You played",total_games,"games.\n"+consolecolor)

    with open('./src/score.csv', 'w', newline='') as score: 
      w = writer(score)            
      date = [dateasstr]
      wins = ['Wins', user_score]
      loses = ['Loses', comp_score]
      draws = ['Draws', tie]
      total = ['Total Games', total_games]
      forloop = [date, wins, loses, draws, total]
      for x in forloop:
        w.writerow(x)
    
    def mtplib():
      global user_score, comp_score
      user_score = int(user_score)
      comp_score = int(comp_score)
        
      userscores = ['Wins', 'Loses', 'Draw']
      compscores = [user_score, comp_score, tie]
      datacolor = yaml['Chart']['datachartcolor']
         
      if charttype == 'bar':
        mtp.bar(userscores, compscores, color=datacolor)
        mtp.title('Your RPS Scoreboard')
        print(success+"As of", dateasstr + consolecolor)
        mtp.savefig('./src/score.png')
        mtp.show()
        print("Thanks for playing! :)")
        sleep(3)
        exit()
          
      elif charttype == 'plot':
        mtp.plot(userscores, compscores, marker='o', color=datacolor)
        mtp.title('Your RPS Scoreboard')
        print(success+"As of", dateasstr + consolecolor)
        mtp.savefig('./src/score.png')
        mtp.show()
        print("Thanks for playing! :)")
        sleep(3)
        exit()
         
      elif charttype == 'dots':
        mtp.scatter(userscores, compscores, color=datacolor, s=[280,140,200])
        mtp.title('Your RPS Scoreboard')
        print(success+"As of", dateasstr + consolecolor)
        mtp.savefig('./src/score.png')
        mtp.show()
        print("Thanks for playing! :)")
        sleep(3)
        exit()             

      elif charttype == 'stem':
        mtp.stem(userscores, compscores, markerfmt='o')
        mtp.title('Your RPS Scoreboard')
        print(success+"As of", dateasstr + consolecolor)
        mtp.savefig('./src/score.png')
        mtp.show()
        print("Thanks for playing! :)")
        sleep(3)
        exit()     

      elif charttype == 'step':
        mtp.step(userscores, compscores, color=datacolor)
        mtp.title('Your RPS Scoreboard')
        print(success+"As of", dateasstr + consolecolor)
        mtp.savefig('./src/score.png')
        mtp.show()
        print("Thanks for playing! :)")
        sleep(3)
        exit()     
      
    def pandas_dataframe():
      global rock_user, paper_user, scissors_user, rock_c, scissors_c, paper_c
      index = ['Player', compname]
      columns = ['Wins','Loses','Draws','Rock','Paper','Scissors']
      ndarray = [[user_score, comp_score, tie, rock_user, paper_user, scissors_user],[comp_score,user_score,tie, rock_c, paper_c, scissors_c]]
      df = DataFrame(ndarray, index, columns)
      print("")
      print(df)
      print('\n'+success+"As of", dateasstr + consolecolor)
      dfasstr = str(df)
      with open('./src/score.txt', 'w') as y:
        y.write(dfasstr)
      print("Thanks for playing! :)")
      sleep(3)
      print("Exiting...")
      exit()
    
    scview = msgbox.askquestion('RPS Scoreboard','Do you want to view your scoreboard chart?')
    if scview == 'yes':
      plot_option = prompt(plot_options)
      if plot_option == {'plot':'pandas'}:
        pandas_dataframe()
      else:
        mtplib()
    else:
      print("As of", dateasstr)
      print("Thanks for playing! :)")
      sleep(3)
      print("Exiting...")
      exit()

  """ ------------------------------------------------------------------------------------------- """

  nonstop = yaml['RPS']['nonstop']
    
  if nonstop:
    print(success + "\nYou can now stop the game by typing \'stop\' while the game plays.\n"+consolecolor)

  compname = input("Enter the name of your player, or type \"none\" to skip.\nType \"cancel\" or \"exit\" to terminate this program.\n").lower()
  if compname == "cancel" or compname == "exit":
    exit()
  elif compname == "none" or compname == '':
    compname = "Computer"
  else:
    compname.title()

  while True:
    user_action = input("Enter a choice: (rock, paper, scissors)\nNote: This is not case sensitive, but don't shortcut any of these words.\n").lower()
    possible_actions = ['rock', 'scissors', 'paper']
    computer_actions = choice(possible_actions)
    
    if user_action not in possible_actions \
      and not user_action == 'stop':
      print(critical + "Invalid option. Try again." + consolecolor)
      continue

    if user_action == computer_actions:
      print(bright+"You choose", user_action.lower())
      print(compname, "chooses", computer_actions)
      print(normal+yellow+ "It's a tie"+consolecolor)
      tie += 1
      total_games += 1
      if user_action or computer_actions == 'rock':
        rock_c += 1
        rock_user += 1
      elif user_action or computer_actions == 'scissors':
        scissors_c += 1
        scissors_user += 1
      else:
        paper_user += 1 
        paper_c += 1    
    
    elif user_action == "paper" or user_action == "p":
        
      if computer_actions == 'scissors':
        print("You choose paper")
        print(compname, "chooses", computer_actions)
        print(dim + "Scissors win! You Lose.")
        paper_user += 1
        scissors_c += 1
        comp_score += 1
        total_games += 1
      else:
        print("You choose paper")
        print(compname, "chooses", computer_actions)
        print(bright + "Paper wins! You Won.")
        paper_user += 1
        rock_c += 1
        user_score += 1
        total_games += 1
    
    elif user_action == 'rock' or user_action == "r":
        
      if computer_actions == 'paper':
        print("You choose rock")
        print(compname, "chooses", computer_actions)
        print(dim + "Paper wins! You Lose.")
        rock_user += 1
        paper_c += 1
        comp_score += 1
        total_games += 1
          
      else:
        print("You choose rock")
        print(compname, "chooses", computer_actions)
        print(bright + "Rock wins! You Won.")
        rock_user += 1
        scissors_c += 1
        user_score += 1 
        total_games += 1

    elif user_action == 'scissors' or user_action == "s":
        
      if computer_actions == 'paper':
        print("You choose scissors")
        print(compname, "chooses", computer_actions)
        print(bright + "Scissors win! You Won.")
        scissors_user += 1
        paper_c += 1
        user_score += 1 
        total_games += 1
      else:
        print("You choose scissors")
        print(compname, "chooses", computer_actions)
        print(dim + "Rock wins! You Lose.")
        scissors_user += 1
        rock_c += 1
        comp_score += 1 
        total_games += 1
    
    while True:

      if not nonstop:
        user_prompt = input("Wanna play again? y/n\n").lower()

        if user_prompt == 'n':
          game_done()

        elif user_prompt != 'y' and not(user_prompt == 'n'):
          print(critical+"Try again."+consolecolor)
        elif user_prompt == 'y':
          break

      else:
        if user_action == 'stop':
          game_done()
        break
