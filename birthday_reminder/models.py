from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=250)
    active=models.BooleanField(default = False)

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    nickname = models.CharField(max_length=250)
    group = models.ForeignKey(Group,on_delete=models.ForeignKey)
    birth_date = models.DateField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name} - {self.nickname}'
