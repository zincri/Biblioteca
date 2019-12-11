from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lender(User):
    def __str__(self):
        return str(self.id)+" - "+self.username
    def name(self):
        return str(self.username)