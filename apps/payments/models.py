from django.db import models

# Create your models here.
class PaymentStatus(models.TextChoices):
    PENDING = "P", "pending"
    COMPLETED = "C", "completed"
    REFUNDED = "RF", "refunded"
    FAILED = "F", "failed"
    ABANDONED = "A", "abandoned"
    REVOKED = "RV", "revoked"
    PRE_APPROVED = "PA", "preapproved"
    ON_HOLD = "OH", "on_hold"
    CANCELLED = "CA", "canceled"
     

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=2, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )
    payment_date = models.DateTimeField(blank=False)