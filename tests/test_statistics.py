
import pytest

from src.statistics import attendance_rate, attendance_summary


def test_attendance_rate():
    assert attendance_rate(8, 10) == 80.0


def test_zero_total():
    assert attendance_rate(0, 0) == 0


def test_attendance_summary():
    result = attendance_summary(8, 10)

    assert result["present"] == 8
    assert result["absent"] == 2
    assert result["total"] == 10
    assert result["rate"] == 80.0


def test_invalid_attendance():
    with pytest.raises(ValueError):
        attendance_summary(12, 10)
