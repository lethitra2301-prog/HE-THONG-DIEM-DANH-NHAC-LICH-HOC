from src.attendance import attendance_status, mark_attendance

def test_student_present():
    assert attendance_status(True) == "Có mặt"

def test_student_absent():
    assert attendance_status(False) == "Vắng mặt"

def test_mark_attendance_success():
    records = {}

    result = mark_attendance(records, "SV001", True)

    assert result == True
    assert records["SV001"] == "Có mặt"

def test_mark_attendance_empty_id():
    records = {}

    result = mark_attendance(records, "", True)

    assert result == False
    assert records == {}
