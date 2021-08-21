from django.db import models

# Create your models here.
class Note(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    def __str__(self):
        return self.text

class Date(models.Model):
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Topic(models.Model):
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    learn=models.BooleanField(default=False)
    work=models.BooleanField(default=False)
    idea=models.BooleanField(default=False)
    life=models.BooleanField(default=False)
    def __str__(self):
        return self.text
