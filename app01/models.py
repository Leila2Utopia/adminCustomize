from django.db import models

# Create your models here.
class Author(models.Model):

    name=models.CharField( max_length=32)
    age=models.IntegerField()


    def __str__(self):
        return self.name

class Publish(models.Model):

    name=models.CharField( max_length=32)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    publisher=models.ForeignKey(to="Publish")
    authors=models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title