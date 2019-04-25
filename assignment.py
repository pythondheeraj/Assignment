import math
import pprint
pos = [0,0]
player1 =[]
player2 =[]
series_of_steps ={"Player1":player1,"Player2":player2}
nextPlayer= "Player1"
while True and pos !=[2, 0]:
    print('Current Position: %s' %(pos))
    s = str(input("Enter Steps:     "))
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    series_of_steps[nextPlayer].append("{} {}".format(direction,steps))
    nextPlayer= "Player2" if nextPlayer=="Player1" else "Player1"
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
print(round(math.sqrt(pos[1]**2+pos[0]**2)))
moves1 = " ,".join(series_of_steps["Player1"])
moves2 = " ,".join(series_of_steps["Player2"])
pprint.pprint("Moves for Player1 are {}".format(moves1))
pprint.pprint("Moves for Player2 are {}".format(moves2))


# Note :Input format 
# Enter Steps:     "UP 2"
# Enter Steps:     "DOWN 10"  etc

