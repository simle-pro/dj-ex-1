from django.db import models

class Autor(models.Model):
    firstn = models.CharField(max_length=50)
    lastn = models.CharField(max_length=50)
    birth_d = models.CharField(max_length=50)

    def __str__(self):
        return self.firstn
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    Autor = models.ForeignKey("Autor", on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.IntegerField()
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.title
