from django.db import models

# Create your models here   .


class User(models.Model):
    user_id = models.BigAutoField
    username = models.CharField(max_length=25)

class Admin(User):

class Transaction(models.Model):
    transactionID = models.BigAutoField
    transaction_userid = models.ForeignKey(User, on_delete=models.CASCADE)


