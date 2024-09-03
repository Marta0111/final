from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    address = models.TextField(blank=True)
    company = models.CharField(max_length=100, blank=True)  # Přidání pole company
    note = models.TextField(blank=True)
def __str__(self):
        return self.name
