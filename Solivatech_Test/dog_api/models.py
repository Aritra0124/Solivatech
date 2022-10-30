from django.db import models


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=250)
    size = models.CharField(choices=(('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')),
                            max_length=25, default='1')
    friendliness = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)
    trainability = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)
    sheddingamount = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)
    exerciseneeds = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING, db_constraint=False)
    gender = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    favoritefood = models.CharField(max_length=250)
    favoritetoy = models.CharField(max_length=250)

    def __str__(self):
        return self.name
