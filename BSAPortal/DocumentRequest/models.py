from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField
    username = models.CharField(max_length=25)


class Resident(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    present_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Document(models.Model):
    doc_type = models.BigAutoField
    res_name = models.ForeignKey(Resident, on_delete=models.CASCADE)
