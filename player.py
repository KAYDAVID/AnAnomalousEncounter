import random
import items, world

class Player():
  def __init__(self):
    self.inventory = []
    self.equipped = [items.DirtyShirt(), items.DirtyPants()]
    self.hp = 100
    self.location_x, self.location_y = world.starting_position
    self.victory = False
  
  def is_alive(self):
    return self.hp > 0

  def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
      action_method(**kwargs)

  def print_inventory(self):
    if len(self.inventory) == 0:
      print("You find nothing of use on yourself!")
    else:
      for item in self.inventory:
        print(item, '\n')

  def print_equipment(self):
    if len(self.equipped) == 0:
      print("You find nothing of use on yourself!")
    else:
      for item in self.equipped:
        print(item, '\n')
  
  def print_enemy_description(self):
    print(world.tile_exists(self.location_x, self.location_y).get_description())
        
  def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    print(world.tile_exists(self.location_x, self.location_y).intro_text())

  def move_to(self, dx, dy):
    self.location_x = dx
    self.location_y = dy
    print(world.tile_exists(self.location_x, self.location_y).intro_text())

  def move_south(self):
    self.move(dx=0, dy=1)
  
  def move_north(self):
    self.move(dx=0, dy=-1)
  
  def move_east(self):
    self.move(dx=1, dy=0)
  
  def move_west(self):
    self.move(dx=-1, dy=0)

  def move_up(self, x, y):
    self.move_to(x, y)

  def move_down(self, x, y):
    self.move_to(x, y)

  def attack(self, enemy):
    best_weapon = None
    max_dmg = 0
    for i in self.inventory:
      if isinstance(i, items.Weapon):
        if i.damage > max_dmg:
          max_dmg = i.damage
          best_weapon = i
    if best_weapon == None:
      best_weapon = items.Fist()
    print("You use your {} against the {}!".format(best_weapon.name, enemy.name))
    enemy.hp -= best_weapon.damage
    if not enemy.is_alive():
      print("You killed the {}!".format(enemy.name))
    else: 
      print("{} HP is {}.".format(enemy.name, enemy.hp))

  def flee(self, tile):
    available_moves = tile.adjacent_moves()
    r = random.randint(0, len(available_moves)-1)
    self.do_action(available_moves[r])

  def pick_up(self, tile):
    tile.add_loot(self)

    