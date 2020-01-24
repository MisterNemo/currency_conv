from django.db import models


class Currency(models.Model):
    code = models.CharField(
        max_length=4,
        verbose_name="currency_code",
        unique=True
    )
    rate = models.FloatField(
        verbose_name="currency_rate"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        verbose_name='created_at'
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        verbose_name='modified_at'
    )



