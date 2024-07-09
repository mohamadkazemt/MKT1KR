from django.db import models

class Operator(models.Model):
    WORK_GROUP_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    personnel_code = models.CharField(max_length=100, unique=True, verbose_name='کد پرسنلی')
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    contact_number = models.CharField(max_length=15, verbose_name='شماره تماس')
    position = models.CharField(max_length=100, verbose_name='سمت')
    work_group = models.CharField(max_length=1, choices=WORK_GROUP_CHOICES, verbose_name='گروه کاری')
    delivered_device = models.CharField(max_length=100, verbose_name='دستگاه تحویلی')
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatars/default_avatar.png', verbose_name='تصویر اپراتور')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FailureReport(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='failure_reports')
    device_name = models.CharField(max_length=100, verbose_name='نام دستگاه')
    failure_type = models.CharField(max_length=200, verbose_name='نوع خرابی')
    report_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ گزارش')

    def __str__(self):
        return f"{self.device_name} - {self.failure_type}"

class LoadReport(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='load_reports')
    load_count = models.PositiveIntegerField(default=0, verbose_name='تعداد بار')
    report_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ گزارش')

    def __str__(self):
        return f"{self.operator} - {self.load_count}"
