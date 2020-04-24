from django.db import models

class Province(models.Model):
		province_id = models.IntegerField(null=False)
		province_name = models.CharField(max_length=70)
		latitude_prov = models.DecimalField(max_digits=9, decimal_places=6)
		longitude_prov = models.DecimalField(max_digits=9, decimal_places=6)

class DbPerson(models.Model):
    	personid = models.IntegerField(null=True)
    	first_name = models.CharField(max_length=100)
    	last_name = models.CharField(max_length=100)