from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# type_value of entry
class Income(models.Model):
    # category of entry
    class IncomeTypes(models.IntegerChoices):
        SAL = 1, 'SALARY'
        BON = 2, 'BONUS'
        OTH = 3, 'OTHER'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # category of entry
    type = models.PositiveSmallIntegerField(choices=IncomeTypes.choices, default=1)
    notes = models.CharField(max_length=255, default='---')
    comment_to_notes = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'incomes'


# type_value of entry
class Outcome(models.Model):
    # category of entry
    class OutcomeTypes(models.IntegerChoices):
        BIL = 1, 'BILLS'
        GRO = 2, 'GROCERIES'
        CLO = 3, 'CLOTHES'
        STU = 4, 'STUDY'
        SPO = 5, 'SPORT'
        FUN = 6, 'FUN'
        HEA = 7, 'HEALTHY'
        HOM = 8, 'HOME'
        FAM = 9, 'FAMILY'
        GIF = 10, 'GIFT'
        OTH = 11, 'OTHER'
        SAV = 12, 'SAVING'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outcomes')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # category of entry
    type = models.PositiveSmallIntegerField(choices=OutcomeTypes.choices, default=1)
    notes = models.CharField(max_length=64, default='---')
    comment_to_notes = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Outcome {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'outcomes'


# type_value of entry
class Balance(models.Model):
    # category of entry
    class BalanceTypes(models.IntegerChoices):

        CUR = 1, 'CURRENT'
        SAV = 2, 'SAVING'

    # _id = str(uuid.uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balances')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # category of entry
    type = models.PositiveSmallIntegerField(choices=BalanceTypes.choices, default=1)
    notes = models.CharField(max_length=64, default='---')
    comment_to_notes = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Balance {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'balances'
