from django.db import models

class Operator(models.Model):
    personnel_code = models.CharField(max_length=100, unique=True, verbose_name='کد پرسنلی')
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    contact_number = models.CharField(max_length=200, verbose_name='شماره تماس')
    position = models.CharField(max_length=200, verbose_name='سمت')
    work_group = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], verbose_name='گروه کاری')
    delivered_device = models.CharField(max_length=200, verbose_name='دستگاه تحویلی')
    photo = models.ImageField(upload_to='operator_photos/', blank=True, null=True, verbose_name='عکس اپراتور')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
