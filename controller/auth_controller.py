from model import user_model

# Đăng ký
def register(email, password):
    if not email or not password:
        return False
    return user_model.register(email, password)

# Đăng nhập
def login(email, password):
    if not email or not password:
        return False
    return user_model.login(email, password)