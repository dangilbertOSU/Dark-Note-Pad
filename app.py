import tkinter as tk
from tkinter import filedialog as fd


class DarkNotePad(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Dark Notepad")

        # setting the global textbox variable
        self.textbox = None

        self.create_shortcuts()
        self.create_window()

    def create_window(self):
        window_height = 500
        window_width = 900

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.master.geometry(
            "{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        self.create_widgets(screen_width, screen_height)

    def create_widgets(self, height, width):
        self.create_menu()
        self.create_textbox(height, width)
        scrollbar = tk.Scrollbar(self.master)
        scrollbar.pack(side=tk.RIGHT, fill='y')

    def create_menu(self):
        menu_bar = tk.Menu(self.master)

        # file
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(
            label="Open", command=self.open, accelerator="Ctrl+O")
        file_menu.add_command(
            label="Save", command=self.save, accelerator="Ctrl+S")
        menu_bar.add_cascade(label="File", menu=file_menu)

        # edit
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.master.config(menu=menu_bar)

    def create_textbox(self, height, width):
        # background =  #282c34
        # font = #a7aebb
        # cursor = #568af2
        self.textbox = tk.Text(self, font=("system", 16, "normal"), width=width, height=height, bg='#282c34',
                               fg='#a7aebb', padx=5, pady=5, highlightthickness=0)
        self.textbox.pack()
        self.textbox.focus()
        self.textbox.config(insertbackground='#568af2')

    def create_shortcuts(self):
        self.master.bind("<Control-s>", self.save_event)
        self.master.bind("<Command-s>", self.save_event)
        self.master.bind("<Control-o>", self.open_event)
        self.master.bind("<Command-o>", self.open_event)

    def save(self):
        input_text = self.textbox.get("1.0", "end")
        file_out = fd.asksaveasfile(mode='w', defaultextension=".txt")

        # asksaveasfile return `None` if dialog closed with "cancel".
        if file_out is None:
            return
        file_out.write(input_text)
        file_out.close()

    def open(self):
        file_name = fd.askopenfilename(initialdir="/", title="Select file",
                                       filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if not file_name:
            return
        file_in = open(file_name, "r")
        text = file_in.read()
        self.textbox.delete('1.0', "end")
        self.textbox.insert('1.0', text)

    def save_event(self, event):
        self.save()

    def open_event(self, event):
        self.open()


root = tk.Tk()
app = DarkNotePad(master=root)
app.mainloop()
