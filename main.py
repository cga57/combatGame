import sys
import json
import random

import ENEMY
import PLAYER


size = 8
units = 4
endCondition = False


def printEnemyList (enemyList):
  for x in range(len(enemyList)):
    print(enemyList[x].name, end = " ")
  print("\n")


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

def combat(player1, player2, player1AttackList, player2AttackList):
  for x in range(len(player1AttackList)):
    unitHp = player2.selectedUnits[x].hp
    attack = player1.selectedUnits[x].attack
    defence = player2.selectedUnits[x].defence
    damage = attack - defence
    if(damage < 0):
      damage = 0
    unitHp = unitHp - damage

  # for x in range(len(player2.selectedUnits)):
  #   if(player2.selectedUnits[x].hp <= 0):
  #     player2.selectedUnits.remove(player2.selectedUnits[x])

  for x in range(len(player1AttackList)):
    unitHp = player1.selectedUnits[x].hp
    attack = player1.selectedUnits[x].attack
    defence = player1.selectedUnits[x].defence
    damage = attack - defence
    if(damage < 0):
      damage = 0
    unitHp = unitHp - damage
    if(unitHp <= 0):
      player1.selectedUnits.remove(player1.selectedUnits[x].name)

def printInfo(player):
  for x in range(len(player.selectedUnits)):
    print(player.selectedUnits[x].enemyInfo())

def takeInputs(player,enemyPlayer):
  attackList = []
  for x in range(len(player.selectedUnits)):
      
      print("Your units ordering: ")
      printEnemyList(player.selectedUnits)
      print("Enemy Units Ordering: ")
      printEnemyList(enemyPlayer.selectedUnits)
      print("Turn for: " + player.selectedUnits[x].name)


      enemyTarget = input("Select enemy unit to target. Input number 1 to 4: ")

      attackList.append(enemyTarget)
  return attackList

def main():
  file = sys.argv[1]
  enemyList = readFile(file)
  

  player1 = PLAYER.Player()
  player2 = PLAYER.Player()
  # for x in range(4):
  player1.selectedUnits = []
  player2.selectedUnits = []
  for x in range(units):
    player1.selectedUnits.append(random.choice(enemyList))
    player2.selectedUnits.append(random.choice(enemyList))

  endCondition = False
  while(not endCondition):
    print("Player 1's turn")
    # errorDetected = False
    player1AttackList = []
    player2AttackList = []

    player1AttackList = takeInputs(player1,player2)

    print("\nPlayer 2's turn")
    player2AttackList = takeInputs(player2, player1)

    combat(player1, player2, player1AttackList, player2AttackList)
    print("Player 1 Units info listed here")
    printInfo(player1)
    print("Player 2 Unit info listed here")
    printInfo(player2)

    if (player1.selectedUnits == [] or player2.selectedUnits == []):
      endCondition = True




  


    


    
        
    


if __name__ == "__main__":
  main()




 
