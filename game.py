import random
def single_player():
    player_score,comp_score=0,0
    inp='Y'
    while inp=='Y':
        lst=['R','P','S']
        random_num=random.randint(0,2)
        comp=lst[random_num]
        print("Enter R for Rock\n      P for paper\n      S for scissor\n      Q to quit")
        i=input()
        print(comp)
        if i==comp:
            print('Draw')
        elif i=='R' and comp=='S':
            print('won')
            player_score+=1
        elif i=='P' and comp=='R':
            print('WON')
            player_score+=1
        elif i=='S' and comp=='P':
            print('won')
            player_score+=1
        elif i=='Q':
            print('YOUR SCORE:',player_score,'\nCOMPUTER SCORE:',comp_score)
            if player_score>comp_score:
                print('WINNER!!!')
            elif player_score==comp_score:
                print('TIE MATCH')
            else:
                print('OOPS!!BETTER LUCK NEXT TIME')
            print('\nENTER Y TO PLAY AGAIN: ')
            inp=input()
            if inp=='Y':
                single_player()
            else:
                break
        else:
            print('loss')
            comp_score+=1
            
n=int(input("Enter 1 to play\nEnter 2 to quit------>"))
if n==1:
    single_player()
else:
    print('bye')