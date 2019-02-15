from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class compound(models.Model):
	formula_name=models.CharField(max_length=100)
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	extensibility=models.CharField(max_length=100)
	stability=models.CharField(max_length=100)
	ductibility=models.CharField(max_length=100)
	toughness=models.CharField(max_length=100)
	strenght=models.CharField(max_length=100)
	pvc_k=models.CharField(max_length=100)
	stabilizer_type=models.CharField(max_length=100)
	stabilizer=models.CharField(max_length=100)
	chalk=models.CharField(max_length=100)
	impact_modifier=models.CharField(max_length=100)
	def __str__(self):
		return self.formula_name
	#formula1=compound(formula_name='T201',extensibility='12',stability='13',ductibility='14',toughness='15',strenght='3',pvc_k='5',stabilizer_type='56',stabilizer='123',chalk='67',impact_modifier='23',author=user)
	def get_absolute_url(self):
		return reverse('compound-detail',kwargs={'pk':self.pk}) 
   
