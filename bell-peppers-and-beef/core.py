def main() -> None:
    player_health = 99
    enemy_health = 100
    while player_health > 0 and enemy_health > 0:
        player_health -=10
        if player_health <= 0:
            print("enemy wins!")
            break
        print(f"player: {player_health}")
        enemy_health -=10
        if enemy_health <= 0:
            print("player wins!")
            break
        print(f"enemy: {enemy_health}")
    print("combat ended.")


if __name__ == "__main__":
    main()
