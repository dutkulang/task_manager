from django.db import models

class Task(models.Model):
    TASK_STATUS = (
        ('C', 'Completed'),
        ('P', 'Pending'),
        ('S', 'Started'),
        ('A', 'Abandon')
    )
    title = models.CharField(
        max_length=30
    )
    details = models.TextField()
    assigned_to = models.CharField(max_length=39)
    status = models.CharField(
        max_length=1, choices=TASK_STATUS
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=30)


    def __str__(self):
        return self.title