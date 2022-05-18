class Enemy:
  def __init__ (self,name,speed,hp,attack,defence):
    self.name = name
    self.speed = speed
    self.hp = hp
    self.attack = attack
    self.defence = defence
  def __str__(self):
    return self.name