from django.contrib.auth.models import User
from django.db import models


class Tour(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)


class Discount(models.Model):
    PROMO = "promo"
    CAMPAIGN = "campaign"
    DISCOUNT = "discount"
    CATEGORIES = [(PROMO, "Промокод"), (CAMPAIGN, "Акция"), (DISCOUNT, "Скидка")]

    category = models.CharField(max_length=8, choices=CATEGORIES, default=PROMO)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    discount = models.PositiveSmallIntegerField(default=10)
    code = models.CharField(max_length=20, default='SkyPro')
    starts_at = models.DateTimeField(null=True)
    ends_at = models.DateTimeField(null=True)

