class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.hp != 0:
            if ((actor.pos_x - target.pos_x)**2 + (actor.pos_y - target.pos_y)**2)**0.5 <= actor.weapon.range:
                target.get_damage(self.damage)
            else:
                print(f"target is too far for weapon {self.damage}")
        else:
            print("the enemy is already defeated")
        print(f"enemy was hit from weapon {self.name}, damage is {self.damage}")

    def __repr__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return bool(self.hp)

    def get_damage(self, amount):
        self.hp = self.hp - amount if self.hp > amount else 0

    def get_cords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp, weapon):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("i can hit only main hero")


    def __str__(self):
        return f"enemy is in the position {self.pos_x, self.pos_y} with weapon {self.weapon}"


class MainHero(BaseCharacter):
    weapons = []
    count = 0
    def __init__(self, pos_x, pos_y, hp, name):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = name

    def hit(self, target):
        if len(MainHero.weapons) != 0:
            if isinstance(target, BaseEnemy):
                self.weapon.hit(self, target)
            else:
                print("i can hit only enemy")
        else:
            print("i am unarmed")

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            print(f"picked up {weapon.name}")
            MainHero.weapons.append(weapon)
            self.weapon = weapon
        else:
            print("it’s not a weapon")

    def next_weapon(self):
        global count
        if len(MainHero.weapons) == 0:
            print("“i am unarmed")
        elif len(MainHero.weapons) == 1:
            print("i have one weapon")
        else:
            self.weapon = MainHero.weapons[count]
            count = count + 1 if count < len(MainHero.weapons) else 0
            print(f"i take weapon {self.weapon.name}")

    def heal(self, amount):
        self.hp = self.hp + amount if self.hp + amount <= 200 else 200
        print(f"now my health is {self.hp}")


weapon1 = Weapon("Короткый меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 499, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, 100, weapon3)
armored_swordsman = BaseEnemy(10, 10, 500, weapon2)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_cords())
main_hero = MainHero(0, 0, 200, "Arthur")
main_hero.add_weapon(weapon4)
main_hero.hit(princess)
print(armored_swordsman.hp)
main_hero.hit(armored_swordsman)
print(armored_swordsman.hp)







