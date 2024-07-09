from django.db import models
from django.utils import timezone

class Operator(models.Model):
    WORK_GROUP_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    personnel_code = models.CharField(max_length=100, unique=True, verbose_name='کد پرسنلی')
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    contact_number = models.CharField(max_length=15, verbose_name='شماره تماس')
    position = models.CharField(max_length=200, verbose_name='سمت')
    work_group = models.CharField(max_length=1, choices=WORK_GROUP_CHOICES, verbose_name='گروه کاری')
    delivered_device = models.CharField(max_length=200, verbose_name='دستگاه تحویلی')
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatars/default_avatar.png', verbose_name='تصویر اپراتور')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Device(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='کد دستگاه')
    name = models.CharField(max_length=200, verbose_name='نام دستگاه')

    def __str__(self):
        return self.name

class Failure(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='failures')
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='failures')
    type = models.CharField(max_length=200, verbose_name='نوع خرابی')
    description = models.TextField(verbose_name='توضیحات')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='زمان گزارش')

    def __str__(self):
        return f"{self.device.name} - {self.type}"

class Load(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='loads')
    amount = models.IntegerField(verbose_name='تعداد بار')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='زمان ثبت بار')

    def __str__(self):
        return f"{self.operator} - {self.amount}"
