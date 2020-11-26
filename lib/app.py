from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import json
from lib import excel


class App:
    def __init__(self):
        self.display = None
        self.data = None
        self.export_menu = None
        self.window = Tk()
        self.window.title('Empty File')
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.main_menu = Menu(self.menu, tearoff=0)
        self.main_menu.add_command(label='Open JSON', command=self.open_json)
        self.menu.add_cascade(label='Main', menu=self.main_menu)

    def run(self):
        self.window.mainloop()

    def open_json(self):
        file_name = filedialog.askopenfilename(defaultextension='.json', filetypes=[('JSON files', '*.json')])

        try:
            with open(file_name) as file:
                self.data = json.load(file)
        except OSError:
            pass

        if self.data:
            self.window.title(file_name)
            self.show_data()
            self.create_export_menu()

        return 1

    def show_data(self):
        if self.display:
            self.display.destroy()
            self.menu.delete('Export')

        self.display = Frame(self.window)

        for i in self.data:
            Label(self.display, text=self.data[i], font=('Arial', 20)).pack()
        self.display.pack(side=TOP, expand=1)

        return 1

    def create_excel(self):
        save_as = filedialog.asksaveasfilename(filetypes=[('Excel Document', '*.xlsx')], defaultextension=".xlsx")
        if not save_as:
            return

        excel.Excel(save_as).create(self.data)
        self.window.title('Empty File')
        messagebox.showinfo('Success!', 'Successful export to excel!')
        self.display.destroy()
        self.menu.delete('Export')

        return 1

    def create_export_menu(self):
        self.export_menu = Menu(self.menu, tearoff=0)
        self.export_menu.add_command(label='To Excel', command=self.create_excel)
        self.menu.add_cascade(label='Export', menu=self.export_menu)

        return 1
