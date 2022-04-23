from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields import NullBooleanField
from map.models import Unit, Customer

from openpyxl import load_workbook
from decimal import Decimal

# Получить список строк из таблицы <filename>, листа <sheet>
def arrayFromSheet(filename: str, sheet: int) -> list:
    wb = load_workbook(filename=filename).worksheets[sheet]
    array = []
    for row in wb.values:
        array.append(row)
    return array[1:]  # Пропускаем заголовок таблицы


class Command(BaseCommand):
    help = "Загрузка КП"    

    def handle(self, *args, **options):
        array = arrayFromSheet('_data.xlsx', 6)
        for row in array:
            cp = Unit()
            try:
                cp.n_mt = int(row[0])
                cp.address = row[2]
                cp.lat = float(round(row[3], 6))
                cp.lon = float(round(row[4], 6))
                cp.municipalDistrict = row[6]
                cp.city = row[7]
                cp.cityDistrict = row[8]
                cp.save()
            except Exception as e:
                with open("errorLog_cp.txt", "a") as f:
                    error = []
                    for cell in row:
                        error.append(cell)
                    error.append(e)
                    f.write(error.__str__() + "\n")
                    

