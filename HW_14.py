# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.strength = 1
        self.agility = 1
        self.intelligence = 1

    def heal(self):
        if self.health < 100 and self.health > 90:
            self.health += (100-self.health)
        if self.health < 100:
            self.health += 10

    def upgrade_skill(self):
        if isinstance(self, Mage):
            if self.intelligence < 10:
                self.intelligence += 1
        if isinstance(self, Archer):
            if self.agility < 10:
                self.agility += 1
        if isinstance(self, Knight):
            if self.strength < 10:
                self.strength += 1

    def read_unit(self):
        return self.name, self.clan


class Mage(Unit):
    def __init__(self, name, clan, class_magic):
        super().__init__(name, clan)
        self.class_magic = class_magic

    def create_mage(self, player_choice):
        if player_choice == 1:
            self.class_magic = "air"
        elif player_choice == 2:
            self.class_magic = "fire"
        elif player_choice == 3:
            self.class_magic = "water"
        else:
            return "Invalid"


class Archer(Unit):
    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon

    def create_archer(self, player_choice):
        if player_choice == 1:
            self.type_weapon = "bow"
        elif player_choice == 2:
            self.type_weapon = "crossbow"
        else:
            return "Invalid"

class Knight(Unit):
    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon

    def create_knight(self, player_choice):
        if player_choice == 1:
            self.type_weapon = "sword"
        elif player_choice == 2:
            self.type_weapon = "axe"
        elif player_choice == 3:
            self.type_weapon = "pike"
        else:
            return "Invalid"

