
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.reminder import ReminderManager


# Kiểm tra 1: Thêm lịch học
def test_add_schedule():
    manager = ReminderManager()

    result = manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    assert result == "Thêm lịch học thành công"


# Kiểm tra 2: Lấy danh sách lịch học
def test_get_schedules():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    assert len(manager.get_schedules()) == 1


# Kiểm tra 3: Tạo nhắc lịch trước 15 phút
def test_create_reminder():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    result = manager.create_reminder("Python", 15)

    assert result == "Tạo nhắc lịch thành công"
    assert manager.get_reminders()[0]["reminder_time"].strftime(
        "%H:%M"
    ) == "06:45"


# Kiểm tra 4: Kiểm tra thời gian hiện tại
def test_check_reminder():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    manager.create_reminder("Python", 15)

    result = manager.check_reminder("2026-11-17 06:45")

    assert len(result) == 1


# Kiểm tra 5: Hiển thị thông báo
def test_show_notifications():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    manager.create_reminder("Python", 15)

    result = manager.show_notifications("2026-11-17 06:45")

    assert len(result) == 1


# Kiểm tra 6: Hiển thị thông tin môn học
def test_notification_information():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    manager.create_reminder("Python", 15)

    result = manager.show_notifications("2026-11-17 06:45")

    assert "Python" in result[0]
    assert "07:00" in result[0]
    assert "A101" in result[0]


# Kiểm tra 7: Hạn chế thông báo trùng lặp
def test_duplicate_reminder():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    manager.create_reminder("Python", 15)

    result = manager.create_reminder("Python", 15)

    assert result == "Nhắc lịch đã tồn tại"


# Kiểm tra 8: Xem danh sách thông báo
def test_get_reminders():
    manager = ReminderManager()

    manager.add_schedule(
        "Python",
        "2026-11-17 07:00",
        "A101"
    )

    manager.create_reminder("Python", 15)

    assert len(manager.get_reminders()) == 1
