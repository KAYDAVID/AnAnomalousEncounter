class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Garbage(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Garbage",
                         description="A stack of unidentifable filth, which you would have to pay someone to take.",
                         value=-100)

class CleanGarbage(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Stuff",
                         description="About {} random knick-knacks and other useless junk.".format(str(self.amt)),
                         value=0)												 

##############################################WEAPONS#######################################

class Weapon(Item):
    def __init__(self, name, description, value, range_type, damage):
        self.range_type = range_type
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Fist(Weapon):
    def __init__(self):
        super().__init__(name="Fist",
                         description="Just your fist.",
                         value=0,
                         range_type="Melee",
                         damage=1)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         range_type="Melee",
                         damage=3)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=3,
                         range_type="Melee",
                         damage=5)

class ShortSword(Weapon):
    def __init__(self):
        super().__init__(name="Short Sword",
                         description="A sharp blade about the length of your forearm, with a leather grip on the handle.",
                         value=5,
                         range_type="Melee",
                         damage=7)

class LongSword(Weapon):
    def __init__(self):
        super().__init__(name="Long Sword",
                         description="A sharp blade about 20 golf tees in length, with a black leather grip on the handle.",
                         value=5,
                         range_type="Melee",
                         damage=10)
                         
##########################################ARMOR###############################################

class Armor(Item):
  def __init__(self, name, description, value, state): #state 1=Aweful 2=Poor 3=Average 4=Good 5=Excellent
    self.state = state
    super().__init__(name, description, value)
    
  def __str__(self):
      return "{}\n=====\n{}\nValue: {}\nState: {}".format(self.name, self.description, self.value, self.state)
      
class DirtyShirt(Armor):
    def __init__(self):
        super().__init__(name="Dirty Shirt",
                         description="A nondescript shirt covered in dirt, holes, and possibly a little blood.",
                         value=0,
                         state="Average")

class DirtyPants(Armor):
    def __init__(self):
        super().__init__(name="Dirty Pants",
                         description="A pair of nondescript pants covered in dirt and stains and missing the lower left leg.",
                         value=0,
                         state="Average")

class CleanShirt(Armor):
    def __init__(self):
        super().__init__(name="Clean Shirt",
                         description="A nondescript white shirt, clean and with a swashbuckler-style look.",
                         value=1,
                         state="Average")

class CleanPants(Armor):
    def __init__(self):
        super().__init__(name="Clean Pants",
                         description="A pair of nondescript clean pants a little worn on the cuffs.",
                         value=1,
                         state="Average")