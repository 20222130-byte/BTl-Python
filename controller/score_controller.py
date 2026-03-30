from model import score_model

# Thêm điểm
def add_score(data):
    try:
        score_model.add(data)
        return True
    except:
        return False

# Sửa điểm
def update_score(data):
    try:
        score_model.update(data)
        return True
    except:
        return False

# Xóa điểm
def delete_score(ma_sv):
    try:
        score_model.delete(ma_sv)
        return True
    except:
        return False

# Tìm điểm
def find_score(ma_sv):
    return score_model.find(ma_sv)

# Lấy tất cả điểm
def get_all():
    return score_model.get_all()