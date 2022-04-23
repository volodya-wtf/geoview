from map.views import unit
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
    help = "Загрузка Клиентов"
    
        
    def handle(self, *args, **options):
        array = arrayFromSheet('_data.xlsx', 0)
        for row in array:
            try:
                ap = Customer()
                ap.municipalDistrict = row[0] # Муниципальное образование
                ap.city = row[1] # Город
                ap.cityDistrict = row[2]  # Район города
                
                if isinstance(row[6], str): # Параметр существует?
                    ap.street = row[6] + " " + row[5] # Параметр + Улица
                else: ap.street = row[5]

                ap.building = row[7] # Номер дома                
                ap.postfix = row[8] # Корпус
                
                try:
                    ap.lat = Decimal(row[3])
                    ap.lon = Decimal(row[4])
                except:
                    with open("errorLog_ap_lat_lon.txt", "a") as f:
                        f.write(error.__str__() + "\n")
                        continue

                if not row[10]:
                    ap.unit = None
                try:
                    cp = Unit.objects.get(n_mt=int(row[10]))
                    ap.unit = cp
                except:
                    ap.unit = None
                ap.save()

            except Exception as e:
                with open("errorLog_ap.txt", "a") as f:
                    error = []
                    for cell in row:
                        error.append(cell)
                    error.append(e)
                    f.write(error.__str__() + "\n")             


