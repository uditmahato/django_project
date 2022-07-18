from django.db import models

# Create your models here.
class about_t(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name +' '+self.last_name +' '+self.email +' '+self.phone