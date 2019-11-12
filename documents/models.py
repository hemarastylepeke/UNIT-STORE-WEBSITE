from django.db import models
import datetime

# Create your models here.

class Book(models.Model):
	numbering = models.AutoField(primary_key=True)
	title = models.CharField(max_length=500)
	code = models.CharField(max_length=50)
	date = models.DateField(("Date"),default=datetime.date.today)
	pdf = models.FileField(upload_to='books/')

	def __str__(self):
		return self.title


