import tkinter as tk
from tkinter import ttk, messagebox
from controller import score_controller
from model import student_model


def open_score():
    root = tk.Tk()
    root.title("Quản lý Điểm")
    root.geometry("1200x600")
    root.configure(bg="#f0f2f5")

    # ===== MAIN FRAME =====
    main_frame = tk.Frame(root, bg="white", padx=10, pady=10)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tk.Label(main_frame, text="QUẢN LÝ ĐIỂM",
             font=("Arial", 16, "bold"),
             bg="white").pack(pady=10)

    # ===== TABLE FRAME (có scrollbar) =====
    table_frame = tk.Frame(main_frame, bg="white")
    table_frame.pack(fill=tk.BOTH, expand=True)

    # Scrollbar
    scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
    scroll_y = tk.Scrollbar(table_frame, orient="vertical")

    tree = ttk.Treeview(
        table_frame,
        columns=("MaSV", "TenSV", "Lop", "Toan", "Van", "Anh", "TB"),
        show="headings",
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
    )

    scroll_x.config(command=tree.xview)
    scroll_y.config(command=tree.yview)

    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(fill=tk.BOTH, expand=True)

    # ===== SET COLUMN WIDTH =====
    tree.heading("MaSV", text="Mã SV")
    tree.column("MaSV", width=80, anchor="center")

    tree.heading("TenSV", text="Tên SV")
    tree.column("TenSV", width=150)

    tree.heading("Lop", text="Lớp")
    tree.column("Lop", width=100, anchor="center")

    tree.heading("Toan", text="Toán")
    tree.column("Toan", width=80, anchor="center")

    tree.heading("Van", text="Văn")
    tree.column("Van", width=80, anchor="center")

    tree.heading("Anh", text="Tiếng Anh")
    tree.column("Anh", width=100, anchor="center")

    tree.heading("TB", text="Trung Bình")
    tree.column("TB", width=100, anchor="center")

    # ===== INPUT =====
    input_frame = tk.Frame(main_frame, bg="white")
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Mã SV", bg="white").grid(row=0, column=0)
    sv_list = [x[0] for x in student_model.get_all()]
    combo_sv = ttk.Combobox(input_frame, values=sv_list, width=12)
    combo_sv.grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Toán", bg="white").grid(row=0, column=2)
    e_toan = tk.Entry(input_frame, width=10)
    e_toan.grid(row=0, column=3)

    tk.Label(input_frame, text="Văn", bg="white").grid(row=0, column=4)
    e_van = tk.Entry(input_frame, width=10)
    e_van.grid(row=0, column=5)

    tk.Label(input_frame, text="Anh", bg="white").grid(row=0, column=6)
    e_anh = tk.Entry(input_frame, width=10)
    e_anh.grid(row=0, column=7)

    # ===== INFO =====
    info_frame = tk.Frame(main_frame, bg="white")
    info_frame.pack(pady=5)

    tk.Label(info_frame, text="Tên SV", bg="white").grid(row=0, column=0)
    entry_name = tk.Entry(info_frame, width=25, state="readonly")
    entry_name.grid(row=0, column=1, padx=5)

    tk.Label(info_frame, text="Lớp", bg="white").grid(row=0, column=2)
    entry_class = tk.Entry(info_frame, width=15, state="readonly")
    entry_class.grid(row=0, column=3, padx=5)

    # ===== FUNCTIONS =====
    def get_student_info(ma_sv):
        r = student_model.find(ma_sv)
        return (r[1], r[4]) if r else ("", "")

    def calculate_avg(t, v, a):
        return round((t + v + a) / 3, 2)

    def load():
        tree.delete(*tree.get_children())
        for row in score_controller.get_all():
            name, lop = get_student_info(row[0])
            avg = calculate_avg(row[1], row[2], row[3])
            tree.insert("", "end", values=(row[0], name, lop, row[1], row[2], row[3], avg))

    def clear():
        combo_sv.set("")
        e_toan.delete(0, tk.END)
        e_van.delete(0, tk.END)
        e_anh.delete(0, tk.END)
        entry_name.config(state="normal"); entry_name.delete(0, tk.END); entry_name.config(state="readonly")
        entry_class.config(state="normal"); entry_class.delete(0, tk.END); entry_class.config(state="readonly")

    def add():
        try:
            data = (combo_sv.get(), float(e_toan.get()), float(e_van.get()), float(e_anh.get()))
            score_controller.add_score(data)
            load(); clear()
        except:
            messagebox.showerror("Lỗi", "Sai dữ liệu")

    def update():
        try:
            data = (float(e_toan.get()), float(e_van.get()), float(e_anh.get()), combo_sv.get())
            score_controller.update_score(data)
            load()
        except:
            messagebox.showerror("Lỗi", "Sai dữ liệu")

    def delete():
        if messagebox.askyesno("Xác nhận", "Xóa?"):
            score_controller.delete_score(combo_sv.get())
            load(); clear()

    def find():
        r = score_controller.find_score(combo_sv.get())
        if r:
            e_toan.delete(0, tk.END); e_toan.insert(0, r[1])
            e_van.delete(0, tk.END); e_van.insert(0, r[2])
            e_anh.delete(0, tk.END); e_anh.insert(0, r[3])

    def refresh():
        load(); clear()

    def back():
        root.destroy()
        from view.menu_view import open_menu
        open_menu()

    # ===== EVENTS =====
    def on_select(event):
        item = tree.focus()
        if item:
            v = tree.item(item, "values")
            combo_sv.set(v[0])
            entry_name.config(state="normal"); entry_name.delete(0, tk.END); entry_name.insert(0, v[1]); entry_name.config(state="readonly")
            entry_class.config(state="normal"); entry_class.delete(0, tk.END); entry_class.insert(0, v[2]); entry_class.config(state="readonly")
            e_toan.delete(0, tk.END); e_toan.insert(0, v[3])
            e_van.delete(0, tk.END); e_van.insert(0, v[4])
            e_anh.delete(0, tk.END); e_anh.insert(0, v[5])

    tree.bind("<<TreeviewSelect>>", on_select)

    # ===== BUTTON =====
    btn_frame = tk.Frame(main_frame, bg="white")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Thêm", bg="#28a745", fg="white", width=10, command=add).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Sửa", bg="#ffc107", width=10, command=update).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Xóa", bg="#dc3545", fg="white", width=10, command=delete).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Tìm", bg="#17a2b8", fg="white", width=10, command=find).grid(row=0, column=3, padx=5)
    tk.Button(btn_frame, text="Refresh", width=10, command=refresh).grid(row=0, column=4, padx=5)
    tk.Button(btn_frame, text="Quay lại", width=10, command=back).grid(row=0, column=5, padx=5)

    load()
    root.mainloop()