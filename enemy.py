class Enemy:
  def __init__ (self,name,speed,hp,attack,defence):
    self.name = name
    self.speed = speed
    self.hp = hp
    self.attack = attack
    self.defence = defence
    self.inUse = False
  def __str__(self):
    return self.name
  def enemyInfo(self):
    print(self.name)
    print(self.speed)
    print(self.hp)
    print(self.attack)
    print(self.defence)