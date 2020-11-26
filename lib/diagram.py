import matplotlib.pyplot as plt
import uuid
import operator


class Diagram:
    def sort_data(self, a, b):
        for i in range(len(a)):
            for j in range(len(a) - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    b[j], b[j + 1] = b[j + 1], b[j]
        return a, b

    def create(self, columns: list, values: list, column: str, value: str) -> str:
        sort_date = self.sort_data(values, columns)
        unique = str('img/{}.png'.format(uuid.uuid4()))
        plt.xlabel(column.title())
        plt.ylabel(value.title())
        plt.title('Diagram', fontsize=20, fontname='Times New Roman')
        plt.bar(sort_date[1], sort_date[0])
        plt.savefig(unique)

        return unique
