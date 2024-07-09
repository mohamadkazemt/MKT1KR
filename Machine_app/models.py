from django.db import models

class Machine(models.Model):
    MACHINE_TYPE_CHOICES = [
        ('Carrier', 'حمل کننده'),
        ('Loader', 'بارکننده'),
    ]

    code = models.CharField(max_length=100, unique=True, verbose_name='کد دستگاه')
    name = models.CharField(max_length=200, verbose_name='نام دستگاه')
    type = models.CharField(max_length=50, choices=MACHINE_TYPE_CHOICES, verbose_name='نوع دستگاه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name

class Operation(models.Model):
    OPERATION_TYPE_CHOICES = [
        ('Start', 'شروع بکار'),
        ('Stop', 'توقف'),
    ]

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='operations')
    operator = models.CharField(max_length=200, verbose_name='اپراتور')
    type = models.CharField(max_length=50, choices=OPERATION_TYPE_CHOICES, verbose_name='نوع عملیات')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='زمان عملیات')

    def __str__(self):
        return f"{self.machine.name} - {self.get_type_display()} - {self.operator}"

class Failure(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='failures')
    type = models.CharField(max_length=200, verbose_name='نوع خرابی')
    description = models.TextField(verbose_name='توضیحات')
    reported_by = models.CharField(max_length=200, verbose_name='گزارش شده توسط')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='زمان گزارش')

    def __str__(self):
        return f"{self.machine.name} - {self.type}"
