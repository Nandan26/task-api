from django.db import models



class Task(models.Model):
    '''
    Task model with two fields
    '''

    title = models.CharField(max_length= 100)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
