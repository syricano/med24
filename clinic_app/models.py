from django.db import models


class HomePage(models.Model):
    """
    Model class for storing information about the home page.

    Inherits from Django's models.Model class.
    """

    # Method to represent the object as a string
    def __str__(self):
        return self.title