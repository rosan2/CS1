# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:59:01 2019

@author: rosan2
"""

"""
This funtion uses the input() funtion to collect data matching certain descriptions
such as adjectives and nouns...
then it takes the collected data and using the .format() function it inserts the data into 
a predetermined paragraph simulating a MadLibs game.
"""

def madLibs():
    print("Let's play Mad Libs for Homework 1")
    print("Type one word responses to the following:")
    print()
    
    name = input("proper_name ==> ")
    print(name)
    adj1 = input("adjective ==> ")
    print(adj1)
    noun1 = input("noun ==> ")
    print(noun1)
    verb1 = input("verb ==> ")
    print(verb1)
    verb2 = input("verb ==> ")
    print(verb2)
    noun2 = input("noun ==> ")
    print(noun2)
    emo1 = input("emotion ==> ")
    print(emo1)
    verb3 = input("verb ==> ")
    print(verb3)
    noun3 = input("noun ==> ")
    print(noun3)
    season = input("season ==> ")
    print(season)
    adj2 = input("adjective ==> ")
    print(adj2)
    emo2 = input("emotion ==> ")
    print(emo2)
    teamName = input("team-name ==> ")
    print(teamName)
    noun4 = input("noun ==> ")
    print(noun4)
    adj3 = input("adjective ==> ")
    print(adj3)
    print()
    print("Here is your Mad Lib...")
    print()
    
    text = """Good morning {}!

  This will be a/an {} {}! Are you {} forward to it?
  You will {} a lot of {} and feel {} when you do.
  If you do not, you will {} this {}.

  This {} was {}. Were you {} when {} won
  the {}?

  Have a/an {} day!"""

    print(text.format(name, adj1, noun1, verb1, verb2, noun2, emo1, verb3, \
                      noun3, season, adj2, emo2, teamName, noun4, adj3))

madLibs()