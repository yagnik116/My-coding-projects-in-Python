import random

print("!!      WELCOME TO THE STONE PAPER SCISSERS      !!")
 
game_list = {1 :"Stone" ,2 :"Paper", 3 :"Scissers"}

def game():
       
        com = random.randint(1,3)
        user = int(input("Enter your choice : (1 for Stone, 2 for Paper, 3 for Scissors) : "))
    
        if(com == user):
                print(f"Computer choose : {game_list[com]}")
                print(f"You choose : {game_list[user]}" )
                print("TIE !!")
                
        elif(com == 1 and user == 2):
                    print(f"Computer choose : {game_list[com]}")
                    print(f"You choose : {game_list[user]}")
                    print("YOU WIN!!")
                    
        elif(com == 1 and user == 3):
                    print(f"Computer choose : {game_list[com]}")
                    print(f"You choose : {game_list[user]}")
                    print("COMPUTER WINS!!")
                    
        elif(com == 2 and user == 1):
                    print(f"Computer choose : {game_list[com]}")
                    print(f"You choose : {game_list[user]}")
                    print("COMPUTER WINS!!")
                
        elif(com == 2 and user == 3):
                    print(f"Computer choose : {game_list[com]}")
                    print(f"You choose : {game_list[user]}")
                    print("YOU WIN!!")
                    
        elif(com == 3 and user == 1):
                    print(f"Computer choose : {game_list[com]}")
                    print(f"You choose : {game_list[user]}")
                    print("YOU WIN!!")
                    
        elif(com == 3 and user == 2):
                    print(f"Computer choose : {game_list[com]}")
                    print(f"You choose : {game_list[user]}")
                    print("COMPUTER WINS!!")
                    
        else:
                print("!!  ERROR  !!")
                
        p = int(input("Want to play again : (1 for yes, 0 for no) : "))
        
        if(p == 0):
           print("!! Thanks for playing !!")
        
        else:
             game()
          
game()
                
