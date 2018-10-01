import random
import items, enemies, actions, world

global start
start = True

class MapTile:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def intro_text(self):
		raise NotImplementedError()
	
	def modify_player(self, player):
		raise NotImplementedError()	
		
	#def get_description(self):
	  #raise NotImplementedError()
		
	def adjacent_moves(self):
	  moves = []
	  if world.tile_exists(self.x + 1, self.y):
	    moves.append(actions.MoveEast())
	  if world.tile_exists(self.x - 1, self.y):
	    moves.append(actions.MoveWest())
	  if world.tile_exists(self.x, self.y - 1):
	    moves.append(actions.MoveNorth())
	  if world.tile_exists(self.x, self.y + 1):
	    moves.append(actions.MoveSouth())
	  return moves
	  
	def avaliable_actions(self):
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		moves.append(actions.ViewEquipment())
		return moves

#################################Rooms##################################
	
class StartingRoom(MapTile):
  def intro_text(self):
    global start
    if start == True:
      start = False
      return"""You wake up in a dingy, musty smelling cave with nothing on you but your clothing...
		  """
    else:
      return"""
      This is the room you woke up in, still musty smelling.
      """
		
  def modify_player(self, player):
	  pass
	
class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.items = []
		self.items.append(item)
		super().__init__(x, y)
	
	def add_loot(self, player):
		for val in self.items:
			player.inventory.append(val)
		self.items = []
	
	def modify_player(self, player):
		pass
		#self.add_loot(player)
		
	def intro_text(self):
	  raise NotImplementedError()
	
	def additional_items(self, item):
		self.items.append(item)

	def avaliable_actions(self):
		if len(self.items) > 0:
			moves = super().avaliable_actions()
			moves.append(actions.PickUp(tile=self))
			return moves
		else:
			return super().avaliable_actions()
		
class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x,y)
	
	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("The {} does {} damage to you.".format(self.enemy.name, self.enemy.damage))
			print("You have {} HP remaining.".format(player.hp))
			
	def intro_text(self):
		raise NotImplementedError()
		
	def get_description(self):
	  return self.enemy.description
		
	def avaliable_actions(self):
	  if self.enemy.is_alive():
	    return[actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.ViewEnemy()]
	  else:
	    return self.adjacent_moves()

#############################################EmptyPaths#################################################

class EmptyCavePath(MapTile):
  def intro_text(self):
    return """
    This is an unremarkable section of cave.
    """
    
  def modify_player(self, player):
    pass

class LargeEmptyCavePath(MapTile):
  def intro_text(self):
    return """
    This is a large cave with a few interesting rock formations on the wall.
    """
    
  def modify_player(self, player):
    pass

class HugeEmptyCavePath(MapTile):
  def intro_text(self):
    return """
    This is a huge cave with a few mushrooms on the ground and water trickling down the wall.
    """
    
  def modify_player(self, player):
    pass

class MassiveEmptyCavePath(MapTile):
  def intro_text(self):
    return """
    This is a massive cavern with jagged stalactites and a few bats hanging from the ceiling.
    """
    
  def modify_player(self, player):
    pass

class DownEmptyCavePath(MapTile):
  def intro_text(self):
    return """
    This is a little cave path slopes downward gently.
    """
    
  def modify_player(self, player):
    pass

class CavernousPit(MapTile):
  def intro_text(self):
    return """
    This cave has a deep dark pit off to oneside of the room.
    """
    
  def modify_player(self, player):
    pass
  
class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
  
#####################################ENEMYROOMS##############################################################

class GoboRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Gobo())
    
  def intro_text(self):
    if self.enemy.is_alive():
      return """
      A slimey Gobo spots you enter!
      """
    else:
      return """
      You see the Gobo you killed in here, laying dead on the ground.
      """

class GoblinRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Goblin())
    
  def intro_text(self):
    if self.enemy.is_alive():
      return """
      A stout Goblin jumps out of the gloom as you enter!
      """
    else:
      return """
      You see the Goblin you killed in here,
      laying dead on the ground.
      """

class OrcRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Orc())
    
  def intro_text(self):
    if self.enemy.is_alive():
      return """
      As you enter you wake a sleeping Orc!
      """
    else:
      return """
      You see the Orc you killed in here,
      laying dead on the ground.
      """

##############################################################LOOTROOMS##############################################

class FindRockRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Rock())
    
  def intro_text(self):
    if len(self.items) == 0:
      return """
      This looks to be a narrow stretch of tunnel, You remember you picked up a rock in this room.
      """
    else:
      return """
    This is a narrow stretch of tunnel as you enter a fist-sized rock clatters on the ground.
    """

class FindDaggerRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Dagger())
    
  def intro_text(self):
    if len(self.items) == 0:
      return """
      This looks to be an ordinary dank empty cave.
      """
    else:
      return """
    This looks to be an ordinary dank empty cave but then you spot something shiny in the corner...
    """

class FindClothesChestRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.CleanGarbage(random.randint(2, 15)))
    super().additional_items(items.CleanShirt())
    super().additional_items(items.CleanPants())
    
  def intro_text(self):
    if len(self.items) == 3:
      return """
      In the corner of this dark cavern you see a discarded chest lying open on the ground...
      """
    else:
      return """
    The discarded chest you looted is still lying here.
    """
