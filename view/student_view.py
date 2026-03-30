import tkinter as tk
from tkinter import ttk, messagebox
from controller import student_controller
from model import class_model


def open_student():
    root = tk.Tk()
    root.title("Quản lý Sinh viên")
    root.geometry("1300x600")
    root.configure(bg="#f0f2f5")

    # ===== MAIN FRAME =====
    main_frame = tk.Frame(root, bg="white", padx=15, pady=15, bd=1, relief="solid")
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=1250, height=550)

    # ===== TITLE =====
    tk.Label(main_frame, text="QUẢN LÝ SINH VIÊN",
             font=("Arial", 14, "bold"),
             bg="white").pack(pady=10)

    # ===== TABLE =====
    tree = ttk.Treeview(main_frame,
                        columns=("MaSV", "Ten", "NgaySinh", "GioiTinh", "Lop"),
                        show="headings", height=10)

    tree.heading("MaSV", text="Mã SV")
    tree.heading("Ten", text="Tên")
    tree.heading("NgaySinh", text="Ngày sinh")
    tree.heading("GioiTinh", text="Giới tính")
    tree.heading("Lop", text="Lớp")

    # Set column widths
    tree.column("MaSV", width=100)
    tree.column("Ten", width=150)
    tree.column("NgaySinh", width=120)
    tree.column("GioiTinh", width=100)
    tree.column("Lop", width=100)

    tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # ===== INPUT =====
    input_frame = tk.Frame(main_frame, bg="white")
    input_frame.pack(pady=5)

    tk.Label(input_frame, text="Mã SV", bg="white").grid(row=0, column=0, padx=5)
    e_id = tk.Entry(input_frame, width=12)
    e_id.grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Tên", bg="white").grid(row=0, column=2, padx=5)
    e_name = tk.Entry(input_frame, width=15)
    e_name.grid(row=0, column=3, padx=5)

    tk.Label(input_frame, text="Ngày sinh", bg="white").grid(row=0, column=4, padx=5)
    e_dob = tk.Entry(input_frame, width=12)
    e_dob.grid(row=0, column=5, padx=5)

    # ===== GENDER + CLASS =====
    sub_frame = tk.Frame(main_frame, bg="white")
    sub_frame.pack(pady=5)

    gender = tk.StringVar(value="Nam")
    tk.Label(sub_frame, text="Giới tính", bg="white").grid(row=0, column=0)
    tk.Radiobutton(sub_frame, text="Nam", variable=gender, value="Nam", bg="white").grid(row=0, column=1)
    tk.Radiobutton(sub_frame, text="Nữ", variable=gender, value="Nữ", bg="white").grid(row=0, column=2)

    tk.Label(sub_frame, text="Lớp", bg="white").grid(row=0, column=3, padx=10)
    combo = ttk.Combobox(sub_frame,
                         values=[x[0] for x in class_model.get_all()],
                         width=15)
    combo.grid(row=0, column=4)

    # ===== FUNCTIONS =====
    def load():
        tree.delete(*tree.get_children())
        for r in student_controller.get_all():
            tree.insert("", "end", values=r)

    def clear_input():
        e_id.delete(0, tk.END)
        e_name.delete(0, tk.END)
        e_dob.delete(0, tk.END)
        combo.set("")
        gender.set("Nam")

    def add():
        if not e_id.get() or not e_name.get():
            messagebox.showerror("Lỗi", "Nhập đầy đủ!")
            return
        if student_controller.student_exists(e_id.get()):
            messagebox.showerror("Lỗi", "Mã sinh viên đã tồn tại!")
            return
        student_controller.add_student(
            (e_id.get(), e_name.get(), e_dob.get(), gender.get(), combo.get()))
        messagebox.showinfo("OK", "Thêm thành công")
        load()
        clear_input()

    def update():
        student_controller.update_student(
            (e_name.get(), e_dob.get(), gender.get(), combo.get(), e_id.get()))
        messagebox.showinfo("OK", "Sửa thành công")
        load()

    def delete():
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?"):
            student_controller.delete_student(e_id.get())
            messagebox.showinfo("OK", "Xóa thành công")
            load()
            clear_input()

    def find():
        r = student_controller.find_student(e_id.get())
        if r:
            e_name.delete(0, tk.END)
            e_name.insert(0, r[1])
            e_dob.delete(0, tk.END)
            e_dob.insert(0, r[2])
            gender.set(r[3])
            combo.set(r[4])
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy")

    def refresh():
        load()
        clear_input()

    def back():
        root.destroy()
        from view.menu_view import open_menu
        open_menu()

    # ===== CLICK TABLE → FILL INPUT =====
    def on_select(event):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            e_id.delete(0, tk.END)
            e_id.insert(0, values[0])
            e_name.delete(0, tk.END)
            e_name.insert(0, values[1])
            e_dob.delete(0, tk.END)
            e_dob.insert(0, values[2])
            gender.set(values[3])
            combo.set(values[4])

    tree.bind("<<TreeviewSelect>>", on_select)

    # ===== BUTTON =====
    btn_frame = tk.Frame(main_frame, bg="white")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Thêm", width=10, bg="#28a745", fg="white", command=add).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Sửa", width=10, bg="#ffc107", command=update).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Xóa", width=10, bg="#dc3545", fg="white", command=delete).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Tìm", width=10, bg="#17a2b8", fg="white", command=find).grid(row=0, column=3, padx=5)
    tk.Button(btn_frame, text="Refresh", width=10, command=refresh).grid(row=0, column=4, padx=5)
    tk.Button(btn_frame, text="Quay lại", width=10, command=back).grid(row=0, column=5, padx=5)

    load()
    root.mainloop()