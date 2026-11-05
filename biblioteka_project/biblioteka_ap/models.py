from django.db import models


class books(models.Model):
    name = models.CharField(max_length=100)
    year_of_realese = models.IntegerField()

    def __str__(self):
        return str(self.name)


class autor(models.Model):
    name = models.CharField()
    surname = models.CharField()

    def __str__(self):
        return str(self.name)


class categories(models.Model):
    ganre = models.CharField()
    description = models.TextField()

    def __str__(self):
        return str(self.ganre)

class Reader(models.Model):
    name = models.CharField(max_length=100)
    which_ganre_like = models.TextField()
    
    def __str__(self):
        return str(self.name)


    