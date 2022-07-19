from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    completion=models.BooleanField(default=False)

    class Meta:
        db_table="TODO"
        verbose_name_plural='ToDo app'
    def __str__(self):
        return self.title