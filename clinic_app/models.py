from django.db import models
from django.contrib.auth.models import AbstractUser


class Signup(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    class Meta:
        
        # Set the related_name for user_permissions and groups
        permissions = (
            ('can_view_special', 'Can view special pages'),
            
        )
# Specify related_name for groups and user_permissions fields
Signup._meta.get_field('groups').remote_field.related_name = 'user_groups'
Signup._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions_set'        
        
class HomePage(models.Model):
    """
    Model class for storing information about the home page.

    Inherits from Django's models.Model class.
    """

    # Method to represent the object as a string
    def __str__(self):
        return self.title

class AboutUs(models.Model):
    """
    Model class for storing about us information.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # Method to represent the object as a string
    def __str__(self):
        return self.title

