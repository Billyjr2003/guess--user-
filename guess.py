import random

def computer_guess(x):
  low = 1
  high = x
  feedback = ""
  while feedback != "c" :
    if low != high :
      guess= random.randint(low,high)
    else : 
      guess = low 
    feedback = input(f"is {guess} too high (H) , too low (L) or correct (C) ?").lower() 
    if feedback == "h"   :
      guess = guess-1 
    elif feedback == "l"  :
      guess = guess +1 
      
    else : 
      print ("yaaaay the computer guess right")  
  print (guess)    
computer_guess(10)  
