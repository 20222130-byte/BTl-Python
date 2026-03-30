# Hệ Thống Quản Lý Sinh Viên

Ứng dụng quản lý sinh viên được phát triển bằng Python với giao diện người dùng Tkinter. Hệ thống cho phép quản lý thông tin sinh viên, lớp học, và điểm số.

## 📋 Tính Năng

### 1. **Quản Lý Sinh Viên**
   - Thêm sinh viên mới (kiểm tra trùng mã sinh viên)
   - Xem danh sách tất cả sinh viên
   - Cập nhật thông tin sinh viên
   - Xóa sinh viên khỏi hệ thống
   - Tìm kiếm sinh viên theo mã
   - Thông tin: Mã SV, Tên, Ngày sinh, Giới tính, Lớp

### 2. **Quản Lý Lớp Học**
   - Thêm lớp mới (kiểm tra trùng mã lớp)
   - Xem danh sách lớp học
   - Cập nhật tên lớp
   - Xóa lớp khỏi hệ thống
   - Tìm kiếm lớp theo mã

### 3. **Quản Lý Điểm Số**
   - Thêm điểm cho sinh viên
   - Xem bảng điểm
   - Cập nhật điểm số
   - Xóa bản ghi điểm

### 4. **Hệ Thống Xác Thực**
   - Đăng nhập (default: tài khoản demo)
   - Đăng ký tài khoản mới
   - Quản lý người dùng

## 🛠️ Yêu Cầu Hệ Thống

- Python 3.7 hoặc cao hơn
- Tkinter (thường có sẵn với Python)
- SQLite3 (có sẵn với Python)

## 📦 Cài Đặt

### 1. Clone hoặc tải dự án
```bash
cd BTl-Python
```

### 2. Chạy ứng dụng
```bash
python main.py
```

Ứng dụng sẽ tự động:
- Khởi tạo cơ sở dữ liệu SQLite (nếu chưa tồn tại)
- Mở cửa sổ đăng nhập

## 🗂️ Cấu Trúc Dự Án

```
BTl-Python/
├── main.py                      # Entry point của ứng dụng
├── model/
│   ├── database.py              # Cấu hình và khởi tạo cơ sở dữ liệu
│   ├── student_model.py         # Xử lý dữ liệu sinh viên
│   ├── class_model.py           # Xử lý dữ liệu lớp học
│   ├── score_model.py           # Xử lý dữ liệu điểm số
│   └── user_model.py            # Xử lý dữ liệu người dùng
├── controller/
│   ├── student_controller.py    # Logic điều khiển sinh viên
│   ├── class_controller.py      # Logic điều khiển lớp học
│   ├── score_controller.py      # Logic điều khiển điểm số
│   └── auth_controller.py       # Logic xác thực người dùng
├── view/
│   ├── login_view.py            # Giao diện đăng nhập
│   ├── register_view.py         # Giao diện đăng ký
│   ├── menu_view.py             # Giao diện menu chính
│   ├── student_view.py          # Giao diện quản lý sinh viên
│   ├── class_view.py            # Giao diện quản lý lớp
│   └── score_view.py            # Giao diện quản lý điểm số
├── student.db                   # File cơ sở dữ liệu SQLite
│   
└── README.md                    # Tài liệu này
```

## 🏗️ Kiến Trúc MVC

Dự án sử dụng mô hình **MVC (Model-View-Controller)**:

- **Model**: Quản lý dữ liệu và tương tác với cơ sở dữ liệu
- **View**: Giao diện người dùng được xây dựng bằng Tkinter
- **Controller**: Xử lý logic nghiệp vụ và kết nối Model với View

## 💾 Cơ Sở Dữ Liệu

CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

-- Bảng users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Bảng Class
CREATE TABLE IF NOT EXISTS Class (
    MaLop VARCHAR(50) PRIMARY KEY,
    TenLop VARCHAR(255)
);

-- Bảng Student
CREATE TABLE IF NOT EXISTS Student (
    MaSV INT PRIMARY KEY,
    TenSV VARCHAR(255),
    NgaySinh DATE,
    GioiTinh VARCHAR(10),
    TenLop VARCHAR(50),
    FOREIGN KEY (TenLop) REFERENCES Class(MaLop)
);

-- Bảng Scores
CREATE TABLE IF NOT EXISTS Scores (
    MaSV INT PRIMARY KEY,
    Toan FLOAT,
    Van FLOAT,
    Anh FLOAT,
    FOREIGN KEY (MaSV) REFERENCES Student(MaSV)
);

## 🚀 Hướng Dẫn Sử Dụng

### Đăng Nhập
1. Chạy `python main.py`
2. Nhập username và password
3. Bấm "Đăng nhập"

### Quản Lý Sinh Viên
1. Từ menu chính, chọn "Quản Lý Sinh Viên"
2. **Thêm**: Nhập thông tin → Bấm "Thêm"
3. **Sửa**: Chọn từ bảng → Sửa thông tin → Bấm "Sửa"
4. **Xóa**: Chọn từ bảng → Bấm "Xóa"
5. **Tìm kiếm**: Nhập mã sinh viên → Bấm "Tìm"

### Quản Lý Lớp
1. Từ menu chính, chọn "Quản Lý Lớp"
2. Tương tự như quản lý sinh viên

### Quản Lý Điểm
1. Từ menu chính, chọn "Quản Lý Điểm"
2. Nhập mã sinh viên và các loại điểm
3. Bấm "Thêm" để lưu điểm

## ✅ Tính Năng Kiểm Tra

- ✓ Kiểm tra trùng mã sinh viên khi thêm
- ✓ Kiểm tra trùng mã lớp khi thêm
- ✓ Kiểm tra trường bắt buộc
- ✓ Xác nhận trước khi xóa
- ✓ Tìm kiếm dữ liệu

## 📝 Ghi Chú

- Ứng dụng sử dụng SQLite3 cho cơ sở dữ liệu cục bộ
- Dữ liệu được lưu trữ trong file `student.db`
- Giao diện được xây dựng toàn bộ bằng Tkinter

## 👨‍💻 Tác Giả

Dự án này được phát triển cho mục đích học tập


---

 

