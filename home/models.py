from django.db import models

class Contact(models.Model):
    Name = models.CharField(max_length=50)  # Use lowercase 'name' instead of 'Name'
    Email = models.EmailField()
    Number = models.CharField(max_length=15)
    Description = models.TextField()

    def __str__(self):
        return self.Name

