
from src.schedule import validate_schedule, create_schedule


def test_valid_schedule():
    assert validate_schedule("Tin học", "7:00") == True


def test_empty_schedule():
    assert validate_schedule("", "") == False


def test_create_schedule():
    result = create_schedule("Tin học", "7:00")
    assert result["subject"] == "Tin học"
    assert result["time"] == "7:00"
