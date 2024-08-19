import random
import logos

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
userCards = []
comCards = []
userSum = 0
comSum = 0

def addCards():
    global userSum
    global comSum

    temp1 = random.choice(cards)
    temp2 = random.choice(cards)
    userCards.append(temp1)
    comCards.append(temp2)
    userSum += temp1
    comSum += temp2

def gameStart ():
    shouldPlay = input ("Do you want to play the game of Blackjack? Type 'y' or 'n': ").lower()

    if shouldPlay == 'y':
        print (logos.blackjackLogo)

        global userSum
        global comSum

        userSum = 0
        comSum = 0
        userCards.clear()
        comCards.clear()
        addCards()

    elif shouldPlay == 'n':
        exit ()
    
    gameContinue()

def isDraw ():
    if userSum == comSum:
        return True
    else:
        return False 

def hasUserWon():
    global userSum
    global comSum

    if userSum > comSum:
        return True
    elif comSum > userSum:
        return False

def printFinalScore():
    global userSum
    global comSum
    print(f"Your final hand: {userCards}, final score: {userSum}")
    print(f"Computer's final hand: {comCards}, final score: {comSum}")

def gameContinue():
    shouldContinue = 'y'
    while shouldContinue == 'y':
        addCards()

        print(f"Your cards: {userCards}, current score: {userSum}")
        print(f"Computer's first card: {comCards[0]}")

        if userSum <=21:
            shouldContinue = input ("Type 'y' to get another card, type 'n' to pass: ").lower()
            if shouldContinue == 'n':
                if hasUserWon():
                    printFinalScore()
                    print("You win! 😃")

                elif isDraw():
                    printFinalScore()
                    print("It's a draw! 😐")

                else:
                    printFinalScore()
                    print("You lose! 😭")

                break
        else:
            print(f"Your final hand: {userCards}, final score: {userSum}")
            print(f"Computer's final hand: [{comCards[0]}, {comCards[1]}], final score: {comCards[0]+comCards[1]}")
            print("You lose! 😭")
            break

    gameStart()

gameStart()