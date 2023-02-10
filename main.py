import random


def thegame():
    rn = random.randint(1, 50)
    score = 0
    for i in range(10):
        un = int(input("Chance number %d : " % (i + 1)))
        if un == -1:
            break
        if un >= 1 and un <= 50:
            if un == rn:
                print("correct guess")
                score = score + 5
                print(score)
                rn = random.randint(1, 50)
            elif un > rn:
                print("The number is greater than expected")
                print("good luck")
                score = score - 1
                print(score)
            elif un < rn:
                print("The number is smaller than expected")
                print("good luck")
                score = score - 1
                print(score)
        else:
            print("The number is out of range")

def finalscore(score):
    if score > 0:
        print("congratulations")
        print("Final score = %d" % (score))
    elif score < 0:
        print("Good luck")
        print("Final score = %d" % (score))
    else:
        print("Try again")

if __name__ == '__main__':


  print("you have only 10 chance")
  print("Enter number between 1 and 50")
  print("To leave the game press -1")
  game = thegame()
  endgame = finalscore()




