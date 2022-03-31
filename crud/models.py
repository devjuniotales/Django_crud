import uuid
from django.db import models

# Create your models here.


class User(models.Model) :
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)


    def __str__(self) -> str:
        return str.name

