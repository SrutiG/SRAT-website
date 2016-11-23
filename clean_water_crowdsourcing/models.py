from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
    type_choices = (("U", "User"), ("W", "Worker"), ("M", "Manager"), ("A", "Admin"))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key = True)
    address_street = models.CharField(max_length=20)
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=2)
    address_zip = models.CharField(max_length=10)
    account_type = models.CharField(choices=type_choices, max_length=1)

    def __str__(self):
        return self.first_name + self.last_name
