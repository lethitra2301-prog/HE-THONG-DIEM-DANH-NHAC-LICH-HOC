
# Chức năng đăng ký tài khoản
def register(username, password):
    if not username or not password:
        return False

    return True


# Chức năng đăng nhập
def login(username, password, saved_username, saved_password):
    if username == saved_username and password == saved_password:
        return True

    return False
