from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class words(models.Model):
     words_text=models.CharField(max_length=100)
     words_number=models.IntegerField(default=0)
     def __str__(self):
          return self.words_text
