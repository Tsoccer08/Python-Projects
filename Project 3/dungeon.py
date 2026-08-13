import random

SIZE = 5

POTION_TYPES = [
    {"name": "+7 HP +1 ATK", "hp": 7, "atk": 1},
    {"name": "+3 HP +2 ATK", "hp": 3, "atk": 2},
    {"name": "+10 HP +3 ATK", "hp": 10, "atk": 3}
]


# Room generation
def make_room(allow_boss):
    # Create empty grid
    grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]

    # Player always starts at (0, 0)
    start = (0, 0)
    grid[0][0] = "P"

    # All empty positions except start
    empties = [
        (x, y)
        for x in range(SIZE)
        for y in range(SIZE)
        if (x, y) != start
    ]

    boss_pos = None

    # Place boss if allowed (boss floor)
    if allow_boss:
        boss_pos = random.choice(empties)
        bx, by = boss_pos
        grid[by][bx] = "B"
        empties.remove(boss_pos)

    # Place door only if there is no boss
    door_pos = None

    if boss_pos is None:
        border = []

        for i in range(SIZE):
            border.append((i, 0))
            border.append((i, SIZE - 1))
            border.append((0, i))
            border.append((SIZE - 1, i))

        border = [p for p in border if p != start]

        door_pos = random.choice(border)
        dx, dy = door_pos
        grid[dy][dx] = "D"

        if door_pos in empties:
            empties.remove(door_pos)

    # Place 1–3 treasure tiles
    for _ in range(random.randint(1, 3)):
        if empties:
            x, y = random.choice(empties)
            grid[y][x] = "T"
            empties.remove((x, y))

    # Place 2 monsters
    for _ in range(2):
        if empties:
            x, y = random.choice(empties)
            grid[y][x] = "M"
            empties.remove((x, y))

    return grid, start, boss_pos, door_pos


# Movement helpers
def move_coords(px, py, d):
    dx = (d == "d") - (d == "a")
    dy = (d == "s") - (d == "w")

    nx, ny = px + dx, py + dy

    if 0 <= nx < SIZE and 0 <= ny < SIZE:
        return nx, ny

    return px, py


# Monster creation
def make_monster(is_boss):
    if is_boss:
        return {
            "name": "Boss",
            "hp": random.randint(30, 45),
            "atk": random.randint(6, 10)
        }

    return {
        "name": "Monster",
        "hp": random.randint(10, 16),
        "atk": random.randint(3, 5)
    }


