import random

class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def take_damage(self, attack_damage):
        # Подсчет полученного урона с учетом брони
        damage_taken = max(0, attack_damage - self.armor)
        self.health -= damage_taken
        return damage_taken

    def is_alive(self):
        return self.health > 0


class Player(Person):
    def attack(self, enemy):
        if enemy.is_alive():
            damage_dealt = self.take_damage(self.damage)
            print(f"Player attacks {enemy.__class__.__name__} for {damage_dealt} damage!")
            enemy.take_damage(self.damage)


class Enemy(Person):
    def attack(self, player):
        if player.is_alive():
            damage_dealt = self.take_damage(self.damage)
            print(f"{self.__class__.__name__} attacks Player for {damage_dealt} damage!")
            player.take_damage(self.damage)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        turn = random.choice(['player', 'enemy'])  # Случайный выбор, кто атакует первым
        print(f"{turn.capitalize()} attacks first!")

        while self.player.is_alive() and self.enemy.is_alive():
            if turn == 'player':
                self.player.attack(self.enemy)
                turn = 'enemy'
            else:
                self.enemy.attack(self.player)
                turn = 'player'
            print(f"Player Health: {self.player.health}, Enemy Health: {self.enemy.health}")

        if self.player.is_alive():
            print("Player wins!")
        else:
            print("Enemy wins!")


# Создание экземпляров классов
player = Player(health=100, damage=20, armor=5)
enemy = Enemy(health=80, damage=15, armor=3)

# Запуск игры
game = Game(player, enemy)
game.start()
