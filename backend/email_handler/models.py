from django.db import models
from users.models import User
# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: ${self.amount} on {self.date.strftime('%Y-%m-%d')}"

