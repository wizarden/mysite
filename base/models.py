from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    des = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


