import random

print("!!  WELCOME TO THE RANDOM NUMBER GUESSING GAME  !!")

def game():
    computer = random.randint(1,100)
    print("Choose number from 1 TO 100.....")
    n = int(input("Enter your Number : "))
    numberOFguess = 1

    while(n != computer):
             if(n > computer):
                 print("Number is greater than computer's number.")
                 print("Choose lower than original number.")
                 n = int(input("Enter the new number : "))
                 numberOFguess += 1
                 
             elif(n < computer):
                  print("Number is less than computer's number.")
                  print("Choose higher than original number.")
                  n = int(input("Enter the new number : "))
                  numberOFguess += 1
                      
             else:
                 print("ERROR")
                 
    if(n == computer):
         print("YOU WON !!")
         print(f"Total number of guesses : {numberOFguess}")
                 
    p = int(input("Want to play again : (1 for yes, 0 for no) : "))
                
    if(p == 0):
         print("!! Thanks for playing !!")
                
    else:
        game()
                 
             
game()