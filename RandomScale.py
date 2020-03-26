#!/usr/bin/env python3
import random
import time 
starttime=time.time()
Time = int(input("Enter Time in Seconds: "))
Note_Set = ["A","A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
Scale_Set = ["MAJ", "min"]
Position_Set = ["1", "2", "3", "4", "5"]

while True:
    Note = random.choice(Note_Set)
    Scale = random.choice(Scale_Set)
    Position = random.choice(Position_Set)
    print(Note, Scale,"Position", Position)
    time.sleep(Time - ((time.time() - starttime) % Time))
