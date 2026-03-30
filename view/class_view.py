import tkinter as tk
from tkinter import ttk, messagebox
from controller import class_controller


def open_class():
    root = tk.Tk()
    root.title("Quản lý Lớp")
    root.geometry("750x520")
    root.configure(bg="#f0f2f5")

    # ===== MAIN FRAME =====
    main_frame = tk.Frame(root, bg="white", padx=15, pady=15, bd=1, relief="solid")
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=470)

    # ===== TITLE =====
    tk.Label(main_frame, text="QUẢN LÝ LỚP",
             font=("Arial", 14, "bold"),
             bg="white").pack(pady=10)

    # ===== TABLE =====
    tree = ttk.Treeview(main_frame,
                        columns=("MaLop", "TenLop"),
                        show="headings",
                        height=10)

    tree.heading("MaLop", text="Mã Lớp")
    tree.heading("TenLop", text="Tên Lớp")

    tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # ===== INPUT =====
    input_frame = tk.Frame(main_frame, bg="white")
    input_frame.pack(pady=5)

    tk.Label(input_frame, text="Mã Lớp", bg="white").grid(row=0, column=0, padx=5)
    e_ma = tk.Entry(input_frame, width=15)
    e_ma.grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Tên Lớp", bg="white").grid(row=0, column=2, padx=5)
    e_ten = tk.Entry(input_frame, width=20)
    e_ten.grid(row=0, column=3, padx=5)

    # ===== FUNCTIONS =====
    def load():
        tree.delete(*tree.get_children())
        for row in class_controller.get_all():
            tree.insert("", "end", values=row)

    def clear_input():
        e_ma.delete(0, tk.END)
        e_ten.delete(0, tk.END)

    def add():
        if not e_ma.get() or not e_ten.get():
            messagebox.showerror("Lỗi", "Nhập đầy đủ!")
            return
        if class_controller.class_exists(e_ma.get()):
            messagebox.showerror("Lỗi", "Mã lớp đã tồn tại!")
            return
        if class_controller.add_class((e_ma.get(), e_ten.get())):
            messagebox.showinfo("OK", "Thêm thành công")
            load()
            clear_input()

    def update():
        if class_controller.update_class((e_ten.get(), e_ma.get())):
            messagebox.showinfo("OK", "Sửa thành công")
            load()

    def delete():
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?"):
            if class_controller.delete_class(e_ma.get()):
                messagebox.showinfo("OK", "Xóa thành công")
                load()
                clear_input()

    def find():
        r = class_controller.find_class(e_ma.get())
        if r:
            e_ten.delete(0, tk.END)
            e_ten.insert(0, r[1])
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
            e_ma.delete(0, tk.END)
            e_ma.insert(0, values[0])
            e_ten.delete(0, tk.END)
            e_ten.insert(0, values[1])

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