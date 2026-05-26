import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from utilities import util


class EditGradePage:

    def __init__(self, root):
        self.root = root
        self.utility = util.Utilities(root)
        self.home_page = tk.Frame(root, bg="#f1f5f9")
        self.home_page.pack(fill="both", expand=True)
        self.root.minsize(900, 620)

        self.edit_mode = False

        self.sidebar()
        self.sidebar_buttons()
        self.profile_content()
        self.profile_title()
        self.profile_line()
        self.add_background_logo()
        self.build_ui()

    def add_background_logo(self):
        img = Image.open("assets/PNHS LOGO.png").resize((420, 420))
        img = img.convert("RGBA")
        r, g, b, a = img.split()
        a = a.point(lambda p: int(p * 0.06))
        img.putalpha(a)
        self.bg_image = ImageTk.PhotoImage(img)
        self.bg_label = tk.Label(self.profile_page, image=self.bg_image, bg="white")
        self.bg_label.place(relx=1.0, rely=1.0, anchor="se")
        self.bg_label.lower()

    def sidebar(self):
        self.bar = tk.Frame(self.home_page, bg="#3054B8", width=350)
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

        student_button = self.utility.create_button(self.bar, 35, "Student", "#3E6CFA", self.show_profile_page, ("Arial", 12))
        student_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        student_button.place(relx=0.016, rely=0.35)

        img = Image.open("assets/pencil.png").resize((46, 46))
        self.pen_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.pen_image, bg="#3E6CFA").place(relx=0.021, rely=0.35)

        imp_button = self.utility.create_button(self.bar, 35, "Import File", "#3054B8", self.show_import_page, ("Arial", 12))
        imp_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        imp_button.place(relx=0.029, rely=0.47)

        img = Image.open("assets/import.png").resize((50, 50))
        self.imp_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.imp_image, bg="#3054B8").place(relx=0.020, rely=0.47)

        activities_button = self.utility.create_button(self.bar, 35, "Activities", "#3054B8", self.show_activites_page, ("Arial", 12))
        activities_button.config(fg="white", relief="flat", pady=10, cursor="hand2")
        activities_button.place(relx=0.029, rely=0.6)

        img = Image.open("assets/calendar.png").resize((50, 50))
        self.act_image = ImageTk.PhotoImage(img)
        tk.Label(self.bar, image=self.act_image, bg="#3054B8").place(relx=0.020, rely=0.598)

        img_logout = Image.open("assets/logout.png").resize((240, 200))
        self.logout_img = ImageTk.PhotoImage(img_logout)
        tk.Button(self.bar, image=self.logout_img, bg="#3054B8", borderwidth=0,
                  activebackground="#3054B8", command=self.confirm_logout, cursor="hand2").place(relx=0.15, rely=0.75)

    def profile_content(self):
        self.profile_page = tk.Frame(self.home_page, bg="white")
        self.profile_page.pack(side="right", fill="both", expand=True)

    def profile_title(self):
        title_frame = tk.Frame(self.profile_page, bg="white")
        title_frame.place(relx=0.0, rely=0.022, relwidth=1.0, relheight=0.10)

        img = Image.open("assets/pencil.png").resize((70, 70))
        self.pencil_image = ImageTk.PhotoImage(img)
        tk.Label(title_frame, image=self.pencil_image, bg="white").place(relx=0.020, rely=0.2)

        tk.Label(title_frame, text="Student", bg="white", fg="#0f172a",
                 font=("Segoe UI", 35, "bold")).place(relx=0.07, rely=0.5, anchor="w")

        self.edit_btn = tk.Button(
            title_frame,
            text="✎ Edit",
            bg="white",
            fg="#475569",
            font=("Segoe UI", 10),
            relief="solid",
            bd=1,
            padx=14,
            pady=5,
            cursor="hand2",
            activebackground="#f1f5f9",
            command=self.toggle_edit_mode,
        )
        self.edit_btn.place(relx=0.9, rely=0.5, anchor="center")

    def profile_line(self):
        tk.Frame(self.profile_page, bg="#173a9e", height=3).place(
            relx=0.02, rely=0.10, relwidth=0.96
        )


    def build_ui(self):

        self.card_total_var   = tk.StringVar(value="0")
        self.card_avg_var     = tk.StringVar(value="0")
        self.card_passing_var = tk.StringVar(value="0")
        self.card_pct_var     = tk.StringVar(value="0%")
        self.card_review_var  = tk.StringVar(value="0")

        card_defs = [
            (0.09, "TOTAL\nSTUDENTS", self.card_total_var,   None,                  "#2563eb"),
            (0.30, "CLASS\nAVERAGE",  self.card_avg_var,     "This Semester",       "#2563eb"),
            (0.52, "PASSING",         self.card_passing_var, self.card_pct_var,     "#16a34a"),
            (0.73, "FOR REVIEW",      self.card_review_var,  "Below 75",            "#dc2626"),
        ]
        for x, title, value_var, subtitle, color in card_defs:
            self.create_card(x, title, value_var, subtitle, color)


        search_frame = tk.Frame(self.profile_page, bg="white",
                                highlightbackground="#cbd5e1", highlightthickness=1)
        search_frame.place(relx=0.02, rely=0.42, relwidth=0.22, relheight=0.06)

        tk.Label(search_frame, text="🔍", bg="white", fg="#94a3b8",
                 font=("Segoe UI", 11)).pack(side="left", padx=(8, 4))

        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.filter_table())

        self.search = tk.Entry(search_frame, relief="flat", font=("Segoe UI", 11),
                               fg="#0f172a", bg="white", insertbackground="#0f172a",
                               textvariable=self.search_var)
        self.search.insert(0, "Student No.")
        self.search.config(fg="#94a3b8")
        self.search.pack(side="left", fill="both", expand=True, padx=(0, 8))

        def on_focus_in(e):
            if self.search.get() == "Student No.":
                self.search_var.set("")
                self.search.config(fg="#0f172a")

        def on_focus_out(e):
            if not self.search.get():
                self.search_var.set("Student No.")
                self.search.config(fg="#94a3b8")

        self.search.bind("<FocusIn>", on_focus_in)
        self.search.bind("<FocusOut>", on_focus_out)


        from utilities import shared_state
        imported_sections = shared_state.imported_data.get("sections", [])
        section_choices = imported_sections if imported_sections else [
            "Section 1: Rose", "Section 2: Gumamela", "Section 3: Sunflower"
        ]

        self.section_var = tk.StringVar(value=section_choices[0])
        self.section = ttk.Combobox(
            self.profile_page,
            textvariable=self.section_var,
            values=section_choices,
            font=("Segoe UI", 10),
            state="readonly",
        )
        self.section.place(relx=0.75, rely=0.42, relwidth=0.23, relheight=0.06)
        self.section_var.trace("w", lambda *args: self.filter_table())


        self.table_frame = tk.Frame(self.profile_page, bg="white",
                                    highlightbackground="#e2e8f0", highlightthickness=1)
        self.table_frame.place(relx=0.02, rely=0.51, relwidth=0.96, relheight=0.46)

        self.setup_table()

    def create_card(self, x, title, value_var, subtitle, color):

        card = tk.Frame(self.profile_page, bg="#f8fafc",
                        highlightbackground="#173a9e", highlightthickness=2)
        card.place(relx=x, rely=0.19, relwidth=0.17, relheight=0.17)

        tk.Label(card, text=title, bg="#f8fafc", fg="#64748b",
                 font=("Segoe UI", 9), justify="left").place(relx=0.08, rely=0.08)

        tk.Label(card, textvariable=value_var, bg="#f8fafc", fg=color,
                 font=("Segoe UI", 26, "bold")).place(relx=0.08, rely=0.40)


        if subtitle is not None:
            if isinstance(subtitle, tk.StringVar):
                tk.Label(card, textvariable=subtitle, bg="#f8fafc", fg="#94a3b8",
                         font=("Segoe UI", 9)).place(relx=0.08, rely=0.80)
            else:
                tk.Label(card, text=subtitle, bg="#f8fafc", fg="#94a3b8",
                         font=("Segoe UI", 9)).place(relx=0.08, rely=0.80)


    def update_cards(self):
        selected_section = self.section_var.get()


        section_rows = [r for r, _ in self.all_rows if str(r[2]) == selected_section]

        total   = len(section_rows)
        passing = sum(1 for r in section_rows if r[4] == "Passed")
        failed  = total - passing

        if total > 0:
            avg = round(sum(r[3] for r in section_rows) / total, 1)
            pct = round((passing / total) * 100, 1)
        else:
            avg = 0.0
            pct = 0.0

        self.card_total_var.set(str(total))
        self.card_avg_var.set(str(avg))
        self.card_passing_var.set(str(passing))
        self.card_pct_var.set(f"{pct}%")
        self.card_review_var.set(str(failed))


    def toggle_edit_mode(self):
        if not self.edit_mode:
            self.enter_edit_mode()
        else:
            self.save_edits()

    def enter_edit_mode(self):
        self.edit_mode = True
        self.edit_btn.config(text="💾 Save", bg="#2563eb", fg="white",
                             activebackground="#1d4ed8")
        self.tree.bind("<Double-1>", self.on_cell_double_click)

    def save_edits(self):
        self.edit_mode = False
        self.edit_btn.config(text="✎ Edit", bg="white", fg="#475569",
                             activebackground="#f1f5f9")
        self.tree.unbind("<Double-1>")


        tree_dict = {}
        for item in self.tree.get_children():
            vals = self.tree.item(item, "values")
            tags = self.tree.item(item, "tags")
            tag  = tags[0] if tags else "passed"
            tree_dict[vals[1]] = (vals, tag)

        new_all_rows = []
        for row_data, tag in self.all_rows:
            sid = row_data[1]
            if sid in tree_dict:
                new_all_rows.append(tree_dict[sid])
            else:
                new_all_rows.append((row_data, tag))
        self.all_rows = new_all_rows

        from utilities import shared_state
        shared_state.imported_data["rows"] = [r for r, _ in self.all_rows]


        self.update_cards()
        messagebox.showinfo("Saved", "Changes have been saved.")

    def on_cell_double_click(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return

        col_id    = self.tree.identify_column(event.x)
        item_id   = self.tree.identify_row(event.y)
        if not item_id:
            return

        col_index = int(col_id.replace("#", "")) - 1
        columns   = ("name", "student_no", "section", "grade", "status")
        col_name  = columns[col_index]

        if col_name != "grade":
            messagebox.showinfo("Edit", "Only the Grade column can be edited.\nDouble-click a cell in the GRADE column.")
            return

        values        = list(self.tree.item(item_id, "values"))
        current_grade = values[3]

        popup = tk.Toplevel(self.root)
        popup.title("Edit Grade")
        popup.resizable(False, False)
        popup.grab_set()
        popup.geometry(f"240x130+{event.x_root}+{event.y_root}")

        tk.Label(popup, text=f"Student:  {values[0]}", font=("Segoe UI", 9),
                 anchor="w").pack(fill="x", padx=14, pady=(12, 2))
        tk.Label(popup, text="New Grade (0–100):", font=("Segoe UI", 9),
                 anchor="w").pack(fill="x", padx=14)

        grade_var = tk.StringVar(value=str(current_grade))
        entry = tk.Entry(popup, textvariable=grade_var, font=("Segoe UI", 11),
                         justify="center")
        entry.pack(padx=14, pady=6, fill="x")
        entry.select_range(0, "end")
        entry.focus_set()

        def apply(event=None):
            raw = grade_var.get().strip()
            try:
                new_grade = float(raw)
                if not (0 <= new_grade <= 100):
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid", "Please enter a number between 0 and 100.",
                                     parent=popup)
                return

            new_status = "Passed" if new_grade >= 75 else "Failed"
            new_tag    = "passed" if new_status == "Passed" else "failed"

            values[3] = new_grade
            values[4] = new_status
            self.tree.item(item_id, values=values, tags=(new_tag,))


            for i, (row_data, tag) in enumerate(self.all_rows):
                if row_data[1] == values[1]:   # match by student_no
                    updated = list(row_data)
                    updated[3] = new_grade
                    updated[4] = new_status
                    self.all_rows[i] = (tuple(updated), new_tag)
                    break

            self.update_cards()
            popup.destroy()

        entry.bind("<Return>", apply)
        tk.Button(popup, text="Apply", command=apply,
                  bg="#2563eb", fg="white", relief="flat",
                  padx=12, pady=4, cursor="hand2").pack(pady=(0, 10))


    def filter_table(self):
        if not hasattr(self, 'tree') or not hasattr(self, 'all_rows'):
            return

        query = self.search_var.get().strip().lower()
        if query == "student no.":
            query = ""

        selected_section = self.section_var.get()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row_data, tag in self.all_rows:
            student_no = str(row_data[1]).lower()
            section    = str(row_data[2])

            if query and query not in student_no:
                continue
            if section != selected_section:
                continue

            item_id = self.tree.insert("", "end", values=row_data)
            self.tree.item(item_id, tags=(tag,))


        self.update_cards()


    def setup_table(self):
        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="#1e293b",
                        fieldbackground="white", rowheight=40, borderwidth=0,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#f8fafc", foreground="#64748b",
                        relief="flat", font=("Segoe UI", 9, "bold"))
        style.map("Treeview",
                  background=[("selected", "#eff6ff"), ("!selected", "white")],
                  foreground=[("selected", "#1e3a8a")])

        columns = ("name", "student_no", "section", "grade", "status")
        self.tree = ttk.Treeview(self.table_frame, columns=columns,
                                 show="headings", selectmode="browse")
        self.tree.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical",
                                  command=self.tree.yview)
        scrollbar.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)
        self.tree.configure(yscrollcommand=scrollbar.set)

        headings = {"name": "STUDENT NAME", "student_no": "STUDENT NO.",
                    "section": "SECTION", "grade": "GRADE", "status": "STATUS"}
        widths   = {"name": 260, "student_no": 160, "section": 160,
                    "grade": 100, "status": 120}

        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(col, width=widths[col], anchor="center")

        self.tree.tag_configure("passed", foreground="green", background="white")
        self.tree.tag_configure("failed", foreground="red",   background="white")

        self.all_rows = []

        from utilities import shared_state
        imported_rows = shared_state.imported_data.get("rows", [])

        if imported_rows:
            for row_data in imported_rows:
                tag = "passed" if row_data[4] == "Passed" else "failed"
                self.all_rows.append((row_data, tag))
            self.filter_table()
        else:
            try:
                from models.database import Repository
                import ast

                table = Repository().get_table()
                for i in range(1, len(table)):
                    curr   = table[i]
                    grade  = round(sum(ast.literal_eval(curr[6])) / 9)
                    status = "Passed" if grade >= 75 else "Failed"
                    tag    = "passed" if status == "Passed" else "failed"
                    row    = (curr[0], curr[1], curr[7], grade, status)
                    self.all_rows.append((row, tag))
                    item_id = self.tree.insert("", "end", values=row)
                    self.tree.item(item_id, tags=(tag,))

                self.update_cards()
            except Exception as e:
                print("Error loading data:", e)


    def show_profile_page(self):
        return

    def show_import_page(self):
        from adminpages.importpage import ImportPage
        self.home_page.destroy()
        ImportPage(self.root)

    def show_activites_page(self):
        from adminpages.activitiespage import ActivitiesPage
        self.home_page.destroy()
        ActivitiesPage(self.root)

    def confirm_logout(self):
        answer = messagebox.askyesno("Logout Confirmation", "Do you want to log out?")
        if answer:
            self.home_page.destroy()
            from studentpages.loginpage import LoginPage
            LoginPage(self.root)

    def start_window(self):
        self.root.mainloop()