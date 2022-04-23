from django.db import models
from django.db.models.deletion import DO_NOTHING

# КП
class Unit(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Широта")
    lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Долгота")

    n_mt = models.IntegerField(verbose_name="Идентификатор в MT", unique=True)

    address = models.CharField(
        verbose_name="Адрес площадки", max_length=200, blank=True, null=True
    )
    municipalDistrict = models.CharField(
        verbose_name="Муниципальное образование", max_length=100, blank=True, null=True
    )
    cityDistrict = models.CharField(
        verbose_name="Городской округ", max_length=100, blank=True, null=True
    )
    city = models.CharField(
        verbose_name="Населенный пункт", max_length=100, blank=True, null=True
    )

    def __str__(self):
        return str(self.address) + " | " + str(self.n_mt)

    class Meta:
        verbose_name_plural = "Контейнерные площадки"
        verbose_name = "Контейнерная площадка"
        ordering = ["n_mt", "address", "municipalDistrict", "cityDistrict", "city"]

# Жилой фонд
class Customer(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Широта")
    lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Долгота")

    unit = models.ForeignKey(
        Unit,
        db_column="n_mt",
        on_delete=models.PROTECT,
        verbose_name="Номер в МТ",
        blank=True,
        null=True,
    )

    # МО <- Город <- Район города
    municipalDistrict = models.CharField(
        verbose_name="МО", max_length=100, blank=True, null=True
    )  # A

    city = models.CharField(
        verbose_name="НП", max_length=100, blank=True, null=True
    )  # B
    cityDistrict = models.CharField(
        verbose_name="Район города", max_length=100, blank=True, null=True
    )  # C

    # ул./пер.+ Название улицы + ,Номер дома + крп/литера/дробь
    prefix = models.CharField(
        verbose_name="Параметр", max_length=100, blank=True, null=True
    )
    street = models.CharField(
        verbose_name="Адрес", max_length=100, blank=True, null=True
    )
    building = models.CharField(max_length=100, verbose_name="Дом", blank=True, null=True)
    postfix = models.CharField(
        verbose_name="Корпус", max_length=3, blank=True, null=True
    )

    def __str__(self):
        return str(
            str(self.prefix)
            + " "
            + str(self.street)
            + " "
            + str(self.building)
            + " "
            + str(self.postfix)
        )

    class Meta:
        verbose_name_plural = "Жилой фонд"
        verbose_name = "Жилой фонд"
        ordering = ["street"]
