
from src.user_management import register, login


# Kiểm tra đăng ký thành công
def test_register_success():
    assert register("thao123", "123456") == True


# Kiểm tra đăng ký khi bỏ trống
def test_register_empty():
    assert register("", "") == False


# Kiểm tra đăng nhập thành công
def test_login_success():
    assert login("thao123", "123456", "thao123", "123456") == True


# Kiểm tra đăng nhập sai mật khẩu
def test_login_wrong_password():
    assert login("thao123", "111111", "thao123", "123456") == False
