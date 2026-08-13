import pytest

from dungeon import (
    move_coords,
    make_monster,
    combat_step,
    apply_potion_effect,
)


def test_move_coords_bounds():
    pos1 = move_coords(0, 0, "d")
    pos2 = move_coords(0, 0, "s")

    assert pos1 == (1, 0)
    assert pos2 == (0, 1)

    pos3 = move_coords(0, 0, "a")
    pos4 = move_coords(0, 0, "w")

    assert pos3 == (0, 0)
    assert pos4 == (0, 0)


def test_make_monster_ranges():
    monster = make_monster(False)
    boss = make_monster(True)

    assert monster["name"] == "Monster"
    assert 10 <= monster["hp"] <= 16

    assert boss["name"] == "Boss"
    assert boss["atk"] >= monster["atk"]


def test_combat_step_attack():
    player = {"hp": 30, "atk": 5}
    monster = {"hp": 20, "atk": 4}

    p1, m1, _ = combat_step(player, monster, "a")
    p2, m2, _ = combat_step(player, monster, "r")

    assert m1["hp"] == 15
    assert p1["hp"] == 26

    assert m2["hp"] == 20
    assert p2["hp"] == 28


def test_apply_potion_effect():
    player = {"hp": 20, "atk": 5, "potions": []}
    potion = {"hp": 10, "atk": 2}

    p1 = apply_potion_effect(player, potion)
    p2 = apply_potion_effect(p1, potion)

    assert p1["hp"] == 30
    assert p1["atk"] == 7

    assert p2["hp"] == 40
    assert p2["atk"] == 9


pytest.main(["-v", "--tb=line", "-rN", __file__])
