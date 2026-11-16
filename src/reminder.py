
from datetime import datetime, timedelta


class ReminderManager:

    def __init__(self):
        self.schedules = []
        self.notifications = []

    # 1. Thêm lịch học
    def add_schedule(self, subject, start_time, location):
        schedule = {
            "subject": subject,
            "start_time": datetime.strptime(
                start_time, "%Y-%m-%d %H:%M"
            ),
            "location": location
        }

        self.schedules.append(schedule)
        return "Thêm lịch học thành công"

    # 2. Lấy danh sách lịch học
    def get_schedules(self):
        return self.schedules

    # 3. Tạo nhắc lịch học
    def create_reminder(self, subject, minutes_before=15):

        schedule = next(
            (s for s in self.schedules
             if s["subject"] == subject),
            None
        )

        if schedule is None:
            return "Không tìm thấy lịch học"

        if minutes_before < 0:
            return "Thời gian nhắc không hợp lệ"

        if self.is_duplicate(
            subject,
            schedule["start_time"]
        ):
            return "Nhắc lịch đã tồn tại"

        reminder = {
            "subject": schedule["subject"],
            "start_time": schedule["start_time"],
            "reminder_time": (
                schedule["start_time"]
                - timedelta(minutes=minutes_before)
            ),
            "location": schedule["location"],
            "shown": False
        }

        self.notifications.append(reminder)

        return "Tạo nhắc lịch thành công"

    # 4. Kiểm tra thời gian hiện tại
    def check_reminder(self, current_time):

        if isinstance(current_time, str):
            current_time = datetime.strptime(
                current_time, "%Y-%m-%d %H:%M"
            )

        results = []

        for reminder in self.notifications:

            if (reminder["reminder_time"] <= current_time
                    < reminder["start_time"]):
                results.append(reminder)

        return results

    # 5. Hiển thị thông báo khi sắp đến giờ học
    def show_notifications(self, current_time):

        due_reminders = self.check_reminder(current_time)
        results = []

        for reminder in due_reminders:

            if not reminder["shown"]:

                message = self.create_notification(reminder)

                results.append(message)
                reminder["shown"] = True

        return results

    # 6. Tạo nội dung thông báo
    def create_notification(self, reminder):

        return (
            f"Nhắc lịch học: {reminder['subject']} | "
            f"Thời gian: "
            f"{reminder['start_time'].strftime('%H:%M %d/%m/%Y')} | "
            f"Địa điểm: {reminder['location']}"
        )

    # 7. Kiểm tra thông báo trùng lặp
    def is_duplicate(self, subject, start_time):

        return any(
            reminder["subject"] == subject
            and reminder["start_time"] == start_time
            for reminder in self.notifications
        )

    # 8. Xem danh sách thông báo
    def get_reminders(self):
        return self.notifications
