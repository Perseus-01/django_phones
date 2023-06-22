from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100) #это не было в презентации/лекции

    # про разные атрибуты у models - не было в лекции/презентации - почему?
