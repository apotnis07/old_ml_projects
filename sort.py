import random


def choose():
    words = ['apple','mango','orange','pineapple','kiwi','watermelon']
    pick=random.choice(words)
    return pick


def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled


def thank(p1name,p2name,p1p,p2p):
    print("Thank you ",p1name,"and",p2name,"for playing:")
    if(p1p>p2p):
        print("Player 1 won")
    elif(p1p<p2p):
        print("Player 2 won")
    elif p1p == p2p:
        print("It's a tie!")


def play():
    p1name=input("Enter name of player 1")
    p2name=input("Enter name of player 2")
    p1p=0
    p2p=0
    turn=0
    while 1:
        turn+=1
        picked_word=choose()
        q=jumble(picked_word)
        print(q)
        if turn % 2 != 0:
            print("Ready player 1")
            ans = input("Enter your answer")
            if ans == picked_word:
                print("Your guessed the word correct")
                p1p = p1p + 1
            else:
                print("Better luck next time")
                print("The correct answer was",picked_word)
            c = int(input("If you want to continue press 1 or else 0"))
            if c == 0:
                thank(p1name,p2name,p1p,p2p)
                break
        else:
            print("Ready player 2")
            ans = input("Enter your answer")
            if ans == picked_word:
                print("Your guessed the word correct")
                p2p = p2p + 1
            else:
                print("Better luck next time")
                print("The correct answer was", picked_word)
            c = int(input("If you want to continue press 1 or else 0"))
            if c == 0:
                thank(p1name, p2name, p1p, p2p)
                break


play()