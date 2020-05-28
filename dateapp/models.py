from django.db import models

class Search(models.Model):
    male_number=models.DecimalField(max_digits=3, decimal_places=0)
    female_number=models.DecimalField(max_digits=3, decimal_places=0)
    situation=models.CharField(max_length=50)
    time=models.DurationField()

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.situation

class Table(models.Model):
    schemaID = models.IntegerField()
    table_name = models.CharField(max_length=20)
    describe = models.TextField()

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.table_name