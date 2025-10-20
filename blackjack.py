import random,time
money=100
hand=['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
chosen=[]
player=[]
dealer=[]
bet=0

def pickcard():
    while True:
        a=random.randint(0,len(hand)-1)
        try: 
            chosen.index(a)==True
        except:
            break
    chosen.append(a)
    return a

def handval(arr):
    aces=0
    totalval=0
    for i in arr:
        try:
            totalval+=int(i)
        except:
            if i =="A":
                aces+=1
                totalval+=1
            else:
                totalval+=10
    for i in range(aces):
        if totalval+10<=21:
            totalval+=10
    return totalval

def dealerturn():
    print(f"\ndealer's hand: {','.join(dealer)}\nyour hand:{','.join(player)}")
    while handval(dealer)<17:
        time.sleep(0.7)
        dealer.append(hand[pickcard()])
        print(f"\ndealer's hand: {','.join(dealer)}\nyour hand:{','.join(player)}")
    time.sleep(0.3)
    if handval(dealer)>21:
        win()
    elif handval(dealer)>handval(player):
        bust()
    elif handval(dealer)<handval(player):
        win()
    else:
        tie()


def playerturn():
    choice=input("hit or stand?\n(h/s): ")
    if choice=="h":
        player.append(hand[pickcard()])
        print(f"\n\ndealer's hand: {dealer[0]},■\nyour hand:{','.join(player)}\n")
        if handval(player)>21:
            bust()
        else:
            playerturn()
    elif choice=="s":
        dealerturn()
    else:
        print("invalid input, try again")
        playerturn()

def newgame():
    global player,dealer,chosen,money,bet
    chosen=[]
    player=[]
    dealer=[]
    for i in range(2):
        player.append(hand[pickcard()])
        dealer.append(hand[pickcard()])
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        bet=int(input("\nyour bet: "))
        if bet<=0 or bet>money:
            print("\ninvalid. try again")
        else:
            break
    print(f"\ndealer's hand: {dealer[0]},■\nyour hand:{','.join(player)}\n")
    playerturn()

def win():
    global money
    money+=bet
    print("\nyou won!")
    print(f"you have {money} dollars left")
    redo()

def bust():
    global money
    print("\nyou lost!")
    money-=bet
    if money==0:
        print("you lost all your money")
    else:
        print(f"you have {money} dollars left")
        redo()

def tie():
    print("\nit's a tie!")
    print(f"you have {money} dollars left")
    redo()

def redo():
    a=input("\nplay new game? (y/n):")
    if a=="y":
        newgame()
    elif a=="n":
        gameover()
    else:
        print("invalid input, pls try again")
        redo()


def gameover():
    print(f"\n\nyou cashed out")
    print(f"your final balance is {money} dollars")


newgame()