class Enemy:
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Gobo(Enemy):
    def __init__(self):
        super().__init__(name="Gobo", description="""
        Gobo: A runt of a goblin-like creature, with green bulbous skin.
        """, hp=2, damage=1)
 
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", description="""
        Goblin: A full fledged goblin, warty, dark green and grinning evily.
        """, hp=5, damage=3)
  
class Orc(Enemy):
	  def __init__(self):
	    super().__init__(name="Orc", description="""
	    Orc: A hulking bestial-humanoid covered in dark fur, with sharp tusks and deep red eyes.""", hp=10, damage=5)