from django.db import models

from apps.company.models import CompanySubscription

# Create your models here.

# Modèle de paiement
class PaymentTransaction(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    )
    transaction_id = models.AutoField(primary_key=True)
    subscription = models.ForeignKey(CompanySubscription, on_delete=models.CASCADE, verbose_name="Abonnement")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant du paiement")
    payment_date = models.DateField(verbose_name="Date de paiement")
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES, verbose_name="Statut de paiement")
    def __str__(self):
        return f"Transaction ID: {self.transaction_id} - Status: {self.get_payment_status_display()}"