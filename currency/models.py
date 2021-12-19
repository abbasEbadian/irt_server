from django.db import models

class History(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DecimalField(max_digits=10, decimal_places=0)  

    def __repr__(self):
        return str(self.name) + " " + str(self.timestamp) + " " + str(price)

    class Meta:
        ordering = ['timestamp']
