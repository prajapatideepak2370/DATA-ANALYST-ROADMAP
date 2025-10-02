import random

def game():
    score = random.randint(1, 100)
    with open("file.txt" ) as f:
      hiscore = f.read()
    
    if (hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
    print(f"Your score is: {score}")
    if (score > hiscore):
        print("You have a new high score!")
        with open("file.txt", "w") as f:
            f.write(str(score))
            
    return score
game()