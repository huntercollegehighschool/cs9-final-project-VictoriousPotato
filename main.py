"""
Name(s): Adela Seltzer, Theo Parker
Name of Project: Home From School
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4


'''
I think I fixed almost everything, we still do not have a limit on the amount of time you can spend on this, maybe make it 15 so ppl can go overtime? 

I made a limit of 15 hours, but I dont really have time to test what happens if you go overtime. it should work. 

Also maybe make the science test studying easier


"""
Name(s): Adela Seltzer, Theo Parker
Name of Project: Home From School
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

'''
'''
I think I fixed almost everything, we still do not have a limit on the amount of time you can spend on this, maybe make it 15 so ppl can go overtime? 

I made a limit of 15 hours, but I dont really have time to test what happens if you go overtime. it should work. 

Also maybe make the science test studying easier

I renamed go to sleep to end day, and removed the prompt to punch the wall (you can still punch wall it just wont say you can)

could you test for bugs and also maybe make the science thing a little easier/more common knowledge?

Also you submitted the project proposal form so I think you should submit the github when we are both ready.


******************************************************************************
IMPORTANT: If you do work on this file it does not save automatically, and you have to commit and push it. This will not submit the file.
******************************************************************************
'''
import os 
import time


def DoScience():
  print("You decided to study for science")
  global Science 
  Science += 1  
  print("There are three topics on your science study guide, and to feel ready after learning each one, you ask yourself a question. The question for the first topic says:")
  time.sleep (1.5)
  sciencequestion = input("What is the first element on the periodic table? ")
  if sciencequestion == 'hydrogen' or sciencequestion == 'Hydrogen':
    Science += 1
  else:
    Science += 0
  time.sleep (0.5)
  print("Next question")
  time.sleep (0.5)
  sciencequestion = input("How many valence electrons is the maximum? ")
  if sciencequestion == '8':
    Science +=1
  else:
    Science +=0
  time.sleep (0.5)
  print("Last question")
  time.sleep (0.5)
  sciencequestion = input("True or false: is water polarized? ")
  if sciencequestion == 'True' or sciencequestion == 'true':
    Science +=1
  else:
    Science += 0
  time.sleep (0.5)
  print("Ok, now choose something else to do: ")
  global Hours
  Hours += 1
  Whatdo()





def DoGames():
  global Game
  print("You decided to play some games")
  time.sleep(1.0)
  print("...")
  time.sleep(1.0)
  print("You played games for a while, and you feel happier")
  Game += 1
  global Hours
  Hours += 1
  Whatdo()




  
def DoPunchWall():
  global PunchWall
  PunchWall += 1
  print("You punched the wall. Your hand hurts. What do you want to do now?")
  time.sleep (0.5)
  Whatdo()






  

def DoHistory():
  global History
  History += 1
  print("You decided to do your history homework")
  time.sleep (0.5)
  print("There are three questions on your  history homework. The first question says:")
  time.sleep (0.5)
  historyquestion = input("Who was the first President of the United States?: ")
  if historyquestion == 'George Washington' or historyquestion == 'george washington' or historyquestion == 'George washington' or historyquestion == 'george Washington' or historyquestion == 'washington' or historyquestion == 'Washington':
    History += 1
  time.sleep (0.5)
  print("Next question")
  time.sleep (0.5)
  historyquestion = input("What year was the American Declaration of Independence signed?: ")
  if historyquestion == '1776':
    History += 1
  time.sleep (0.5)
  print ("Last question")
  time.sleep (0.5)
  print("For how many seconds did George washington brush his teeth on December 23rd 1799?")
  historyquestion = input("? ")
  if historyquestion == '0':
    History += 1
  time.sleep (0.5)
  print("Ok, now choose something else to do: ")
  global Hours
  Hours += 1
  Whatdo()











def DoMath():
  global Math
  Math += 1
  time.sleep (0.5)
  print("You decided to do your math homework")
  time.sleep (0.5)
  print("There are three questions on your math homework. The first question says:")
  time.sleep (0.5)
  mathquestion = input("What is 1 + 1?: ")
  if mathquestion == '2':
    Math += 1
  time.sleep (0.5)
  print("Next question")
  time.sleep (0.5)
  mathquestion = input("What is 582734 + 417265?: ")
  if mathquestion == '999999':
    Math += 1
  time.sleep (0.5)
  print ("Last question")
  time.sleep (0.5)
  mathquestion = input("What is 23095723 + 93764103?: ")
  if mathquestion == '116859826':
    Math += 1
  time.sleep (0.5)
  print("Okay you are done, time to do something else")
  time.sleep (0.5)
  global Hours
  Hours += 1
  Whatdo()
  



def EndDay():
  global Happy
  Happy = 0
  TimeSlept = 12 - Hours
  if TimeSlept > 7:
    time.sleep (0.5)
    print("You slept for", TimeSlept, "hours, and you got a good night sleep.")
  elif TimeSlept == 7:
    print("You slept 7 hours, and feel a little groggy waking up.")
    Happy -= 5
  elif TimeSlept == 6: #like the amount of sleep im gonna get doimg this at midnight on my phone after procrastinating 7 hours
    print("You slept for 6 hours, and felt groggy waking up.")
    Happy -= 13
  elif TimeSlept == 5:
    print("You only got 5 hours of sleep, and were really tired waking up.")
    Happy -= 24
  elif TimeSlept == 4:
    print("You definitely should have gotten more sleep, and were very tired when you woke up. You only managed to get 4 hours of sleep.")
    Happy -= 40
  elif TimeSlept == 3:
    print ("You only managed to get 3 hours of sleep, and you missed your alarm and were late to school. You felt really tired too.")
    Happy -= 60
  elif TimeSlept == 2:
    print ("You only managed to get 2 hours of sleep, and you missed your alarm and were late to school. You felt really tired too.")
    Happy -= 85
  elif TimeSlept == 1:
    print("You did too many activities last night and had only had an hour to sleep. You feel immensely tired.")
    Happy -= 120
  elif TimeSlept == 0:
    print("You did too many activities last night and did not sleep at all. Oh well.")
    Happy -= 120
  elif TimeSlept == -1 or -2:
    print("You were late to school, and you got in trouble.")
    Happy -= 145
  elif TimeSlept == -3:
    print("You did so many activities that you got no sleep last night and were still doing stuff when you were supposed to leave for school. Your parent yelled at you, and you were grounded for a week. Best not do that again")
    Happy -=145
    Happy -= (TimeSlept*-30)
  if History == 4: 
    time.sleep (0.5)
    print("Your teacher graded your History homework and gave you 100% with a smiley face yay!")
    Happy += 10
  elif History == 1 or History == 2 or History == 3:
    time.sleep (0.5)
    print("Your history work was not satisfactory :(")
  else:
    time.sleep (0.5)
    print("You didn't have History homework to hand in and you got embarrased when you were called out for it by your teacher.")
    Happy -= 5
  if Math == 4:
    time.sleep (0.5)
    print("Your teacher seemed very happy with your efforts on math homework!")
    Happy += 10
  elif Math == 1 or Math == 2 or Math == 3:
    time.sleep (0.5)
    print("You tried, but not hard enough on your math homework.")
  else:
    time.sleep (0.5)
    print("You did not even start your math homework. Shame. There was a pop quiz the next day that you failed.")
    Happy -= 5
  if Science == 4:
    time.sleep (0.5)
    print("You aced the science test, and feel very happy!")
    Happy += 12
  elif Science == 1 or Science == 2 or Science == 3:
    time.sleep (0.5)
    print("You tried, but did not do well when you studied science, and messed up on the test.")
  else:
    time.sleep (0.5)
    print("You did not study, and you absolutely flunked that science test.")
    Happy -= 8
  if Game == 0:
    time.sleep (0.5)
    print("You did not play any games tonight.")
  else:
    time.sleep (0.5)
    print("You played games today.")
    Happy = Happy + (Game * 6)
  if PunchWall > 1:
    time.sleep (0.5)
    print("You punched the wall multiple times, and your hand hurts the next day. You are not really able to write notes without pain and regret your decision.")
    Happy -= (5*PunchWall)
  elif PunchWall == 1:
    time.sleep (0.5)
    print("You punched the wall, but the pain was manageble and you had a fine day.")
  print("After going about your day, you felt if you had to give a value to your happiness, it would be: ", Happy)
  if Happy == 39: #Max happiness i think
    print("Astounding job! you felt very happy walking around school, doing your daily buisness.")
  if Happy >= 25:
    print("Nice job")
  elif Happy >= 0:
    print("Meh")
  else:
    print("You did not feel great about your day. Maybe tommorow will be better..?")
  
    
    




  
def Whatdo():
  if 4 - Hours >= 1:
    print("You have", 4 - Hours ," hours before you are supposed to be in bed")
  elif Hours == 4:
    print("It is bedtime now")
  elif 12 > Hours > 4:
    print("You should be in bed by now")
  elif Hours == 12:
    print("Dawn breaks, and it is now time to go to school (end the day to go to school).")
  elif 14 >= Hours > 12:
    print("You are already late to school. (end the day to go to school).")
  else:
    print("You stayed in your room for too long, and your parents noticed you hadn't gone to school yet, and how sleepy you looked. They sent you to school, but you arrived very late.")
    EndDay()
  hello = input("Choose one: 'History' 'Math' 'Science' 'Games' 'Punch Wall' 'End The Day':  ")
  if hello == 'History' or hello == 'history' and History == 0:
    DoHistory()
  elif hello == 'Math' or hello =='math' and Math == 0:
    DoMath()
  elif hello == 'Science' or hello =='science' and Science == 0:
    DoScience()
  elif hello == 'Games' or hello =='games':
    DoGames()
  elif hello == 'Punch Wall' or hello =='Punch wall' or hello =='punch Wall' or hello =='punch wall':
    DoPunchWall()
  elif hello == 'End The Day' or hello =='End The day' or hello =='End the Day' or hello =='End the day' or hello =='end The Day' or hello =='end The day' or hello == 'end the Day' or hello == 'end the day':
    EndDay()
  else:
    print("Either that is not an option or you have already done this and cannot redo it. Please try again.")
    Whatdo()
    





print("You arrive home from school. It is Wednesday, and you have Math and History homework to do, as well as a Science test to study for. You have 12 hours before you have to leave for school, and you are supposed to go to bed in around 4 hours. You can redo some things but not others. What shall you do?")
time.sleep (1.0)
global Hours
Hours = 0
global Game
Game = 0
global Science
Science = 0
global History
History = 0
global Math
Math = 0
global PunchWall
PunchWall = 0
Whatdo()

