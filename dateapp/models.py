from django.db import models

class Search(models.Model):
    male_number=models.DecimalField(max_digits=3, decimal_places=0)
    female_number=models.DecimalField(max_digits=3, decimal_places=0)
    situation=models.CharField(max_length=50)
    time=models.DurationField()


class Table(models.Model):
    schemaID = models.IntegerField()
    table_name = models.CharField(max_length=20)
    describe = models.TextField()