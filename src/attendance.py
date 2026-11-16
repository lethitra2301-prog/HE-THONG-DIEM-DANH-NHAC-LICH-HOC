def attendance_status(is_present):
    if is_present:
        return "Có mặt"
    return "Vắng mặt"
def mark_attendance(attendance_records, student_id, is_present):
    if not student_id or not student_id.strip():
        return False

    status = attendance_status(is_present)

    attendance_records[student_id] = status

    return True