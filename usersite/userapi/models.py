from django.db import models

# User models is created here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    def __str__(self):
       return self.name