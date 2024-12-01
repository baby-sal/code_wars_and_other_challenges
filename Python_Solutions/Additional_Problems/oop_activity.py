# RPG Character Builder

### Description: Each student (or group) will create a set of classes representing characters,
# weapons, and items in a fantasy RPG.
# Characters will have different abilities, health levels, and weapons based on their type.

### Requirements

### 1. Base Class: Character

# * Attributes: name, health, strength, defense
#
#     * Methods:
#
#         * attack(target: Character): Calculates damage based on the character's strength and target’s defense, then
#           reduces target’s health.
#         * take_damage(amount: int): Reduces the character's health by a given amount.
#         * __str__: Returns a description of the character with health, strength, and other stats. (note from Hamed, you might want to google this. Its very easy)

class Character:

    total_cha = 0

    def __init__(self, name, health, strength, defense, speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        Character.total_cha += 1

    def get_health(self):
        return self.health

    def get_strength(self):
        return self.strength

    def set_health(self, health):
        self.health = health

    def attack(self, target):
        damage = target.get_strength()
        new_health = target.get_health() - damage
        target.set_health(new_health)
        return f"{self.name} struck {target.name} with damage of {damage}! {target.name} has {new_health} remaining!"

    def take_damage(self, damage_taken):
        damage_taken = 5
        damage_health = self.get_health() - damage_taken
        self.set_health(damage_health)
        return f"{self.name} was hit! {self.name} now has {damage_health}"

    def __str__(self):
        return (f"{self.name} has:\n"
                f"strength: {self.strength}\n"
                f"health: {self.health}\n"
                f"defense: {self.defense}\n"
                f"speed: {self.speed}")

# ### 2. Subclasses:
#
# Each class inherits from Character and overrides certain methods.
#
# #### Warrior:
#
# * Higher strength and defense, but slower speed.
# * Override attack to deal extra damage.

class Warrior(Character):
    def __init__(self, name, health, strength, defense, speed):
        super().__init__(name,health,strength,defense,speed)
        self.strength = strength + 10
        self.defense = defense + 10
        self.speed = speed - 10

    def attack(self, target):
        damage = target.get_strength()
        new_health = target.get_health() - (damage + 10)
        target.set_health(new_health)
        return f"{self.name} struck {target.name} with damage of {damage}! {target.name} has {new_health} remaining!"

# #### Mage:
#
# * Lower strength, but high magical power.
# * Has a cast_spell() method instead of a regular attack.

class Mage(Character):
    def __init__(self, name, health, strength, defense, speed, magical_power):
        super().__init__(name,health,strength,defense,magical_power)
        self.strength = strength - 10
        self.defense = defense
        self.speed = speed
        self.magical_power = magical_power

    def attack(self, target):
        pass

    def cast_spell(self):
        pass

# #### Archer:
#
# * Moderate strength and high speed.
# * Has a shoot_arrow() method that can hit a target from afar.

class Mage(Character):
    def __init__(self, name, health, strength, defense, speed):
        super().__init__(name,health,strength,defense,speed)
        self.strength = strength
        self.defense = defense
        self.speed = speed + 20

    def shoot_arrow(self,target):
        pass

# ### 3. Items
#
# (Think about what class this needs to inherit from)
#
# * Create an Item class (for potions, shields, etc.) with attributes like name, effect, and use().
#
# * Example:
#     * Potion: Restores health.
#     * shield: Temporarily boosts defense.

cha_1 = Character("Sally", 100, 100,100, 100)

print(Character.__str__(cha_1))