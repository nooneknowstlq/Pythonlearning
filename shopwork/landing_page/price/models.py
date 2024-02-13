from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField(max_length=30, verbose_name="Цена")
    pc_description = models.CharField(max_length=200, verbose_name="Описание")

    def __str__(self):
        return self.pc_description

    class Meta:
        verbose_name = 'цену'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name="Товар")
    pt_price = models.CharField(max_length=200, verbose_name="Цена")

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

