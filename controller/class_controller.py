from model import class_model

# Thêm lớp
def add_class(data):
    try:
        class_model.add(data)
        return True
    except:
        return False

# Sửa lớp
def update_class(data):
    try:
        class_model.update(data)
        return True
    except:
        return False

# Xóa lớp
def delete_class(ma_lop):
    try:
        class_model.delete(ma_lop)
        return True
    except:
        return False

# Tìm lớp
def find_class(ma_lop):
    return class_model.find(ma_lop)

# Lấy tất cả lớp
def get_all():
    return class_model.get_all()