import pytest

from src.grass import Grass


def test_init_success_grass(init_grass_dict) -> None:
    emerald_grass = init_grass_dict["emerald_grass"]

    assert emerald_grass.name == "emerald_grass"
    assert emerald_grass.description == "green grass"
    assert emerald_grass.price == 1500
    assert emerald_grass.quantity == 150
    assert emerald_grass.country == "Germany"
    assert emerald_grass.germination_period == 14
    assert emerald_grass.color == "Dark green"


def test_raise_value_error_zero_quantity():
    with pytest.raises(ValueError):
        Grass("emerald_grass", "green grass", 1500, 0, "Germany", 14, "Dark green")
