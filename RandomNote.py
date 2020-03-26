#!/usr/bin/env python3
import random
import time 
starttime=time.time()
Time = int(input("Enter Time in Seconds: "))
Note_Set = ["A","A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
String_Set = ["1", "2", "3", "4"]

while True:
    Note = random.choice(Note_Set)
    String = random.choice(String_Set)
    print(Note, "String", String)
    time.sleep(Time - ((time.time() - starttime) % Time))
