from django.db import models
from Customer.models import Customer


class SanctionedLoan(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    required_loan = models.IntegerField(default=None)
    approved_loan = models.IntegerField(default=None)
    tenure = models.IntegerField(default=None)
    interest = models.FloatField(default=None)
    emi = models.FloatField(default=0.0, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer},{self.required_loan},{self.approved_loan},{self.tenure},{self.interest},{self.emi},{self.is_approved}"
