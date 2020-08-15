from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    people = models.IntegerField()
    memo = models.TextField()
    m_d = models.CharField(max_length=5)
    def __str__(self):
        return self.name
