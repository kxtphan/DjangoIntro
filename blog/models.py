from django.db import models
from django.conf import settings
from django.utils import timezone


# Defines the model (this is an object)
# models.Model means that Post is a Django Model, so it is saved in database
class Post(models.Model):
    # Link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Define text with a limited number of characters
    title = models.CharField(max_length=200)
    # Define long text with no limit on number of characters
    text = models.TextField()
    # Date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Add model to db with 'python manage.py makemigrations blog' and 'python manage.py migrate'
