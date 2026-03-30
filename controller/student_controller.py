from model import student_model

def add_student(data): student_model.add(data)
def update_student(data): student_model.update(data)
def delete_student(id): student_model.delete(id)
def find_student(id): return student_model.find(id)
def get_all(): return student_model.get_all()

def student_exists(id): 
    return student_model.exists_by_id(id)