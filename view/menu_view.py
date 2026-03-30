import tkinter as tk

def open_menu():
    root = tk.Tk()
    root.title("Menu chính")
    root.geometry("400x350")
    root.configure(bg="#f0f2f5")

    # ===== FRAME CHÍNH =====
    main_frame = tk.Frame(root, bg="white", padx=30, pady=30, bd=1, relief="solid")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # ===== TITLE =====
    tk.Label(main_frame, text="MENU HỆ THỐNG",
             font=("Arial", 16, "bold"),
             bg="white").pack(pady=15)

    # ===== FUNCTIONS =====
    def open_student_screen():
        root.destroy()
        from view.student_view import open_student
        open_student()

    def open_class_screen():
        root.destroy()
        from view.class_view import open_class
        open_class()

    def open_score_screen():
        root.destroy()
        from view.score_view import open_score
        open_score()

    # ===== BUTTON =====
    tk.Button(main_frame,
              text="Quản lý Sinh viên",
              width=25, height=2,
              bg="#1877f2", fg="white",
              font=("Arial", 10, "bold"),
              command=open_student_screen).pack(pady=5)

    tk.Button(main_frame,
              text="Quản lý Lớp",
              width=25, height=2,
              bg="#42b72a", fg="white",
              font=("Arial", 10, "bold"),
              command=open_class_screen).pack(pady=5)

    tk.Button(main_frame,
              text="Quản lý Điểm",
              width=25, height=2,
              bg="#f39c12", fg="white",
              font=("Arial", 10, "bold"),
              command=open_score_screen).pack(pady=5)

    root.mainloop()