import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from studentpages.loginpage import LoginPage
from utilities import util

class GradePage:

    def __init__(self, root):
        self.root = root
        self.utility = util.Utilities(root)

        self.grade_page = tk.Frame(root, bg="white")
        self.grade_page.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.sidebar()
        self.sidebar_buttons()
        self.logout_butn()
        self.profile_content()
        self.profile_line()
        self.profile_title()
        self.grade_details()
        self.add_background_logo()


    def sidebar(self):
        self.bar = tk.Frame(self.grade_page, bg="#3054B8", width=350)
        self.bar.place(x=0, y=0, relheight=1.0)


        head = tk.Label(self.bar, text="PORTAL\nPanuelos National High School",
                        bg="#3054B8", fg="white", font=("Arial", 14, "bold"))
        head.place(relx=0.5, rely=0.25, anchor="center")

    def add_background_logo(self):
        img = Image.open("assets/PNHS_LOGO.jpg")

        img = img.resize((165, 165))

        self.bg_image = ImageTk.PhotoImage(img)

        self.bg_label = tk.Label(
            self.bar,
            image=self.bg_image,
            bg="#3054B8"

        )
        self.bg_label.place(relx=0.25, rely=0.02)

        self.bg_label.lower()

    def sidebar_buttons(self):

        seperator = tk.Frame(
            self.bar,
            bg="white",
            height=3
        )

        seperator.place(
            relx=0.0,
            rely=0.299,
            relwidth=1.0
        )

        profile_button = self.utility.create_button(
            self.bar,
            35,
            "My Profile",
            "#3054B8",
            self.show_profile_page,
            ("Arial", 12),
        )

        profile_button.config(
            fg="white",
            relief="flat",
            pady=10,
            cursor="hand2",
        )

        profile_button.place(relx=0.029, rely=0.32)

        img = Image.open("assets/PROF.png")
        img = img.resize((70, 70))
        self.icon_image = ImageTk.PhotoImage(img)

        self.icon_label = tk.Label(
            self.bar,
            image=self.icon_image,
            bg="#3054B8"
        )

        self.icon_label.place(relx=0.018, rely=0.31)

        Update_Profile_button = self.utility.create_button(
            self.bar,
            35,
            "Update Profile",
            "#3054B8",
            self.show_update_profile,
            ("Arial", 12),
        )

        Update_Profile_button.config(
            fg="white",
            relief="flat",
            pady=10,
            cursor="hand2",
        )

        Update_Profile_button.place(relx=0.029, rely=0.39)

        img = Image.open("assets/UPD.png")
        img = img.resize((70, 70))
        self.UPD_image = ImageTk.PhotoImage(img)

        self.UPD_label = tk.Label(
            self.bar,
            image=self.UPD_image,
            bg="#3054B8"
        )

        self.UPD_label.place(relx=0.012, rely=0.37)

        grades_button = self.utility.create_button(
            self.bar,
            35,
            "Grades",
            "#3E6CFA",
            self.show_grade_page,
            ("Arial", 12),
        )

        grades_button.config(
            fg="white",
            relief="flat",
            pady=10,
            cursor="hand2",
        )

        grades_button.place(relx=0.029, rely=0.46)

        img = Image.open("assets/GRADE.png")
        img = img.resize((45, 45))
        self.GRD_image = ImageTk.PhotoImage(img)

        self.GRD_label = tk.Label(
            self.bar,
            image=self.GRD_image,
            bg="#3E6CFA"
        )

        self.GRD_label.place(relx=0.045, rely=0.46)

        rank_button = self.utility.create_button(
            self.bar,
            35,
            "Rankings",
            "#3054B8",
            self.show_rankings_page,
            ("Arial", 12),
        )

        rank_button.config(
            fg="white",
            relief="flat",
            pady=10,
            cursor="hand2",
        )

        rank_button.place(relx=0.025, rely=0.53)

        img = Image.open("assets/RANK.png").resize((69, 69))
        self.RNK_image = ImageTk.PhotoImage(img)

        self.RNK_label = tk.Label(
            self.bar,
            image=self.RNK_image,
            bg="#3054B8"
        )

        self.RNK_label.place(relx=0.010, rely=0.51)

        seperator2 = tk.Frame(
            self.bar,
            bg="white",
            height=3
        )

        seperator2.place(
            relx=0.0,
            rely=0.60,
            relwidth=1.0
        )

    def logout_butn(self):
        img = Image.open("assets/logout.png")
        img = img.resize((240, 200))

        self.logout_img = ImageTk.PhotoImage(img)

        logout_btn = tk.Button(
            self.bar,
            image=self.logout_img,
            bg="#3054B8",
            borderwidth=0,
            activebackground="#3054B8",
            command=self.confirm_logout,
            cursor="hand2"
        )

        logout_btn.place(relx=0.15, rely=0.75)

    def profile_line(self):
        seperator = tk.Frame(
            self.grade_page,
            bg="#173a9e",
            height=3
        )

        seperator.place(
            relx=0.24,
            rely=0.15,
            relwidth=0.74
        )

        seperator2 = tk.Frame(
            self.grade_page,
            bg="#173a9e",
            height=3
        )

        seperator2.place(
            relx=0.24,
            rely=0.31,
            relwidth=0.74
        )

    def profile_content(self):
        self.right_content = tk.Frame(self.grade_page, bg="white")
        self.right_content.place(x=350, y=0, relwidth=1.0, relheight=1.0)

    def profile_title(self):
        from studentpages.loginpage import LoginPage

        self.grade_title = tk.Label(self.right_content, text="Grades", bg="white",
                                    fg="black", font=("Arial", 50, "bold"))
        self.grade_title.place(relx=0.03, rely=0.05)

    def grade_details(self):
        import ast
        from studentpages.loginpage import LoginPage

        gwa = ast.literal_eval(LoginPage.get_current_user().grades)

        self.gwa_num = tk.Label(self.right_content, text=f'{round(sum(gwa)/9)}', bg="white",
                                font=("Arial", 60, "bold"), padx=10)
        self.gwa_num.place(relx=0.04, rely=0.18)

        self.gwa_text = tk.Label(self.right_content, text="GWA(General Weighted Average)",
                                 bg="white", font=("Arial", 20), fg="black")
        self.gwa_text.place(relx=0.10, rely=0.22)

        self.w_honors = tk.Label(self.right_content, text="90-94: with honors", bg="white",
                                font=("Arial", 15), padx=10)
        self.w_honors.place(relx=0.57, rely=0.28)

        self.w_hhonors = tk.Label(self.right_content, text="95-97: with high honors", bg="white",
                                 font=("Arial", 15), padx=10)
        self.w_hhonors.place(relx=0.57, rely=0.219)

        self.w_hhhonors = tk.Label(self.right_content, text="98-100: with highest honors", bg="white",
                                 font=("Arial", 15), padx=10)
        self.w_hhhonors.place(relx=0.569, rely=0.16)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", background="white", foreground="black",
                        font=("Arial", 14, "bold"), borderwidth=0)
        style.configure("Custom.Treeview", rowheight=35, font=("Arial", 12),
                        background="white", fieldbackground="white", borderwidth=0)

        style.layout("Custom.Treeview", [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

        cols = ("Program", "Grade")
        self.tree = ttk.Treeview(self.right_content, columns=cols, show="headings", style="Custom.Treeview")

        self.tree.column("Program", width=400, anchor="w")
        self.tree.column("Grade", width=100, anchor="center")

        curr_grades  = LoginPage.get_current_user().grades
        actual_grade = []

        for i in range(len(curr_grades)-1):
            pointed = curr_grades[i:i+2]

            if pointed.isdigit():
                actual_grade.append(pointed)

        for col in cols:

            self.tree.heading(col, text=col, anchor="w" if col == "Program" else "center")

        subjects = [
            ("General Mathematics", actual_grade[0]),
            ("Earth and Life Science", actual_grade[1]),
            ("Oral Communication", actual_grade[2]),
            ("Komunikasyon at Pananaliksik", actual_grade[3]),
            ("Introduction to Philosophy", actual_grade[4]),
            ("Physical Education and Health", actual_grade[5]),
            ("Empowerment Technologies (ICT)", actual_grade[6]),
            ("Discipline and Ideas in Social Science", actual_grade[7]),
            ("Personal Development", actual_grade[8])
        ]

        for sub in subjects:
            self.tree.insert("", "end", values=sub)


        self.tree.place(relx=0.04, rely=0.35, relwidth=0.85, relheight=0.55)

    def show_profile_page(self):
        from studentpages.homepage import ProfilePage
        self.grade_page.destroy()
        ProfilePage(self.root)

    def show_update_profile(self):
        from studentpages.updatepage import UpdateProfile
        self.grade_page.destroy()
        UpdateProfile(self.root)

    def show_grade_page(self):
        return

    def show_rankings_page(self):
        from studentpages.rankings import RankingsPage

        self.grade_page.destroy()

        RankingsPage(self.root)

    def confirm_logout(self):
        answer = messagebox.askyesno("Logout Confirmation", "Do you want to log out?")

        if answer:
            self.grade_page.destroy()
            from studentpages.loginpage import LoginPage
            LoginPage(self.root)
        else:
            pass