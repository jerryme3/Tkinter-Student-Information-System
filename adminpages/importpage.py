import os
import re
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from utilities import util


class ImportPage:

    def __init__(self, root):
        self.root = root
        self.utility = util.Utilities(root)
        self.import_page = tk.Frame(root, bg="white")
        self.import_page.pack(fill="both", expand=True)
        self.root.minsize(800, 600)

        self.sidebar()
        self.sidebar_buttons()
        self.import_content()
        self.add_background_logo()

    def add_background_logo(self):
        img = Image.open("assets/PNHS LOGO.png").convert("RGBA")
        img = img.resize((1300, 1300))
        img.putalpha(70)
        self.bg_image = ImageTk.PhotoImage(img)
        self.bg_label = tk.Label(self.main_frame, image=self.bg_image, bg="white")
        self.bg_label.place(relx=0.45, rely=0.1)
        self.bg_label.lower()

    def sidebar(self):
        self.bar = tk.Frame(self.import_page, bg="#3054B8", width=350)
        self.bar.pack(side="left", fill="y")
        self.bar.pack_propagate(False)

        img = Image.open("assets/PNHS_LOGO.jpg").resize((165, 165))
        self.bg_image1 = ImageTk.PhotoImage(img)
        self.bg_label1 = tk.Label(self.bar, image=self.bg_image1, bg="#3054B8")
        self.bg_label1.place(relx=0.25, rely=0.02)
        self.bg_label1.lower()

        self.utility.create_label(self.bar, "PORTAL", "#3054B8", "white", ("Arial", 16, "bold")).place(relx=0.5, rely=0.20, anchor="center")
        self.utility.create_label(self.bar, "ADMIN Panel", "#3054B8", "#E6DB75", ("Arial", 12, "bold")).place(relx=0.5, rely=0.24, anchor="center")
        self.utility.create_label(self.bar, "Panuelos National High School", "#3054B8", "white", ("Arial", 14, "normal")).place(relx=0.5, rely=0.27, anchor="center")

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

        imp_button = self.utility.create_button(self.bar, 35, "Import File", "#3E6CFA", self.show_import_page,
                                                ("Arial", 12))
        imp_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        imp_button.place(relx=0.029, rely=0.47)

        img = Image.open("assets/import.png").resize((46, 46))
        self.imp_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.imp_image, bg="#3E6CFA").place(relx=0.020, rely=0.47)

        activities_button = self.utility.create_button(self.bar, 35, "Activities", "#3054B8", self.show_activites_page,
                                                       ("Arial", 12))
        activities_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        activities_button.place(relx=0.029, rely=0.6)

        img = Image.open("assets/calendar.png").resize((50, 50))
        self.act_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.act_image, bg="#3054B8").place(relx=0.020, rely=0.598)

        img_logout = Image.open("assets/logout.png").resize((240, 200))
        self.logout_img = ImageTk.PhotoImage(img_logout)
        tk.Button(self.bar, image=self.logout_img, bg="#3054B8", borderwidth=0,
                  activebackground="#3054B8", command=self.confirm_logout, cursor="hand2").place(relx=0.15, rely=0.75)

    def import_content(self):
        from utilities import shared_state

        self.main_frame = tk.Frame(self.import_page, bg="#F0F4FA")
        self.main_frame.place(relx=0.18, rely=0, relwidth=0.9, relheight=1.0)

        self.utility.create_label(self.main_frame, "📤", "#F0F4FA", "#1E3A8A", ("Arial", 16)).place(x=30, y=25)
        self.utility.create_label(self.main_frame, "Import .csv / .xlsx File", "#F0F4FA", "#0F172A", ("Arial", 16, "bold")).place(x=65, y=25)
        tk.Frame(self.main_frame, bg="#93C5FD", height=1).place(x=30, y=65, relwidth=0.92)

        content_card = tk.Frame(self.main_frame, bg="#FFFFFF")
        content_card.config(highlightbackground="#E2E8F0", highlightthickness=1, bd=0)
        content_card.place(x=30, y=85, relwidth=0.92, relheight=0.50)

        self.utility.create_label(content_card, "📁", "#FFFFFF", "#3B82F6", ("Arial", 42)).place(relx=0.5, rely=0.22, anchor="center")
        self.utility.create_label(content_card, "Select a student grade spreadsheet to upload", "#FFFFFF", "#1E3A8A", ("Arial", 15, "bold")).place(relx=0.5, rely=0.45, anchor="center")

        badge_frame = tk.Frame(content_card, bg="#FFFFFF")
        badge_frame.place(relx=0.5, rely=0.58, anchor="center")
        for fmt in [".csv", ".xlsx", ".xls"]:
            tk.Label(badge_frame, text=f"📄 {fmt}", bg="#E0F2FE", fg="#0369A1",
                     font=("Arial", 9, "bold"), padx=10, pady=3, bd=1, relief="solid").pack(side="left", padx=6)

        browse_btn = self.utility.create_button(content_card, None, "  📁 Browse File from Computer", "#3B82F6", self.browse_file, ("Arial", 11, "bold"))
        browse_btn.config(fg="white", relief="flat", cursor="hand2", padx=30, pady=10)
        browse_btn.place(relx=0.5, rely=0.78, anchor="center")


        recent_card = tk.Frame(self.main_frame, bg="#FFFFFF")
        recent_card.config(highlightbackground="#E2E8F0", highlightthickness=1, bd=0)
        recent_card.place(x=30, rely=0.63, relwidth=0.92, relheight=0.35)

        self.utility.create_label(recent_card, "🔄 RECENT IMPORTS", "#FFFFFF", "#94A3B8", ("Arial", 10, "bold")).place(x=20, y=15)


        self.recent_list_frame = tk.Frame(recent_card, bg="#FFFFFF")
        self.recent_list_frame.place(x=10, y=40, relwidth=0.97, relheight=0.80)


        self.render_recent_imports()

    def render_recent_imports(self):
        from utilities import shared_state


        for widget in self.recent_list_frame.winfo_children():
            widget.destroy()

        recent_list = shared_state.imported_data.get("recent_imports", [])

        if not recent_list:
            tk.Label(self.recent_list_frame, text="No files imported yet.", bg="#FFFFFF",
                     fg="#94A3B8", font=("Arial", 10)).pack(anchor="w", padx=10, pady=10)
            return

        for entry in recent_list:
            row = tk.Frame(self.recent_list_frame, bg="#FFFFFF")
            row.pack(fill="x", pady=3, padx=5)

            tk.Label(row, text="📋", bg="#DCFCE7", fg="#15803D",
                     font=("Arial", 14), padx=8, pady=4).pack(side="left")

            info_frame = tk.Frame(row, bg="#FFFFFF")
            info_frame.pack(side="left", padx=8)

            tk.Label(info_frame, text=entry["file_name"], bg="#FFFFFF", fg="#0F172A",
                     font=("Arial", 10, "bold"), anchor="w").pack(anchor="w")
            tk.Label(info_frame, text=entry["date"], bg="#FFFFFF", fg="#94A3B8",
                     font=("Arial", 8), anchor="w").pack(anchor="w")

            tk.Label(row, text="Done", bg="#DCFCE7", fg="#16A34A",
                     font=("Arial", 9, "bold"), padx=10, pady=2).pack(side="right", padx=5)

            tk.Frame(self.recent_list_frame, bg="#E2E8F0", height=1).pack(fill="x", padx=5)

    def browse_file(self):
        selected_file = filedialog.askopenfilename(
            title="Select Student Grade File",
            filetypes=[
                ("All Supported Files", "*.csv *.xlsx *.xls"),
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx *.xls"),
            ]
        )
        if selected_file:
            self.process_imported_file(selected_file)

    def handle_dropped_file(self, event):
        dropped_file = event.data
        if dropped_file.startswith('{') and dropped_file.endswith('}'):
            dropped_file = dropped_file[1:-1]
        if dropped_file:
            self.process_imported_file(dropped_file)

    def process_imported_file(self, file_path):
        from utilities import shared_state

        file_name = os.path.basename(file_path)
        _, extension = os.path.splitext(file_name)

        if extension.lower() not in ['.csv', '.xlsx', '.xls']:
            messagebox.showerror(
                "Invalid File Type",
                f"Unsupported file format: {extension}\nPlease select a .csv, .xlsx, or .xls file."
            )
            return

        try:
            if extension.lower() == '.csv':
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            df.columns = [c.strip() for c in df.columns]

            if 'Full Name' not in df.columns or 'Student ID' not in df.columns:
                messagebox.showerror(
                    "Missing Columns",
                    "The file must have 'Full Name' and 'Student ID' columns.\n\n"
                    f"Found columns: {', '.join(df.columns)}"
                )
                return


            base         = os.path.splitext(file_name)[0]
            readable     = re.sub(r'_+', ' ', base).strip()
            section_name = re.sub(r'\s{2,}', ': ', readable)


            shared_state.imported_data["rows"] = [
                r for r in shared_state.imported_data["rows"] if r[2] != section_name
            ]
            if section_name in shared_state.imported_data["sections"]:
                shared_state.imported_data["sections"].remove(section_name)


            grade_col = None
            for col in df.columns:
                if col.lower().startswith('grade'):
                    grade_col = col
                    break


            new_rows = []
            for _, row in df.iterrows():
                name       = str(row['Full Name']).strip()
                student_id = str(row['Student ID']).strip()
                try:
                    grade = int(row[grade_col]) if grade_col and pd.notna(row[grade_col]) else 0
                except (ValueError, TypeError):
                    grade = 0
                status = "Passed" if grade >= 75 else "Failed"
                new_rows.append((name, student_id, section_name, grade, status))


            shared_state.imported_data["rows"].extend(new_rows)
            shared_state.imported_data["sections"].append(section_name)


            now_str = datetime.now().strftime("%B %d, %Y  %I:%M %p")
            recent_list = shared_state.imported_data.setdefault("recent_imports", [])


            shared_state.imported_data["recent_imports"] = [
                e for e in recent_list if e["file_name"] != file_name
            ]

            shared_state.imported_data["recent_imports"].insert(0, {
                "file_name": file_name,
                "date": now_str,
                "section": section_name,
            })

            shared_state.imported_data["recent_imports"] = \
                shared_state.imported_data["recent_imports"][:5]


            self.render_recent_imports()

            total_sections = len(shared_state.imported_data["sections"])
            answer = messagebox.askyesno(
                "File Imported Successfully",
                f"Loaded {len(new_rows)} student(s) from:\n{file_name}\n\n"
                f"Section: {section_name}\n"
                f"Total sections imported so far: {total_sections}\n\n"
                "Go to the Student page to view the table?"
            )
            if answer:
                self.show_profile_page()

        except Exception as e:
            messagebox.showerror("Read Error", f"Could not read the file:\n{str(e)}")



    def show_profile_page(self):
        from adminpages.homepage import EditGradePage
        self.import_page.destroy()
        EditGradePage(self.root)

    def show_import_page(self):
        return

    def show_activites_page(self):
        from adminpages.activitiespage import ActivitiesPage
        self.import_page.destroy()
        ActivitiesPage(self.root)

    def confirm_logout(self):
        answer = messagebox.askyesno("Logout Confirmation", "Do you want to log out?")
        if answer:
            self.import_page.destroy()
            from studentpages.loginpage import LoginPage
            LoginPage(self.root)