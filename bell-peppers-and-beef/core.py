import random

class Entity():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def get_damage(self):
        return random.randrange(10, 20)

def main() -> None:
    player = Entity("Player 1", 100)
    enemy = Entity("Enemy 1", 100)

    while player.hp > 0 and enemy.hp > 0:
        # Player on defense. Enemy attacking.
        damage = enemy.get_damage()
        player.hp -= damage
        print(f"{player.name} takes {damage} damage.")
        if player.hp <= 0:
            print(f"{enemy.name} wins!")
            break

        # Enemy on defense. Player attacking.
        damage = player.get_damage()
        enemy.hp -= damage
        print(f"{enemy.name} takes {damage} damage.")
        if enemy.hp <= 0:
            print(f"{player.name} wins!")
            break

        print(f"{player.name}: {player.hp} hp")
        print(f"{enemy.name}: {enemy.hp} hp\n")

    print("combat ended.")


if __name__ == "__main__":
    main()
