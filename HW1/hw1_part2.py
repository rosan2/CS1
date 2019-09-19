# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:46:50 2019

@author: rosan2
"""
'''
In this program it collects input from the user regarding time and how many miles they have/plan to run.
Using that information it calculates the average pace, average speed, and projected time.
'''

import math

def speedCalculations(minutes, seconds, milesRun, milesTarget):
    
    pace = (minutes*60 + (seconds)) / milesRun
    paceMin = int(pace / 60)
    paceSec = int(pace % 60)
    sentence1 = "Pace is {0} minutes and {1} seconds per mile.".format(paceMin, paceSec)
    print(sentence1)
    
    hour = (minutes / 60) + ((seconds/60) / 60)
    speed = milesRun / hour
    sentance2 = "Speed is {0:.2f} miles per hour.".format(speed)
    print(sentance2)
    
    target = pace * milesTarget
    targetSec = int(target % 60)
    targetMin = int(target / 60)
    print("""Time to run the target distance of {0:.2f} miles\
 is {1} minutes and {2} seconds.""".format(milesTarget, targetMin, targetSec))
    
minutes = input("Minutes ==> ")
print(minutes)
seconds = input("Seconds ==> ")
print(seconds)
milesRun = input("Miles ==> ")
print(milesRun)
milesTarget = input("Target Miles ==> ")
print(milesTarget + "\n")


speedCalculations(int(minutes), int(seconds), float(milesRun), float(milesTarget))

