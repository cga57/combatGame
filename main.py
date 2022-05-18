import sys
import json
import random

import ENEMY
import PLAYER


size = 8

def readFile(file):
  enemyList = []
  with open(file, "r") as file:
    enemyListJson = json.load(file)
    # print(enemyListJson)
    for x in range(size):

      # map json object to class
      enemyObject = ENEMY.Enemy(enemyListJson["data"][x]["name"],
                          enemyListJson["data"][x]["attack"],
                          enemyListJson["data"][x]["speed"],
                          enemyListJson["data"][x]["hp"],
                          enemyListJson["data"][x]["defense"])
      enemyList.append(enemyObject)
  return enemyList

def main():
  file = sys.argv[1]
  enemyList = readFile(file)


  player1 = PLAYER.Player()
  player2 = PLAYER.Player()
  # for x in range(4):
  player1.selectedUnits = []
  player2.selectedUnits = []
  player1.selectedUnits.append(str(random.choice(enemyList)))
  player2.selectedUnits.append(str(random.choice(enemyList)))

  print(player1.selectedUnits)
  print(player2.selectedUnits)



  





if __name__ == "__main__":
    main()




 
