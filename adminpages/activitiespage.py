import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry

from utilities import util


class ActivitiesPage:

    def __init__(self, root):
        self.root = root
        self.utility = util.Utilities(root)

        self.activities_page = tk.Frame(root, bg="white")
        self.activities_page.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        self.root.minsize(800, 600)

        self.sidebar()
        self.sidebar_buttons()
        self.act_title()
        self.profile_line()
        self.add_background_logo()
        self.activities_content()

    def add_background_logo(self):
        img = Image.open("assets/PNHS LOGO.png").convert("RGBA")
        img = img.resize((1300, 1300))
        img.putalpha(70)
        self.bg_image = ImageTk.PhotoImage(img)

        self.bg_label = tk.Label(
            self.activities_page,
            image=self.bg_image,
            bg="white"
        )
        self.bg_label.place(relx=0.45, rely=0.1)
        self.bg_label.lower()

    def sidebar(self):
        self.bar = tk.Frame(self.activities_page, bg="#3054B8", width=350)
        self.bar.pack(side="left", fill="y")
        self.bar.pack_propagate(False)

        img = Image.open("assets/PNHS_LOGO.jpg").resize((165, 165))
        self.bg_image1 = ImageTk.PhotoImage(img)

        self.bg_label1 = tk.Label(self.bar, image=self.bg_image1, bg="#3054B8")
        self.bg_label1.place(relx=0.25, rely=0.02)
        self.bg_label1.lower()

        portal_label = self.utility.create_label(
            self.bar, "PORTAL", "#3054B8", "white", ("Arial", 16, "bold")
        )
        portal_label.place(relx=0.5, rely=0.20, anchor="center")

        admin_label = self.utility.create_label(
            self.bar, "ADMIN Panel", "#3054B8", "#E6DB75", ("Arial", 12, "bold")
        )
        admin_label.place(relx=0.5, rely=0.24, anchor="center")

        school_label = self.utility.create_label(
            self.bar, "Panuelos National High School", "#3054B8", "white", ("Arial", 14, "normal")
        )
        school_label.place(relx=0.5, rely=0.27, anchor="center")

    def sidebar_buttons(self):
        tk.Frame(self.bar, bg="white", height=3).place(relx=0.0, rely=0.299, relwidth=1.0)
        tk.Frame(self.bar, bg="white", height=3).place(relx=0.0, rely=0.7, relwidth=1.0)

        student_button = self.utility.create_button(self.bar, 35, "Student", "#3054B8", self.show_profile_page,
                                                    ("Arial", 12))
        student_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        student_button.place(relx=0.016, rely=0.35)

        img = Image.open("assets/pencil.png").resize((50, 50))
        self.pen_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.pen_image, bg="#3054B8").place(relx=0.021, rely=0.35)

        imp_button = self.utility.create_button(self.bar, 35, "Import File", "#3054B8", self.show_import_page,
                                                ("Arial", 12))
        imp_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        imp_button.place(relx=0.029, rely=0.47)

        img = Image.open("assets/import.png").resize((50, 50))
        self.imp_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.imp_image, bg="#3054B8").place(relx=0.020, rely=0.47)

        activities_button = self.utility.create_button(self.bar, 35, "Activities", "#3E6CFA", self.show_activites_page,
                                                       ("Arial", 12))
        activities_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        activities_button.place(relx=0.029, rely=0.6)

        img = Image.open("assets/calendar.png").resize((45, 45))
        self.act_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.act_image, bg="#3E6CFA").place(relx=0.023, rely=0.6)

        img_logout = Image.open("assets/logout.png").resize((240, 200))
        self.logout_img = ImageTk.PhotoImage(img_logout)
        tk.Button(self.bar, image=self.logout_img, bg="#3054B8", borderwidth=0,
                  activebackground="#3054B8", command=self.confirm_logout, cursor="hand2").place(relx=0.15, rely=0.75)

    def profile_line(self):
        seperator = tk.Frame(self.activities_page, bg="#173a9e", height=3)
        seperator.place(relx=0.19, rely=0.15, relwidth=0.76)

        seperator2 = tk.Frame(self.activities_page, bg="#173a9e", height=3)
        seperator2.place(relx=0.19, rely=0.7, relwidth=0.76)

    def act_title(self):
        activity = tk.Label(
            self.activities_page,
            text="📅 Activities",
            bg="white",
            fg="black",
            font=("Arial", 35, "bold")
        )
        activity.place(relx=0.2, rely=0.08)

    def activities_content(self):
        from datetime import datetime

        self.container = tk.Frame(
            self.activities_page,
            bg="#F5F5F5",
            highlightbackground="#B8B8B8",
            highlightthickness=1
        )
        self.container.place(relx=0.22, rely=0.2, relwidth=0.66, relheight=0.45)

        new_act = tk.Label(
            self.container,
            text="+  NEW ACTIVITY",
            bg="#F5F5F5",
            fg="#B0B0B0",
            font=("Arial", 16)
        )
        new_act.place(relx=0.02, rely=0.04)

        self.date_posted = datetime.today()
        self.date_posted = self.date_posted.strftime("%m/%d/%Y")

        self.date = DateEntry(
            self.container,
            background="#2E4FA8",
            foreground="white",
            borderwidth=1,
            date_pattern="mm/dd/yyyy",
            font=("Arial", 13)
        )
        self.date.place(relx=0.06, rely=0.18, relwidth=0.32, relheight=0.12)

        self.description = tk.Text(
            self.container,
            font=("Arial", 13),
            relief="solid",
            bd=1
        )
        self.placeholder_text = "Description and Instruction...."
        self.description.insert("1.0", self.placeholder_text)
        self.description.place(relx=0.06, rely=0.35, relwidth=0.50, relheight=0.38)

        self.dropdown = tk.StringVar(value="Project")
        dropdown_menu = tk.OptionMenu(
            self.container,
            self.dropdown,
            "Activity",
            "Quiz",
            "Project"
        )
        dropdown_menu.config(font=("Arial", 12), bg="white", relief="solid", cursor="hand2")
        dropdown_menu.place(relx=0.68, rely=0.08, relwidth=0.24, relheight=0.12)

        self.dropdown_sec = tk.StringVar(value="All Sections")
        section_menu = tk.OptionMenu(
            self.container,
            self.dropdown_sec,
            "All Sections",
            "Rose Garden",
            "Gumamela Grove",
            "Sunflower Field"
        )
        section_menu.config(font=("Arial", 12), bg="white", relief="solid", cursor="hand2")
        section_menu.place(relx=0.68, rely=0.35, relwidth=0.24, relheight=0.12)

        post_btn = tk.Button(
            self.container,
            text="💾 Post Activity",
            bg="white",
            fg="black",
            font=("Arial", 12, "bold"),
            relief="solid",
            bd=1,
            cursor="hand2",
            command=self.post
        )
        post_btn.place(relx=0.68, rely=0.56, relwidth=0.24, relheight=0.11)

        add_btn = tk.Button(
            self.container,
            text="↻ Revert Input",
            bg="#2E4FA8",
            fg="white",
            activebackground="#2E4FA8",
            activeforeground="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.revert
        )
        add_btn.place(relx=0.68, rely=0.71, relwidth=0.24, relheight=0.11)

    def revert(self):
        self.description.delete("1.0", "end")
        self.dropdown.set("Project")
        self.dropdown_sec.set("All Sections")

    def post(self):
        date_text = self.date.get()
        desc_text = self.description.get("1.0", "end-1c").strip()
        section = self.dropdown_sec.get()

        if not desc_text or desc_text == self.placeholder_text:
            messagebox.showwarning("Warning", "Please enter a valid activity description.")
            return

        def assess_dropdown():
            import csv

            if self.dropdown.get() == "Quiz":
                with open(file="quiz.csv", mode="a", newline="") as csvfile:
                    writer = csv.writer(csvfile)

                    writer.writerow([self.date_posted, desc_text, date_text, section])
                    return

            elif self.dropdown.get() == "Project":
                with open(file="project.csv", mode="a", newline="") as csvfile:
                    writer = csv.writer(csvfile)

                    writer.writerow([self.date_posted, desc_text, date_text, section])
                    return

            elif self.dropdown.get() == "Activity":
                with open(file="activity.csv", mode="a", newline="") as csvfile:
                    writer = csv.writer(csvfile)

                    writer.writerow([self.date_posted, desc_text, date_text, section])
                    return

        try:
            if int(date_text[0:2]) < int(self.date_posted[0:2]) or int(date_text[6:10]) < int(self.date_posted[6:10]):
                messagebox.showwarning("Warning", "Please enter a valid due date.")
                return

            elif (int(date_text[0:2]) == int(self.date_posted[0:2]) or int(date_text[6:10]) == int(self.date_posted[6:10])) and int(date_text[3:5]) < int(self.date_posted[3:5]):
                messagebox.showwarning("Warning", "Please enter a valid due date.")
                return

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid due date.")

        assess_dropdown()

        messagebox.showinfo(
            "Success",
            f"Activity Posted!\nDate: {date_text}\nType: {self.dropdown.get()}"
        )

        self.revert()



    def show_profile_page(self):
        from adminpages.homepage import EditGradePage
        self.activities_page.destroy()
        EditGradePage(self.root)

    def show_import_page(self):
        from adminpages.importpage import ImportPage
        self.activities_page.destroy()
        ImportPage(self.root)

    def show_activites_page(self):
        return

    def confirm_logout(self):
        answer = messagebox.askyesno("Logout Confirmation", "Do you want to log out?")


        if answer:
            self.activities_page.destroy()
            from studentpages.loginpage import LoginPage
            LoginPage(self.root)
        else:
            pass