
def attendance_rate(present, total):
    """
    Tinh ty le chuyen can cua sinh vien.
    """
    if total <= 0:
        return 0

    if present < 0 or present > total:
        raise ValueError("So buoi co mat khong hop le")

    return present / total * 100


def attendance_summary(present, total):
    """
    Tong hop thong tin diem danh.
    """
    if total < 0 or present < 0 or present > total:
        raise ValueError("Du lieu diem danh khong hop le")

    absent = total - present

    rate = attendance_rate(present, total)

    return {
        "present": present,
        "absent": absent,
        "total": total,
        "rate": round(rate, 2)
    }
