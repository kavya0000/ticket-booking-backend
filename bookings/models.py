from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    ticket_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_name}"

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField()  # or whatever type you need
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





