from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email=models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=20, primary_key = True)
    phone = models.CharField(max_length=11)
    address_street = models.CharField(max_length=20)
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=2)
    address_zip = models.CharField(max_length=10)
    account_type = models.CharField(max_length=1)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def Address(self):
        return self.address_street + ", " + self.address_city + ", " + self.address_state + " " + self.address_zip

class WaterSourceReport(models.Model):
    reporter_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    report_number = models.AutoField(primary_key=True)
    water_type = models.CharField(max_length=20)
    water_condition = models.CharField(max_length=20)
    water_location = models.CharField(max_length=50, unique=True)
    report_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "Number: " + str(self.report_number) + \
               " Water Type: " + self.water_type + " Water Condition: " + self.water_condition + " Water Location: " + self.water_location

    def __eq__(self, other):
        return self.report_number == other.report_number and self.water_location == other.water_location

class WaterPurityReport(models.Model):
    reporter_name=models.ForeignKey(Account, on_delete=models.CASCADE)
    report_number = models.AutoField(primary_key=True)
    water_location = models.ForeignKey(WaterSourceReport, to_field = 'water_location', on_delete=models.CASCADE)
    water_condition = models.CharField(max_length=20)
    virus_ppm = models.IntegerField(null=False)
    contaminant_ppm = models.IntegerField(null=False)
    report_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "Number: " + self.report_number + " Date: " + self.report_date + " Water Location: " + self.water_location + \
               " Water Condition: " + self.water_condition + " Contaminant PPM: " + self.contaminant_ppm + \
               " Virus PPM: " + self.virus_ppm






