# Ruben
class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            print("the enemy is already defeated")
        elif actor.get_cords()[0] + self.range < target.get_cords()[0] and actor.get_cords()[1] + self.range < \
                target.get_cords()[1]:
            print(f'target is too far for weapon {self.name}')
        else:
            print(f'enemy was hit from weapon {self.name} , damage is {self.damage}')
            target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x = delta_x
        self.pos_y = delta_y

    def is_alive(self):
        return bool(self.hp)

    def get_damage(self, amount):
        self.hp = self.hp - amount if self.hp > amount else 0

    def get_cords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            Weapon.hit(self, target)
        else:
            print('i can hit only main hero')

    def __str__(self):
        print(f"“enemy is in the position({self.pos_x},{self.pos_y}) with weapon {self.weapon}")


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon
        self.count = 0

    def hit(self, target):
        if not isinstance(self, Weapon):
            print('i am unarmed')
        elif isinstance(target, BaseEnemy):
            Weapon.hit(self, target)
        else:
            print('i can hit only enemy')

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon.append(weapon)
        else:
            print("it’s not a Weapon")

    def next_weapon(self):
        if not len(self.weapon):
            print("i am unarmed")
        elif len(self.weapon) == 1:
            print("i have one weapon")
        else:
            if self.count < len(self.weapon):
                self.count += 1
                print(f"i take weapon {self.weapon[self.count]} ")

    def heal(self, amount):
        self.hp = self.hp + amount if self.hp + amount < 200 else 200


# Narek
def pr(n):
    for i in range(1, n + 1):
        print(i, end='')
    print()

pr(13)