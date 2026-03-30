import tkinter as tk
from tkinter import messagebox
from controller import auth_controller

def open_register():
    root = tk.Tk()
    root.title("Đăng ký")
    root.geometry("400x350")
    root.configure(bg="#f0f2f5")

    # ===== FRAME CHÍNH =====
    main_frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=1, relief="solid")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # ===== TITLE =====
    tk.Label(main_frame, text="Đăng ký tài khoản",
             font=("Arial", 16, "bold"), bg="white").pack(pady=10)

    # ===== EMAIL =====
    tk.Label(main_frame, text="Email", bg="white", anchor="w").pack(fill="x")
    entry_email = tk.Entry(main_frame, width=30)
    entry_email.pack(pady=5)

    # ===== PASSWORD =====
    tk.Label(main_frame, text="Mật khẩu", bg="white", anchor="w").pack(fill="x")
    entry_pass = tk.Entry(main_frame, width=30, show="*")  # ✅ che mật khẩu
    entry_pass.pack(pady=5)

    # ===== FUNCTIONS =====
    def back_login():
        root.destroy()
        from view.login_view import open_login
        open_login()

    def register():
        email = entry_email.get()
        password = entry_pass.get()

        if not email or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return

        if len(password) < 6:
            messagebox.showerror("Lỗi", "Mật khẩu phải >= 6 ký tự")
            return

        if auth_controller.register(email, password):
            messagebox.showinfo("Thành công", "Đăng ký thành công!")
            back_login()
        else:
            messagebox.showerror("Lỗi", "Email đã tồn tại!")

    # ===== BUTTON =====
    tk.Button(main_frame, text="Đăng ký", width=20, bg="#28a745", fg="white",
              command=register).pack(pady=10)

    tk.Button(main_frame, text="Quay lại đăng nhập",
              command=back_login, bg="white", fg="blue", bd=0).pack()

    root.mainloop()