import tkinter as tk
from tkinter import messagebox
from controller import auth_controller
from view.menu_view import open_menu


def open_login():
    root = tk.Tk()
    root.title("Đăng nhập")
    root.geometry("400x350")
    root.configure(bg="#f0f2f5")

    # ===== FRAME CHÍNH =====
    main_frame = tk.Frame(root, bg="white", padx=25, pady=25, bd=1, relief="solid")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # ===== TITLE =====
    tk.Label(main_frame, text="Đăng nhập",
             font=("Arial", 16, "bold"), bg="white").pack(pady=10)

    # ===== EMAIL =====
    tk.Label(main_frame, text="Email", bg="white", anchor="w").pack(fill="x")
    entry_email = tk.Entry(main_frame, width=30)
    entry_email.pack(pady=5)

    # ===== PASSWORD =====
    tk.Label(main_frame, text="Mật khẩu", bg="white", anchor="w").pack(fill="x")
    entry_pass = tk.Entry(main_frame, width=30, show="*")
    entry_pass.pack(pady=5)

    # ===== FUNCTIONS =====
    def login():
        email = entry_email.get()
        password = entry_pass.get()

        if not email or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return

        if auth_controller.login(email, password):
            root.destroy()
            open_menu()
        else:
            messagebox.showerror("Lỗi", "Sai tài khoản")

    def go_register():
        root.destroy()
        from view.register_view import open_register
        open_register()

    # ===== BUTTON =====
    tk.Button(main_frame, text="Đăng nhập",
              width=20, bg="#1877f2", fg="white",
              font=("Arial", 10, "bold"),
              command=login).pack(pady=10)

    tk.Button(main_frame, text="Tạo tài khoản mới",
              width=20, bg="#42b72a", fg="white",
              command=go_register).pack(pady=5)

    root.mainloop()