# Combat logic
def combat_step(player, monster, action):
    p = dict(player)
    m = dict(monster)
    events = []

    if action == "a":
        m["hp"] -= p["atk"]
        events.append(("player_hit", p["atk"]))

        if m["hp"] > 0:
            p["hp"] -= m["atk"]
            events.append(("monster_hit", m["atk"]))

    elif action == "r":
        dmg = max(1, m["atk"] // 2)
        p["hp"] -= dmg
        events.append(("run", dmg))

    return p, m, events


# Potion effect
def apply_potion_effect(player, potion):
    return {
        "hp": player["hp"] + potion["hp"],
        "atk": player["atk"] + potion["atk"],
        "potions": player["potions"]
    }


# Grid update helper
def player_on_grid(grid, old_pos, new_pos):
    g = [row[:] for row in grid]

    ox, oy = old_pos
    nx, ny = new_pos

    g[oy][ox] = "."
    g[ny][nx] = "P"

    return g


# Main game loop
def main():
    # Initialize random number generator
    random.seed()

    # Display the dungeon grid
    def print_grid(g):
        for row in g:
            print(" ".join(row))

    # Allow the player to choose a potion from inventory
    def choose_potion(pots):
        print("\nYour potions:")

        for i, p in enumerate(pots):
            print(
                f"{i + 1}. {p['name']} "
                f"(+{p['hp']} HP, +{p['atk']} ATK)"
            )

        sel = input("Choose (0 to cancel): ")

        if sel.isdigit():
            num = int(sel)

            if 1 <= num <= len(pots):
                return num - 1

        return -1

    # Randomly decide which floor will contain the boss
    rooms_before_boss = random.randint(1, 3)
    boss_floor = rooms_before_boss + 1

    # Initialize starting floor, room, and player stats
    floor = 1
    grid, (px, py), _, _ = make_room(False)

    player = {
        "hp": 30,
        "atk": 6,
        "potions": []
    }

    running = True

    # Run the game until the player quits, wins, or dies
    while running:
        print(
            "\nLEGEND: P=You  M=Monster  B=Boss  "
            "D=Door  T=Treasure  .=Empty\n"
        )

        print_grid(grid)

        print(
            f"\nFloor {floor} | HP {player['hp']} | "
            f"ATK {player['atk']} | "
            f"Potions {len(player['potions'])}"
        )

        # Get and validate movement or action input
        cmd = input("W A S D | U = potion | Q = quit: ").lower()

        while cmd not in ["w", "a", "s", "d", "u", "q"]:
            print("You entered the wrong key.")

            cmd = input(
                "W A S D | U = potion | Q = quit: "
            ).lower()

        # Handle quitting the game
        if cmd == "q":
            print("Quitting...")
            running = False

        # Handle potion usage outside of combat
        elif cmd == "u":
            if not player["potions"]:
                print("No potions.")
            else:
                idx = choose_potion(player["potions"])

                if idx >= 0:
                    pot = player["potions"][idx]

                    player = apply_potion_effect(player, pot)

                    player["potions"] = [
                        p
                        for i, p in enumerate(player["potions"])
                        if i != idx
                    ]

                    print(
                        f"You used {pot['name']}: "
                        f"+{pot['hp']} HP, "
                        f"+{pot['atk']} ATK"
                    )

        # Handle player movement
        else:
            nx, ny = move_coords(px, py, cmd)
            tile = grid[ny][nx]

            if (nx, ny) != (px, py):

                # Handle moving through a door to the next floor
                if tile == "D":
                    floor += 1

                    grid, (px, py), _, _ = make_room(
                        floor == boss_floor
                    )

                    print(
                        f"\nYou pass through the door "
                        f"to Floor {floor}."
                    )

                # Handle picking up a treasure potion
                elif tile == "T":
                    pot = random.choice(POTION_TYPES).copy()

                    player["potions"].append(pot)

                    print(
                        f"\nYou picked up a potion: "
                        f"+{pot['hp']} HP, "
                        f"+{pot['atk']} ATK"
                    )

                    grid[ny][nx] = "."

                    grid = player_on_grid(
                        grid,
                        (px, py),
                        (nx, ny)
                    )

                    px, py = nx, ny

                # Handle combat with a monster or boss
                elif tile in ("M", "B"):
                    combat_origin = (px, py)

                    monster = make_monster(tile == "B")

                    print(
                        f"\nA {monster['name']} appears! "
                        f"HP {monster['hp']} "
                        f"ATK {monster['atk']}"
                    )

                    fight = True

                    while (
                        fight
                        and player["hp"] > 0
                        and monster["hp"] > 0
                    ):
                        print(
                            f"\nYou HP {player['hp']} "
                            f"ATK {player['atk']} | "
                            f"Enemy HP {monster['hp']}"
                        )

                        act = input(
                            "(A)ttack (P)otion (R)un: "
                        ).lower()

                        # Handle potion usage during combat
                        if act == "p":
                            if not player["potions"]:
                                print("You have no potions.")
                            else:
                                idx = choose_potion(
                                    player["potions"]
                                )

                                if idx >= 0:
                                    pot = player["potions"][idx]

                                    player = apply_potion_effect(
                                        player,
                                        pot
                                    )

                                    player["potions"] = [
                                        p
                                        for i, p in enumerate(
                                            player["potions"]
                                        )
                                        if i != idx
                                    ]

                                    print(
                                        f"You used {pot['name']}: "
                                        f"+{pot['hp']} HP, "
                                        f"+{pot['atk']} ATK"
                                    )

                        # Handle attacking or running
                        elif act == "a" or act == "r":
                            player, monster, events = combat_step(
                                player,
                                monster,
                                act
                            )

                            for etype, val in events:
                                if etype == "player_hit":
                                    print(
                                        f"You hit for {val}."
                                    )

                                if etype == "monster_hit":
                                    print(
                                        f"Enemy hits you for {val}."
                                    )

                                if etype == "run":
                                    print(
                                        f"You fled and took "
                                        f"{val} damage."
                                    )

                            if act == "r":
                                grid = player_on_grid(
                                    grid,
                                    (px, py),
                                    combat_origin
                                )

                                px, py = combat_origin
                                fight = False

                            else:
                                if monster["hp"] <= 0:
                                    print("Enemy defeated!")

                                    if random.random() < 0.5:
                                        pot = random.choice(
                                            POTION_TYPES
                                        ).copy()

                                        player["potions"].append(pot)

                                        print(
                                            "The monster dropped "
                                            f"a potion! "
                                            f"+{pot['hp']} HP "
                                            f"+{pot['atk']} ATK"
                                        )

                                    grid[ny][nx] = "."

                                    grid = player_on_grid(
                                        grid,
                                        (px, py),
                                        (nx, ny)
                                    )

                                    px, py = nx, ny
                                    fight = False

                                    if tile == "B":
                                        print(
                                            "\nYou defeated "
                                            "the Boss! YOU WIN!"
                                        )

                                        running = False

                                elif player["hp"] <= 0:
                                    print(
                                        "\nYou died. Game Over."
                                    )

                                    running = False
                                    fight = False

                        # Handle invalid combat input
                        else:
                            print("Invalid action.")

                # Handle moving onto an empty tile
                elif tile == ".":
                    grid = player_on_grid(
                        grid,
                        (px, py),
                        (nx, ny)
                    )

                    px, py = nx, ny

    # End-of-game message
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
