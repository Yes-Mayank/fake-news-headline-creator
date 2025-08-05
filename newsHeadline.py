
# FUNNY N FAKE NEWS HEADLINES GENERATOR 


import random
import time
import sys

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
  
subject = ["mayank", "harish", "amrit", "alina"]
subject1 = ["boat", "car", "horse", "apple"]
action = ["eats", "slaps", "KICKS", "rides", "cut",]
object_ = ["at stage", "at toilet", "at home", "at school"]

while True:
    print("\nGenerating headline...")
    time.sleep(2)  

    a = random.choice(subject)
    b = random.choice(action)
    c = random.choice(object_)
    d = random.choice(subject1)

    headline = f"HEADLINE::: {a} {b} {d} {c}"
    typing_effect(headline, 0.07)  

    again = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if again != "yes":
        typing_effect("Exiting... Goodbye!", 0.05)
        break