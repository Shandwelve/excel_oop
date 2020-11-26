from xlsxwriter import *
import uuid
from lib import diagram


class Excel:
    def __init__(self):
        self.columns = None
        self.data = None
        self.workbook = Workbook('xls/{}.xlsx'.format(uuid.uuid4()))
        self.worksheet = self.workbook.add_worksheet()
        self.style1 = self.workbook.add_format()
        self.style2 = self.workbook.add_format()
        self.make_styles()

    def make_styles(self):
        self.style1.set_align('right')

        self.style2.set_font_color('red')
        self.style2.set_align('center')
        self.style2.set_underline()
        self.style2.set_bold()
        self.style2.set_border()

    def create(self, data: dict):
        self.columns = list(data[next(iter(data))].keys())
        self.data = data
        last_column = self.make_header() + 1
        self.make_body()
        self.add_diagram(last_column, 'name', 'marks_average')
        self.workbook.close()

    def make_header(self) -> int:
        column = 0
        for i in self.columns:
            self.worksheet.write(0, column, i, self.style2)
            self.worksheet.set_column(0, column, 20)
            column += 1

        return column

    def make_body(self):
        row = 1
        for i in self.data:
            column = 0
            for j in self.columns:
                self.worksheet.write(row, column, self.data[i][j], self.style1)
                column += 1
            row += 1

    def add_diagram(self, position: int, column: str, value: str):
        columns = []
        values = []
        for i in self.data:
            columns.append(self.data[i][column])
            values.append(self.data[i][value])

        bar_diagram = diagram.Diagram()
        img = bar_diagram.create(columns, values, column, value)
        self.worksheet.insert_image(0, position, img)
