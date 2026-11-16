
from reminder import ReminderManager

manager = ReminderManager()

# Thêm lịch học
manager.add_schedule(
    "Lập trình Python",
    "2026-11-17 07:00",
    "Phòng A101"
)

# Tạo nhắc lịch trước 15 phút
print(manager.create_reminder("Lập trình Python", 15))

# Xem danh sách lịch học
print("\nDANH SÁCH LỊCH HỌC:")
print(manager.get_schedules())

# Kiểm tra thông báo tại thời điểm 6 giờ 45
print("\nTHÔNG BÁO:")
result = manager.show_notifications("2026-11-17 06:45")

for notification in result:
    print(notification)

# Xem danh sách nhắc lịch
print("\nDANH SÁCH NHẮC LỊCH:")
print(manager.get_reminders())
